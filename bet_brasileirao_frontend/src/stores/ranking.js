import { defineStore } from 'pinia'
import { rankingService } from '@/services/rankingService'
import { extractErrorMessage } from '@/utils/errors'

export const useRankingStore = defineStore('ranking', {
  state: () => ({
    rows: [],
    orderBy: 'points', // 'points' | 'right_calls'
    loading: false,
    error: null
  }),

  actions: {
    async fetchRanking(orderBy = this.orderBy) {
      this.orderBy = orderBy
      this.loading = true
      this.error = null
      try {
        this.rows =
          orderBy === 'right_calls'
            ? await rankingService.byRightCalls({ limit: 50 })
            : await rankingService.byPoints({ limit: 50 })
      } catch (err) {
        this.error = extractErrorMessage(err, 'Não foi possível carregar o ranking.')
        this.rows = []
      } finally {
        this.loading = false
      }
    }
  }
})
