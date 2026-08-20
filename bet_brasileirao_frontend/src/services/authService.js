import api from './api'

/**
 * Espelha o auth_controller/user_controller do backend FastAPI.
 * LoginRequest aceita e-mail OU login no mesmo campo "login".
 * UserCreate valida CPF (11 dígitos) e idade mínima de 18 anos; o formulário
 * de cadastro no front deve refletir essas mesmas regras.
 */
export const authService = {
  async login({ login, password }) {
    const { data } = await api.post('/auth/login', { login, password })
    return data // { access_token, token_type, user }
  },

  async register(payload) {
    // payload: { name, email, birthDate, login, cpf, password }
    const { data } = await api.post('/users/', payload)
    return data
  },

  async me() {
    const { data } = await api.get('/users/me')
    return data
  },

  async updateProfile(userId, payload) {
    const { data } = await api.put(`/users/${userId}`, payload)
    return data
  },

  logout() {
    localStorage.removeItem('apostacopa_token')
    localStorage.removeItem('apostacopa_user')
  }
}
