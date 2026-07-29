"""Ansible plugin for Infra Pilot - playbooks, inventory, roles, modules, tasks, variables, templates, handlers, collections, galaxy, vault, facts, callbacks, connections, strategies, execution, results, reporting, ansible.cfg management, module discovery, role management, playbook creation, ad-hoc commands, dynamic inventory, plugin management, filter plugins, lookup plugins, test plugins, action plugins, cache plugins, callback plugins, connection plugins, inventory plugins, shell plugins, strategy plugins, vars plugins"""

import json
import logging
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    import ansible_runner
    import ansible.constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase
    HAS_ANSIBLE = True
except ImportError:
    HAS_ANSIBLE = False
    ansible_runner = None
    PlaybookExecutor = None


class AnsibleError(Exception):
    pass


class ResultCallback(CallbackBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.results = {"plays": [], "hosts": {}, "stats": {}, "failures": [], "unreachable": []}

    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host.get_name()
        task = result.task_name or "unknown"
        self.results["hosts"].setdefault(host, []).append({"task": task, "status": "ok", "result": result._result})

    def v2_runner_on_failed(self, result, **kwargs):
        host = result._host.get_name()
        task = result.task_name or "unknown"
        self.results["hosts"].setdefault(host, []).append({"task": task, "status": "failed", "result": result._result, "msg": result._result.get("msg", "")})
        self.results["failures"].append({"host": host, "task": task, "msg": result._result.get("msg", "")})

    def v2_runner_on_unreachable(self, result):
        host = result._host.get_name()
        self.results["hosts"].setdefault(host, []).append({"task": "connection", "status": "unreachable", "msg": result._result.get("msg", "")})
        self.results["unreachable"].append({"host": host, "msg": result._result.get("msg", "")})

    def v2_playbook_on_stats(self, stats):
        self.results["stats"] = {h: {"ok": s.ok, "failures": s.failures, "unreachable": s.unreachable, "changed": s.changed, "skipped": s.skipped, "rescued": s.rescued, "ignored": s.ignored} for h, s in stats.items() if hasattr(s, 'ok')}


class AnsibleManager:
    def __init__(self, inventory_path: Optional[str] = None, private_key: Optional[str] = None,
                 remote_user: Optional[str] = None, become: bool = False,
                 become_user: Optional[str] = None, become_method: Optional[str] = None,
                 forks: int = 10, timeout: int = 30, ansible_config: Optional[str] = None):
        self.inventory_path = inventory_path or self._default_inventory()
        self.private_key = private_key
        self.remote_user = remote_user
        self.become = become
        self.become_user = become_user
        self.become_method = become_method or "sudo"
        self.forks = forks
        self.timeout = timeout
        self.ansible_config = ansible_config
        self._connected = False
        if HAS_ANSIBLE:
            self._connected = True

    def _default_inventory(self) -> str:
        return os.path.join(os.path.expanduser("~"), ".ipilot", "ansible", "inventory.yml")

    def check_connection(self) -> bool:
        return HAS_ANSIBLE

    def run_playbook(self, playbook_path: str, extra_vars: Optional[Dict] = None,
                     inventory: Optional[str] = None, limit: Optional[str] = None,
                     tags: Optional[List[str]] = None, skip_tags: Optional[List[str]] = None,
                     check_mode: bool = False, diff: bool = False,
                     vault_password: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise AnsibleError("Ansible is not installed")
        try:
            if ansible_runner:
                kwargs = {"playbook": playbook_path, "inventory": inventory or self.inventory_path, "quiet": True, "cancel_callback": lambda: False}
                if extra_vars:
                    kwargs["extravars"] = extra_vars
                if limit:
                    kwargs["limit"] = limit
                if tags:
                    kwargs["tags"] = tags
                if check_mode:
                    kwargs["check"] = True
                if diff:
                    kwargs["diff"] = True
                if vault_password:
                    kwargs["vault_pass"] = vault_password
                if self.private_key:
                    kwargs["ssh_key"] = self.private_key
                if self.remote_user:
                    kwargs["remote_user"] = self.remote_user
                if self.become:
                    kwargs["become"] = True
                    kwargs["become_user"] = self.become_user or "root"
                r = ansible_runner.run(**kwargs)
                return {
                    "status": r.status, "rc": r.rc,
                    "ok": r.stats.get("ok", {}) if r.stats else {},
                    "failures": r.stats.get("failures", {}) if r.stats else {},
                    "unreachable": r.stats.get("unreachable", {}) if r.stats else {},
                    "changed": r.stats.get("changed", {}) if r.stats else {},
                    "skipped": r.stats.get("skipped", {}) if r.stats else {},
                    "playbook": playbook_path, "success": r.status == "successful",
                }
            else:
                loader = DataLoader()
                inventory = InventoryManager(loader=loader, sources=inventory or self.inventory_path)
                variable_manager = VariableManager(loader=loader, inventory=inventory)
                if extra_vars:
                    variable_manager.extra_vars = extra_vars
                passwords = {}
                if vault_password:
                    passwords["vault_pass"] = vault_password
                cb = ResultCallback()
                executor = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
                executor._tqm._stdout_callback = cb
                executor.run()
                return {"results": cb.results, "playbook": playbook_path, "success": len(cb.results.get("failures", [])) == 0 and len(cb.results.get("unreachable", [])) == 0}
        except Exception as e:
            raise AnsibleError(f"Failed to run playbook: {e}")

    def run_ad_hoc(self, module: str, args: str, hosts: str = "all",
                   inventory: Optional[str] = None, extra_vars: Optional[Dict] = None,
                   become: Optional[bool] = None, check_mode: bool = False) -> Dict:
        if not self.check_connection():
            raise AnsibleError("Ansible is not installed")
        try:
            if ansible_runner:
                kwargs = {
                    "module": module, "host_pattern": hosts,
                    "inventory": inventory or self.inventory_path,
                    "quiet": True, "cancel_callback": lambda: False,
                }
                if args:
                    kwargs["module_args"] = args
                if extra_vars:
                    kwargs["extravars"] = extra_vars
                if become is not None:
                    kwargs["become"] = become
                if check_mode:
                    kwargs["check"] = True
                if self.private_key:
                    kwargs["ssh_key"] = self.private_key
                if self.remote_user:
                    kwargs["remote_user"] = self.remote_user
                r = ansible_runner.run(**kwargs)
                return {
                    "status": r.status, "rc": r.rc,
                    "events": len(r.events),
                    "hosts": {h: {"status": s.get("status"), "changed": s.get("changed"), "rc": s.get("rc")} for h, s in (r.stats.get("ok", {}).items() if r.stats else {})},
                    "success": r.status == "successful",
                }
            else:
                return {"note": "ansible-runner not available, falling back to CLI", "command": f"ansible {hosts} -m {module} -a '{args}' -i {inventory or self.inventory_path}"}
        except Exception as e:
            raise AnsibleError(f"Failed to run ad-hoc command: {e}")

    def list_inventory_hosts(self, inventory: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise AnsibleError("Ansible is not installed")
        try:
            loader = DataLoader()
            inv = InventoryManager(loader=loader, sources=inventory or self.inventory_path)
            hosts = []
            for h in inv.get_hosts():
                vars = inv.get_vars(h.name)
                hosts.append({"name": h.name, "groups": [g.name for g in h.groups], "vars": {k: v for k, v in vars.items() if not k.startswith("_")}})
            return hosts
        except Exception as e:
            raise AnsibleError(f"Failed to list inventory: {e}")

    def list_groups(self, inventory: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise AnsibleError("Ansible is not installed")
        try:
            loader = DataLoader()
            inv = InventoryManager(loader=loader, sources=inventory or self.inventory_path)
            return [{"name": g.name, "hosts": [h.name for h in g.hosts], "children": [c.name for c in g.child_groups], "vars": g.vars} for g in inv.get_groups().values() if g.name not in ("all", "ungrouped")]
        except Exception as e:
            raise AnsibleError(f"Failed to list groups: {e}")

    def create_inventory_entry(self, hostname: str, group: str = "all",
                               vars: Optional[Dict] = None,
                               inventory: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise AnsibleError("Ansible is not installed")
        try:
            inv_path = inventory or self.inventory_path
            os.makedirs(os.path.dirname(inv_path), exist_ok=True)
            if inv_path.endswith((".yml", ".yaml")):
                import yaml
                if os.path.exists(inv_path):
                    with open(inv_path) as f:
                        data = yaml.safe_load(f) or {}
                else:
                    data = {}
                if group not in data:
                    data[group] = {"hosts": {}}
                if "hosts" not in data[group]:
                    data[group]["hosts"] = {}
                data[group]["hosts"][hostname] = vars or {}
                with open(inv_path, "w") as f:
                    yaml.dump(data, f, default_flow_style=False)
            else:
                with open(inv_path, "a") as f:
                    f.write(f"{hostname} ansible_host={vars.get('ansible_host', hostname)} ansible_user={vars.get('ansible_user', 'root')}\n")
            return {"host": hostname, "group": group, "inventory": inv_path}
        except Exception as e:
            raise AnsibleError(f"Failed to create inventory entry: {e}")

    def install_role(self, role_name: str, galaxy_server: Optional[str] = None, force: bool = False) -> Dict:
        if not self.check_connection():
            raise AnsibleError("Ansible is not installed")
        try:
            cmd = ["ansible-galaxy", "role", "install"]
            if force:
                cmd.append("--force")
            if galaxy_server:
                cmd.extend(["--server", galaxy_server])
            cmd.append(role_name)
            result = subprocess.run(cmd, capture_output=True, text=True)
            return {"role": role_name, "success": result.returncode == 0, "stdout": result.stdout, "stderr": result.stderr}
        except Exception as e:
            raise AnsibleError(f"Failed to install role: {e}")

    def install_collection(self, collection_name: str, galaxy_server: Optional[str] = None, force: bool = False) -> Dict:
        if not self.check_connection():
            raise AnsibleError("Ansible is not installed")
        try:
            cmd = ["ansible-galaxy", "collection", "install"]
            if force:
                cmd.append("--force")
            if galaxy_server:
                cmd.extend(["--server", galaxy_server])
            cmd.append(collection_name)
            result = subprocess.run(cmd, capture_output=True, text=True)
            return {"collection": collection_name, "success": result.returncode == 0, "stdout": result.stdout, "stderr": result.stderr}
        except Exception as e:
            raise AnsibleError(f"Failed to install collection: {e}")

    def list_roles(self) -> List[str]:
        try:
            cmd = ["ansible-galaxy", "role", "list"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            roles = []
            for line in result.stdout.split("\n"):
                line = line.strip()
                if line and not line.startswith("#") and not line.startswith("ansible-galaxy"):
                    roles.append(line)
            return roles
        except Exception as e:
            raise AnsibleError(f"Failed to list roles: {e}")

    def list_collections(self) -> List[str]:
        try:
            cmd = ["ansible-galaxy", "collection", "list"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            collections = []
            for line in result.stdout.split("\n"):
                line = line.strip()
                if line and not line.startswith("#") and not line.startswith("ansible-galaxy"):
                    collections.append(line)
            return collections
        except Exception as e:
            raise AnsibleError(f"Failed to list collections: {e}")

    def encrypt_vault(self, file_path: str, vault_password: str, output_file: Optional[str] = None, vault_id: Optional[str] = None) -> Dict:
        try:
            cmd = ["ansible-vault", "encrypt"]
            if vault_id:
                cmd.extend(["--vault-id", vault_id])
            if output_file:
                cmd.extend(["--output", output_file])
            cmd.append(file_path)
            result = subprocess.run(cmd, capture_output=True, text=True, input=vault_password + "\n" + vault_password + "\n")
            return {"file": file_path, "encrypted": True, "success": result.returncode == 0, "stdout": result.stdout, "stderr": result.stderr}
        except Exception as e:
            raise AnsibleError(f"Failed to encrypt vault: {e}")

    def decrypt_vault(self, file_path: str, vault_password: str, output_file: Optional[str] = None) -> Dict:
        try:
            cmd = ["ansible-vault", "decrypt"]
            if output_file:
                cmd.extend(["--output", output_file])
            cmd.append(file_path)
            result = subprocess.run(cmd, capture_output=True, text=True, input=vault_password + "\n")
            return {"file": file_path, "decrypted": True, "success": result.returncode == 0}
        except Exception as e:
            raise AnsibleError(f"Failed to decrypt vault: {e}")

    def edit_vault(self, file_path: str, vault_password: str, new_content: str) -> Dict:
        try:
            self.decrypt_vault(file_path, vault_password, output_file=file_path + ".decrypted")
            with open(file_path + ".decrypted", "w") as f:
                f.write(new_content)
            self.encrypt_vault(file_path + ".decrypted", vault_password, output_file=file_path)
            os.unlink(file_path + ".decrypted")
            return {"file": file_path, "edited": True}
        except Exception as e:
            raise AnsibleError(f"Failed to edit vault: {e}")

    def view_vault(self, file_path: str, vault_password: str) -> str:
        try:
            result = subprocess.run(["ansible-vault", "view", file_path], capture_output=True, text=True, input=vault_password + "\n")
            if result.returncode == 0:
                return {"content": result.stdout}
            raise AnsibleError(f"Failed to view vault: {result.stderr}")
        except Exception as e:
            raise AnsibleError(f"Failed to view vault: {e}")

    def create_playbook(self, name: str, hosts: str = "all", become: bool = True,
                        tasks: Optional[List[Dict]] = None, vars: Optional[Dict] = None,
                        roles: Optional[List[str]] = None, path: Optional[str] = None) -> Dict:
        try:
            playbook = [{"name": name, "hosts": hosts, "become": become}]
            if vars:
                playbook[0]["vars"] = vars
            if roles:
                playbook[0]["roles"] = roles
            if tasks:
                playbook[0]["tasks"] = tasks
            else:
                playbook[0]["tasks"] = [{"name": "Debug info", "ansible.builtin.debug": {"msg": "Default task from Infra Pilot"}}]
            pb_path = path or os.path.join(os.path.expanduser("~"), ".ipilot", "ansible", f"{name.replace(' ', '_')}.yml")
            os.makedirs(os.path.dirname(pb_path), exist_ok=True)
            import yaml
            with open(pb_path, "w") as f:
                yaml.dump(playbook, f, default_flow_style=False)
            return {"name": name, "path": pb_path, "hosts": hosts, "tasks": len(playbook[0]["tasks"]), "roles": roles}
        except Exception as e:
            raise AnsibleError(f"Failed to create playbook: {e}")

    def ping(self, hosts: str = "all", inventory: Optional[str] = None) -> Dict:
        return self.run_ad_hoc(module="ansible.builtin.ping", args="", hosts=hosts, inventory=inventory)

    def gather_facts(self, hosts: str = "all", inventory: Optional[str] = None) -> Dict:
        return self.run_ad_hoc(module="ansible.builtin.setup", args="", hosts=hosts, inventory=inventory)

    def check_connectivity(self, hosts: str = "all", inventory: Optional[str] = None) -> Dict:
        return self.run_ad_hoc(module="ansible.builtin.ping", args="", hosts=hosts, inventory=inventory)

    def shell_command(self, hosts: str, command: str, inventory: Optional[str] = None, become: bool = False) -> Dict:
        return self.run_ad_hoc(module="ansible.builtin.shell", args=command, hosts=hosts, inventory=inventory, become=become)

    def copy_file(self, hosts: str, src: str, dest: str, inventory: Optional[str] = None, become: bool = False) -> Dict:
        return self.run_ad_hoc(module="ansible.builtin.copy", args=f"src={src} dest={dest}", hosts=hosts, inventory=inventory, become=become)

    def file_operations(self, hosts: str, path: str, state: str = "directory", mode: Optional[str] = None,
                        owner: Optional[str] = None, group: Optional[str] = None,
                        inventory: Optional[str] = None, become: bool = False) -> Dict:
        args = f"path={path} state={state}"
        if mode: args += f" mode={mode}"
        if owner: args += f" owner={owner}"
        if group: args += f" group={group}"
        return self.run_ad_hoc(module="ansible.builtin.file", args=args, hosts=hosts, inventory=inventory, become=become)

    def package_manager(self, hosts: str, name: str, state: str = "present",
                        package_type: str = "apt", inventory: Optional[str] = None,
                        become: bool = True) -> Dict:
        if package_type in ("apt", "apt-get"):
            module = "ansible.builtin.apt"
        elif package_type in ("yum", "dnf"):
            module = "ansible.builtin.yum"
        elif package_type == "pip":
            module = "ansible.builtin.pip"
        else:
            module = f"ansible.builtin.{package_type}"
        return self.run_ad_hoc(module=module, args=f"name={name} state={state}", hosts=hosts, inventory=inventory, become=become)

    def service_management(self, hosts: str, name: str, state: str = "started",
                           enabled: Optional[bool] = None, inventory: Optional[str] = None,
                           become: bool = True) -> Dict:
        args = f"name={name} state={state}"
        if enabled is not None: args += f" enabled={str(enabled).lower()}"
        return self.run_ad_hoc(module="ansible.builtin.service", args=args, hosts=hosts, inventory=inventory, become=become)

    def systemd_daemon_reload(self, hosts: str, inventory: Optional[str] = None, become: bool = True) -> Dict:
        return self.run_ad_hoc(module="ansible.builtin.systemd", args="daemon_reload=yes", hosts=hosts, inventory=inventory, become=become)

    def docker_container_management(self, hosts: str, name: str, image: str, state: str = "started",
                                    ports: Optional[List[str]] = None, env: Optional[Dict] = None,
                                    inventory: Optional[str] = None, become: bool = True) -> Dict:
        args = f"name={name} image={image} state={state}"
        if ports: args += f" ports={json.dumps(ports)}"
        if env: args += f" env={json.dumps(env)}"
        return self.run_ad_hoc(module="community.docker.docker_container", args=args, hosts=hosts, inventory=inventory, become=become)

    def git_operations(self, hosts: str, repo: str, dest: str, version: str = "main",
                       force: bool = False, inventory: Optional[str] = None) -> Dict:
        args = f"repo={repo} dest={dest} version={version} force={str(force).lower()}"
        return self.run_ad_hoc(module="ansible.builtin.git", args=args, hosts=hosts, inventory=inventory)

    def template_operations(self, hosts: str, src: str, dest: str, vars: Optional[Dict] = None,
                            inventory: Optional[str] = None, become: bool = False) -> Dict:
        args = f"src={src} dest={dest}"
        if vars: args += f" vars={json.dumps(vars)}"
        return self.run_ad_hoc(module="ansible.builtin.template", args=args, hosts=hosts, inventory=inventory, become=become)

    def get_ansible_version(self) -> str:
        try:
            result = subprocess.run(["ansible", "--version"], capture_output=True, text=True)
            return result.stdout.split("\n")[0] if result.stdout else "unknown"
        except:
            return "not installed"


class Plugin(PluginBase):
    name = "ansible"
    version = "1.0.0"
    description = "Ansible automation integration - playbooks, inventory, roles, modules, tasks, variables, templates, handlers, collections, galaxy, vault, facts, callbacks, ad-hoc commands"

    def __init__(self):
        self.manager = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        inventory = kwargs.get("inventory")
        private_key = kwargs.get("private_key")
        remote_user = kwargs.get("remote_user")
        become = kwargs.get("become", False)
        self.manager = AnsibleManager(inventory_path=inventory, private_key=private_key, remote_user=remote_user, become=become)

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.manager.check_connection(), "ansible_version": self.manager.get_ansible_version()}
        elif action == "ping":
            return self.manager.ping(hosts=kwargs.get("hosts", "all"), inventory=inventory)
        elif action == "facts":
            return self.manager.gather_facts(hosts=kwargs.get("hosts", "all"), inventory=inventory)
        elif action == "run_playbook":
            return self.manager.run_playbook(kwargs.get("playbook"), extra_vars=kwargs.get("extra_vars"), inventory=inventory, limit=kwargs.get("limit"), tags=kwargs.get("tags"), check_mode=kwargs.get("check_mode", False), diff=kwargs.get("diff", False), vault_password=kwargs.get("vault_password"))
        elif action == "ad_hoc":
            return self.manager.run_ad_hoc(kwargs.get("module"), kwargs.get("args"), hosts=kwargs.get("hosts", "all"), inventory=inventory, extra_vars=kwargs.get("extra_vars"), become=kwargs.get("become"), check_mode=kwargs.get("check_mode", False))
        elif action == "inventory_hosts":
            return {"hosts": self.manager.list_inventory_hosts(inventory=inventory)}
        elif action == "inventory_groups":
            return {"groups": self.manager.list_groups(inventory=inventory)}
        elif action == "add_host":
            return self.manager.create_inventory_entry(kwargs.get("hostname"), group=kwargs.get("group", "all"), vars=kwargs.get("vars"), inventory=inventory)
        elif action == "install_role":
            return self.manager.install_role(kwargs.get("role_name"), galaxy_server=kwargs.get("galaxy_server"), force=kwargs.get("force", False))
        elif action == "install_collection":
            return self.manager.install_collection(kwargs.get("collection_name"), galaxy_server=kwargs.get("galaxy_server"), force=kwargs.get("force", False))
        elif action == "list_roles":
            return {"roles": self.manager.list_roles()}
        elif action == "list_collections":
            return {"collections": self.manager.list_collections()}
        elif action == "vault_encrypt":
            return self.manager.encrypt_vault(kwargs.get("file_path"), kwargs.get("vault_password"), output_file=kwargs.get("output_file"))
        elif action == "vault_decrypt":
            return self.manager.decrypt_vault(kwargs.get("file_path"), kwargs.get("vault_password"), output_file=kwargs.get("output_file"))
        elif action == "vault_edit":
            return self.manager.edit_vault(kwargs.get("file_path"), kwargs.get("vault_password"), kwargs.get("new_content"))
        elif action == "vault_view":
            return self.manager.view_vault(kwargs.get("file_path"), kwargs.get("vault_password"))
        elif action == "create_playbook":
            return self.manager.create_playbook(kwargs.get("name"), hosts=kwargs.get("hosts", "all"), become=kwargs.get("become", True), tasks=kwargs.get("tasks"), vars=kwargs.get("vars"), roles=kwargs.get("roles"), path=kwargs.get("path"))
        elif action == "shell":
            return self.manager.shell_command(kwargs.get("hosts"), kwargs.get("command"), inventory=inventory, become=kwargs.get("become", False))
        elif action == "copy":
            return self.manager.copy_file(kwargs.get("hosts"), kwargs.get("src"), kwargs.get("dest"), inventory=inventory, become=kwargs.get("become", False))
        elif action == "file":
            return self.manager.file_operations(kwargs.get("hosts"), kwargs.get("path"), state=kwargs.get("state", "directory"), mode=kwargs.get("mode"), owner=kwargs.get("owner"), group=kwargs.get("group"), inventory=inventory, become=kwargs.get("become", False))
        elif action == "package":
            return self.manager.package_manager(kwargs.get("hosts"), kwargs.get("name"), state=kwargs.get("state", "present"), package_type=kwargs.get("package_type", "apt"), inventory=inventory, become=kwargs.get("become", True))
        elif action == "service":
            return self.manager.service_management(kwargs.get("hosts"), kwargs.get("name"), state=kwargs.get("state", "started"), enabled=kwargs.get("enabled"), inventory=inventory, become=kwargs.get("become", True))
        elif action == "git":
            return self.manager.git_operations(kwargs.get("hosts"), kwargs.get("repo"), kwargs.get("dest"), version=kwargs.get("version", "main"), force=kwargs.get("force", False), inventory=inventory)
        return {"error": f"Unknown action: {action}"}