import api from './api'

/**
 * Endpoints do recurso Team (Controller -> Service -> Repository no backend).
 */
export const teamService = {
  async list(params = {}) {
    const { data } = await api.get('/teams/', { params })
    return data
  },

  async getById(teamId) {
    const { data } = await api.get(`/teams/${teamId}`)
    return data
  }
}
