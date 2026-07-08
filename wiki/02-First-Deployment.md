# First Deployment

## 1. Set Up and Log In

```bash
ipilot config set api_url http://localhost:3001
ipilot login <your-api-key>
```

## 2. Make a Server

```bash
ipilot server create --name my-first-server --type web --memory 2048
```

## 3. Check If It's Running

```bash
ipilot server status <server-id>
```

You'll see `running` when it's ready.

## 4. Delete (Clean Up)

```bash
ipilot server delete <server-id>
```

## Via the Web Page

Open http://localhost:5173 and click **"Server erstellen"**.

---

*[CLI Reference](05-CLI-Reference)*
