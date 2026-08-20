import api from './api'

/**
 * Rankings de apostadores (schema UserRanking: name, points, max_points, right_calls).
 */
export const rankingService = {
  async byPoints(params = {}) {
    const { data } = await api.get('/users/ranking/points', { params })
    return data
  },

  async byRightCalls(params = {}) {
    const { data } = await api.get('/users/ranking/right-calls', { params })
    return data
  }
}
