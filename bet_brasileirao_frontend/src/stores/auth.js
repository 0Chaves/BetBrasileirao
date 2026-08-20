import { defineStore } from 'pinia'
import { authService } from '@/services/authService'
import { extractErrorMessage } from '@/utils/errors'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('apostacopa_user') || 'null'),
    token: localStorage.getItem('apostacopa_token') || null,
    loading: false,
    error: null
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
    balance: (state) => state.user?.points ?? 0
  },

  actions: {
    async login({ login, password }) {
      this.loading = true
      this.error = null
      try {
        const { access_token, user } = await authService.login({ login, password })
        this.token = access_token
        this.user = user
        localStorage.setItem('apostacopa_token', access_token)
        localStorage.setItem('apostacopa_user', JSON.stringify(user))
        return user
      } catch (err) {
        this.error = extractErrorMessage(err, 'Não foi possível entrar. Verifique suas credenciais.')
        throw err
      } finally {
        this.loading = false
      }
    },

    async register(payload) {
      this.loading = true
      this.error = null
      try {
        return await authService.register(payload)
      } catch (err) {
        this.error = extractErrorMessage(err, 'Não foi possível concluir o cadastro.')
        throw err
      } finally {
        this.loading = false
      }
    },

    async updatePassword(newPassword) {
      this.loading = true
      this.error = null
      try {
        const updated = await authService.updateProfile(this.user.id, { password: newPassword })
        this.user = updated
        localStorage.setItem('apostacopa_user', JSON.stringify(updated))
        return updated
      } catch (err) {
        this.error = extractErrorMessage(err, 'Não foi possível alterar a senha.')
        throw err
      } finally {
        this.loading = false
      }
    },

    /** Rebusca o usuário logado (ex: após uma aposta, para refletir o saldo real do backend) */
    async refreshUser() {
      try {
        const user = await authService.me()
        this.user = user
        localStorage.setItem('apostacopa_user', JSON.stringify(user))
      } catch {
        // mantém o estado anterior se a rebusca falhar
      }
    },

    logout() {
      authService.logout()
      this.user = null
      this.token = null
    }
  }
})
