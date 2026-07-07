# FAQ

**What is Infra Pilot?**
A modular orchestration framework for IaC, containers, and multi-cloud — via CLI, web, or Discord.

**Why not just Terraform/Pulumi?**
Infra Pilot builds on top of them with a unified API, AI features, Discord control, green tracking, and a dashboard.

**Connection failed on `ipilot health`?**
Check `docker compose ps`. Set correct URL: `ipilot config set api_url http://localhost:3001`.

**Can I run single services?**
Yes. `docker compose up -d postgres redis`.

**How to change output format?**
`ipilot config set output_format json`

**200+ commands — how to keep track?**
`ipilot --help` for top-level, `ipilot <command> --help` for subcommands.

**Can I work offline?**
Yes. Use a local LLM (Ollama, LM Studio) — set `AI_API_ENDPOINT` in `.env`.

---

*[Issues](https://github.com/drosemann/infra-pilot/issues) · [Discussions](https://github.com/drosemann/infra-pilot/discussions)*
