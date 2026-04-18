import { Authenticated, Unauthenticated, useQuery, useMutation, useAction } from "convex/react";
import { api } from "../convex/_generated/api";
import { SignInForm } from "./SignInForm";
import { SignOutButton } from "./SignOutButton";
import { Toaster, toast } from "sonner";
import { useState } from "react";

export default function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <header className="sticky top-0 z-10 bg-white/80 backdrop-blur-sm p-4 flex justify-between items-center border-b">
        <h2 className="text-xl font-semibold accent-text">Game Panel</h2>
        <SignOutButton />
      </header>
      <main className="flex-1 p-8">
        <div className="max-w-6xl mx-auto">
          <Content />
        </div>
      </main>
      <Toaster />
      
      {/* Google AdSense */}
      <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=YOUR-CLIENT-ID"
        crossOrigin="anonymous"></script>
      <ins className="adsbygoogle"
        style={{ display: 'block' }}
        data-ad-client="YOUR-CLIENT-ID"
        data-ad-slot="YOUR-AD-SLOT"
        data-ad-format="auto"
        data-full-width-responsive="true"></ins>
      <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
      </script>
    </div>
  );
}

function Content() {
  const loggedInUser = useQuery(api.auth.loggedInUser);
  const config = useQuery(api.pterodactyl.getConfig);
  const servers = useQuery(api.pterodactyl.listServers);
  const saveConfig = useMutation(api.pterodactyl.saveConfig);
  const fetchServers = useAction(api.pterodactyl.fetchServers);

  const [apiKey, setApiKey] = useState("");
  const [panelUrl, setPanelUrl] = useState("");

  if (loggedInUser === undefined) {
    return (
      <div className="flex justify-center items-center">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div>
      </div>
    );
  }

  const handleSaveConfig = async () => {
    try {
      await saveConfig({ apiKey, panelUrl });
      await fetchServers();
      toast.success("Configuration saved");
    } catch (error) {
      toast.error("Failed to save configuration");
    }
  };

  const refreshServers = async () => {
    try {
      await fetchServers();
      toast.success("Servers refreshed");
    } catch (error) {
      toast.error("Failed to refresh servers");
    }
  };

  return (
    <div className="flex flex-col gap-8">
      <div className="text-center">
        <h1 className="text-5xl font-bold accent-text mb-4">Game Panel</h1>
        <Authenticated>
          <p className="text-xl text-slate-600">Welcome back, {loggedInUser?.email ?? "friend"}!</p>
        </Authenticated>
        <Unauthenticated>
          <p className="text-xl text-slate-600">Sign in to get started</p>
        </Unauthenticated>
      </div>

      <Unauthenticated>
        <SignInForm />
      </Unauthenticated>

      <Authenticated>
        {!config ? (
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-2xl font-semibold mb-4">Configure Pterodactyl</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700">Panel URL</label>
                <input
                  type="text"
                  value={panelUrl}
                  onChange={(e) => setPanelUrl(e.target.value)}
                  className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
                  placeholder="https://panel.example.com"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700">API Key</label>
                <input
                  type="password"
                  value={apiKey}
                  onChange={(e) => setApiKey(e.target.value)}
                  className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
                />
              </div>
              <button
                onClick={handleSaveConfig}
                className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
              >
                Save Configuration
              </button>
            </div>
          </div>
        ) : (
          <div className="space-y-6">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-semibold">Your Servers</h2>
              <button
                onClick={refreshServers}
                className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
              >
                Refresh Servers
              </button>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {servers?.map((server) => (
                <div key={server._id} className="bg-white p-6 rounded-lg shadow">
                  <h3 className="text-lg font-semibold">{server.name}</h3>
                  <p className="text-sm text-gray-500">ID: {server.serverId}</p>
                  <p className={`text-sm ${
                    server.status === 'running' ? 'text-green-500' : 'text-red-500'
                  }`}>
                    Status: {server.status}
                  </p>
                </div>
              ))}
            </div>
          </div>
        )}
      </Authenticated>
    </div>
  );
}
