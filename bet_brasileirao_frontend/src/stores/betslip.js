import { defineStore } from 'pinia'
import { betService } from '@/services/betService'
import { extractErrorMessage } from '@/utils/errors'
import { useAuthStore } from './auth'

/**
 * Bilhete de apostas do usuário. Diferente de um bilhete combinado tradicional,
 * o backend processa cada seleção como uma aposta independente (POST /bets/
 * com { points, prediction, game_id }) e só calcula o multiplicador no momento
 * da criação — por isso não há "odds" para mostrar antes de apostar, só depois.
 */
export const useBetSlipStore = defineStore('betslip', {
  state: () => ({
    selections: [],
    submitting: false,
    error: null,
    lastResults: []
  }),

  getters: {
    count: (state) => state.selections.length,
    isEmpty: (state) => state.selections.length === 0,
    totalStake: (state) => state.selections.reduce((sum, s) => sum + (Number(s.points) || 0), 0)
  },

  actions: {
    // selection: { gameId, prediction, label, teams } — uma seleção ativa por jogo
    addSelection(selection) {
      const existingIndex = this.selections.findIndex((s) => s.gameId === selection.gameId)
      const entry = { points: 10, ...selection, id: selection.gameId }
      if (existingIndex >= 0) {
        this.selections.splice(existingIndex, 1, entry)
      } else {
        this.selections.push(entry)
      }
    },

    removeSelection(id) {
      this.selections = this.selections.filter((s) => s.id !== id)
    },

    updatePoints(id, points) {
      const sel = this.selections.find((s) => s.id === id)
      if (sel) sel.points = points
    },

    clear() {
      this.selections = []
    },

    async submit() {
      this.submitting = true
      this.error = null
      const results = []
      try {
        for (const sel of [...this.selections]) {
          const bet = await betService.place({
            points: sel.points,
            prediction: sel.prediction,
            game_id: sel.gameId
          })
          results.push({ ...bet, teams: sel.teams, label: sel.label })
          this.removeSelection(sel.id)
        }
        this.lastResults = results
        await useAuthStore().refreshUser()
        return results
      } catch (err) {
        this.error = extractErrorMessage(err, 'Não foi possível finalizar a aposta.')
        throw err
      } finally {
        this.submitting = false
      }
    }
  }
})
