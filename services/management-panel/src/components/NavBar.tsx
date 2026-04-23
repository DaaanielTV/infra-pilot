import React from 'react';

export const NavBar: React.FC = () => {
  const items = ["Dashboard", "Servers", "Settings"];
  return (
    <nav className="hidden md:flex justify-center gap-6 border-b bg-white/90 dark:bg-gray-900/90 px-4 py-2">
      {items.map((it) => (
        <a key={it} href="#" className="text-sm font-medium text-gray-700 hover:text-brand-primary">
          {it}
        </a>
      ))}
    </nav>
  );
};

export default NavBar;
