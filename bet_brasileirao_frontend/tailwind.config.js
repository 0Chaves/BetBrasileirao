/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        surface: '#101415',
        'surface-dim': '#101415',
        'surface-bright': '#363a3b',
        'surface-container-lowest': '#0b0f10',
        'surface-container-low': '#191c1e',
        'surface-container': '#1d2022',
        'surface-container-high': '#272a2c',
        'surface-container-highest': '#323537',
        'on-surface': '#e0e3e5',
        'on-surface-variant': '#bccbb9',
        'inverse-surface': '#e0e3e5',
        'inverse-on-surface': '#2d3133',
        outline: '#869585',
        'outline-variant': '#3d4a3d',
        'surface-tint': '#4ae176',
        primary: '#4be277',
        'on-primary': '#003915',
        'primary-container': '#22c55e',
        'on-primary-container': '#004b1e',
        'inverse-primary': '#006e2f',
        secondary: '#ffc640',
        'on-secondary': '#402d00',
        'secondary-container': '#e3aa00',
        'on-secondary-container': '#5a4100',
        tertiary: '#bfc6e0',
        'on-tertiary': '#283044',
        'tertiary-container': '#a4abc4',
        'on-tertiary-container': '#383f54',
        error: '#ffb4ab',
        'on-error': '#690005',
        'error-container': '#93000a',
        'on-error-container': '#ffdad6',
        'primary-fixed': '#6bff8f',
        'primary-fixed-dim': '#4ae176',
        'on-primary-fixed': '#002109',
        'on-primary-fixed-variant': '#005321',
        'secondary-fixed': '#ffdf9f',
        'secondary-fixed-dim': '#f9bd22',
        'on-secondary-fixed': '#261a00',
        'on-secondary-fixed-variant': '#5c4300',
        'tertiary-fixed': '#dae2fd',
        'tertiary-fixed-dim': '#bec6e0',
        'on-tertiary-fixed': '#131b2e',
        'on-tertiary-fixed-variant': '#3f465c',
        background: '#101415',
        'on-background': '#e0e3e5',
        'surface-variant': '#323537',
        'zone-libertadores': '#1e3a8a',
        'zone-pre-lib': '#3b82f6',
        'zone-sulamericana': '#eab308'
      },
      fontFamily: {
        'display-lg': ['"Archivo Narrow"', 'sans-serif'],
        'display-lg-mobile': ['"Archivo Narrow"', 'sans-serif'],
        'headline-md': ['"Archivo Narrow"', 'sans-serif'],
        'body-lg': ['Inter', 'sans-serif'],
        'body-md': ['Inter', 'sans-serif'],
        'label-sm': ['"JetBrains Mono"', 'monospace'],
        'odds-display': ['"Archivo Narrow"', 'sans-serif']
      },
      fontSize: {
        'display-lg': ['48px', { lineHeight: '56px', letterSpacing: '-0.02em', fontWeight: '700' }],
        'display-lg-mobile': ['32px', { lineHeight: '40px', fontWeight: '700' }],
        'headline-md': ['24px', { lineHeight: '32px', fontWeight: '600' }],
        'body-lg': ['18px', { lineHeight: '28px', fontWeight: '400' }],
        'body-md': ['16px', { lineHeight: '24px', fontWeight: '400' }],
        'label-sm': ['12px', { lineHeight: '16px', letterSpacing: '0.05em', fontWeight: '500' }],
        'odds-display': ['20px', { lineHeight: '24px', fontWeight: '700' }]
      },
      borderRadius: {
        sm: '0.125rem',
        DEFAULT: '0.25rem',
        md: '0.375rem',
        lg: '0.5rem',
        xl: '0.75rem',
        full: '9999px'
      },
      spacing: {
        base: '4px',
        xs: '4px',
        sm: '8px',
        md: '16px',
        lg: '24px',
        xl: '40px',
        gutter: '16px',
        'margin-mobile': '16px',
        'margin-desktop': '48px'
      }
    }
  },
  plugins: []
}
