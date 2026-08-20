import { defineStore } from 'pinia'
import { standingsService } from '@/services/standingsService'
import { extractErrorMessage } from '@/utils/errors'

export const useStandingsStore = defineStore('standings', {
  state: () => ({
    rows: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchStandings() {
      this.loading = true
      this.error = null
      try {
        const teams = await standingsService.list({ limit: 100 })
        this.rows = [...teams].sort((a, b) => (a.position ?? 0) - (b.position ?? 0))
      } catch (err) {
        this.error = extractErrorMessage(err, 'Não foi possível carregar a classificação.')
        this.rows = []
      } finally {
        this.loading = false
      }
    }
  }
})
