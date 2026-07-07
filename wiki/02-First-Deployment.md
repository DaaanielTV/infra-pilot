# First Deployment

## 1. Configure & Login

```bash
ipilot config set api_url http://localhost:3001
ipilot login <your-api-key>
```

## 2. Create a Server

```bash
ipilot server create --name my-first-server --type web --memory 2048
```

## 3. Check Status

```bash
ipilot server status <server-id>
```

Status changes to `running` when ready.

## 4. Delete (Cleanup)

```bash
ipilot server delete <server-id>
```

## Via Dashboard

Open http://localhost:5173 and click **"Server erstellen"**.

---

*[CLI Reference](05-CLI-Reference)*
