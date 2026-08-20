import api from './api'

/**
 * Endpoints do recurso Game (GameResponse: id, status, date, home_team_goals,
 * away_team_goals, winner_str, home_team, away_team, winner, bets).
 */
export const gameService = {
  async list(params = {}) {
    const { data } = await api.get('/games/', { params })
    return data
  },

  async getById(gameId) {
    const { data } = await api.get(`/games/${gameId}`)
    return data
  }
}
