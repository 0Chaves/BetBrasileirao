import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 3000,
    proxy: {
      // Encaminha chamadas /api/* para o backend FastAPI em desenvolvimento
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})