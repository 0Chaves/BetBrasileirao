import axios from 'axios'

// Em desenvolvimento o vite.config.js faz proxy de /api -> http://localhost:8000
// Em produção, defina VITE_API_URL no .env apontando para a API FastAPI.
// const baseURL = import.meta.env.VITE_API_URL || '/api'
const baseURL = 'http://localhost:8000'

const api = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Injeta o token (se existir) em toda requisição autenticada
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('apostacopa_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Trata 401 de forma centralizada (token expirado / inválido)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('apostacopa_token')
      localStorage.removeItem('apostacopa_user')
    }
    return Promise.reject(error)
  }
)

export default api
