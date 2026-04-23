const { } = require('tailwindcss/defaultTheme');

module.exports = {
  darkMode: 'class',
  mode: 'jit',
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          primary: '#6C5CE7', // Cosmic Infra primary
          'primary-dark': '#5A46CD', // hover/active variant
          secondary: '#EC4899', // Cosmic Infra secondary
          accent: '#22D3EE', // Cosmic Infra accent
        },
      },
    },
  },
  variants: {
    extend: {},
  },
};
