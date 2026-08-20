import { defineStore } from 'pinia'
import { gameService } from '@/services/gameService'
import { gamePhase } from '@/utils/gameStatus'
import { extractErrorMessage } from '@/utils/errors'

export const useGamesStore = defineStore('games', {
  state: () => ({
    games: [],
    activeFilter: 'upcoming',
    loading: false,
    error: null
  }),

  getters: {
    liveGames: (state) => state.games.filter((g) => gamePhase(g.status) === 'live'),
    upcomingGames: (state) => state.games.filter((g) => gamePhase(g.status) === 'upcoming'),
    finishedGames: (state) => state.games.filter((g) => gamePhase(g.status) === 'finished'),
    filteredGames: (state) => {
      if (state.activeFilter === 'live') return state.games.filter((g) => gamePhase(g.status) === 'live')
      if (state.activeFilter === 'finished') return state.games.filter((g) => gamePhase(g.status) === 'finished')
      return state.games.filter((g) => gamePhase(g.status) === 'upcoming')
    }
  },

  actions: {
    setFilter(filter) {
      this.activeFilter = filter
    },

    async fetchGames() {
      this.loading = true
      this.error = null
      try {
        this.games = await gameService.list({ limit: 400 })
      } catch (err) {
        this.error = extractErrorMessage(err, 'Não foi possível carregar os jogos.')
        this.games = []
      } finally {
        this.loading = false
      }
    }
  }
})
