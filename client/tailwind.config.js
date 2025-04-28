/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        background: '#6D213C',
        text: '#F9F0DC',
        link: '#007bff',
        'header-1': '#F9F0DC',
        'header-2': '#CB769E',
        'header-3': '#F9F0DC',
        accent: '#226D5E',
        'accent-2': '#DDE1FF',
      },
      fontFamily: {
        space: ['"Space Mono"', 'monospace'],
        abril: ['"Abril Fatface"', 'serif'],
      },
    },
  },
  plugins: [],
}
