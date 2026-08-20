import api from './api'

/**
 * Recurso Bet. Cada aposta é uma previsão única para um jogo: points (stake),
 * prediction (HOME_TEAM | AWAY_TEAM | DRAW, mesma convenção de Game.winner_str)
 * e game_id. O multiplicador é calculado pelo backend no momento da criação
 * (BetService.place_bet) — não existe endpoint para "escolher" a odd antes.
 *
 * DELETE /bets/{id} hoje só é permitido para admin (get_current_admin_user),
 * então não expomos cancelamento aqui para o usuário comum.
 */
export const betService = {
  async place({ points, prediction, game_id }) {
    const { data } = await api.post('/bets/', { points, prediction, game_id })
    return data
  },

  async listMine() {
    const { data } = await api.get('/bets/me')
    return data
  },

  async getById(betId) {
    const { data } = await api.get(`/bets/${betId}`)
    return data
  }
}
