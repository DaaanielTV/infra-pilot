import React from 'react';

export const ThemeToggle: React.FC = () => {
  const toggle = () => {
    const root = document.documentElement;
    if (root.classList.contains('dark')) {
      root.classList.remove('dark');
    } else {
      root.classList.add('dark');
    }
  };

  return (
    <button onClick={toggle} aria-label="Toggle theme" className="px-3 py-2 rounded bg-brand-primary text-white shadow-sm hover:bg-brand-primary-dark" title="Toggle theme">
      Theme
    </button>
  );
};

export default ThemeToggle;
