import api from './api'

/**
 * Não existe endpoint /standings no backend: a classificação é derivada dos
 * próprios times (Team.position/playedGames/won/lost/draw/points, sincronizados
 * pelo script api/control/api_externa.py a partir da api.football-data.org).
 */
export const standingsService = {
  async list(params = {}) {
    const { data } = await api.get('/teams/', { params })
    return data
  }
}
