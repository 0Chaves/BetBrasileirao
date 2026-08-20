<script setup>
import { ref, onMounted, computed } from 'vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import { betService } from '@/services/betService'
import { useGamesStore } from '@/stores/games'
import { predictionLabel } from '@/utils/gameStatus'
import { extractErrorMessage } from '@/utils/errors'

const games = useGamesStore()
const bets = ref([])
const loading = ref(false)
const error = ref(null)

const sortedBets = computed(() => [...bets.value].sort((a, b) => b.id - a.id))

function gameLabel(gameId) {
  const game = games.games.find((g) => g.id === gameId)
  return game ? `${game.home_team.name} vs ${game.away_team.name}` : `Jogo #${gameId}`
}

function statusLabel(status) {
  return status === 'finalizada' ? 'Finalizada' : 'Em andamento'
}

onMounted(async () => {
  loading.value = true
  error.value = null
  try {
    const [myBets] = await Promise.all([
      betService.listMine(),
      games.games.length ? Promise.resolve() : games.fetchGames()
    ])
    bets.value = myBets
  } catch (err) {
    error.value = extractErrorMessage(err, 'Não foi possível carregar suas apostas.')
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <DefaultLayout>
    <main class="flex-1 w-full px-margin-mobile md:px-margin-desktop py-lg pb-32 max-w-4xl mx-auto flex flex-col gap-lg">
      <h2 class="text-display-lg-mobile md:text-display-lg font-display-lg text-on-surface tracking-tight">
        Minhas Apostas
      </h2>

      <p v-if="loading" class="text-on-surface-variant font-body-md text-body-md">Carregando...</p>
      <p v-else-if="error" class="text-error font-body-md text-body-md">{{ error }}</p>
      <p v-else-if="sortedBets.length === 0" class="text-on-surface-variant font-body-md text-body-md">
        Você ainda não fez nenhuma aposta.
      </p>

      <div v-else class="flex flex-col gap-md">
        <div
          v-for="bet in sortedBets"
          :key="bet.id"
          class="bg-surface-container-low border border-surface-container rounded-xl p-md flex flex-wrap items-center justify-between gap-md"
        >
          <div>
            <p class="font-body-lg text-body-lg text-on-surface">{{ gameLabel(bet.game_id) }}</p>
            <p class="font-label-sm text-label-sm text-on-surface-variant">
              Palpite: {{ predictionLabel(bet.prediction) }}
            </p>
          </div>
          <div class="text-right">
            <p class="font-body-md text-body-md text-on-surface">{{ Number(bet.points).toFixed(2) }} pontos</p>
            <p class="font-label-sm text-label-sm text-on-surface-variant">
              Multiplicador: {{ Number(bet.multiplier).toFixed(2) }}x
            </p>
          </div>
          <span
            class="font-label-sm text-label-sm px-md py-xs rounded-full uppercase font-bold"
            :class="
              bet.status === 'finalizada'
                ? 'bg-primary-container text-on-primary-container'
                : 'bg-surface-variant text-on-surface-variant'
            "
          >
            {{ statusLabel(bet.status) }}
          </span>
        </div>
      </div>
    </main>
  </DefaultLayout>
</template>
