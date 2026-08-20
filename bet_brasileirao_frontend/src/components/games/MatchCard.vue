<script setup>
import { computed } from 'vue'
import LiveBadge from '@/components/ui/LiveBadge.vue'
import PredictionChip from '@/components/games/PredictionChip.vue'
import { useBetSlipStore } from '@/stores/betslip'
import { gamePhase, PREDICTIONS } from '@/utils/gameStatus'

const props = defineProps({
  game: { type: Object, required: true }
  /**
   * Formato GameResponse do backend:
   * {
   *   id, status, date, home_team_goals, away_team_goals, winner_str,
   *   home_team: { name, flag, ... }, away_team: { name, flag, ... }
   * }
   */
})

const betSlip = useBetSlipStore()

const phase = computed(() => gamePhase(props.game.status))
const isLive = computed(() => phase.value === 'live')
const isFinished = computed(() => phase.value === 'finished')

const kickoffLabel = computed(() =>
  new Date(props.game.date).toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit' })
)

const teams = computed(() => `${props.game.home_team.name} vs ${props.game.away_team.name}`)

function isSelected(predictionKey) {
  const current = betSlip.selections.find((s) => s.gameId === props.game.id)
  return current?.prediction === predictionKey
}

function selectPrediction(prediction) {
  betSlip.addSelection({
    gameId: props.game.id,
    prediction: prediction.key,
    label: prediction.label,
    teams: teams.value
  })
}
</script>

<template>
  <article
    class="bg-surface-container rounded-xl overflow-hidden border shadow-sm transition-transform hover:translate-y-[-2px] duration-200"
    :class="[isLive ? 'border-primary/30' : 'border-outline-variant', { 'opacity-80': isFinished }]"
  >
    <!-- Cabeçalho -->
    <div
      class="px-md py-sm border-b border-outline-variant flex justify-between items-center bg-surface-container-high"
    >
      <LiveBadge v-if="isLive" />
      <span v-else-if="isFinished" class="font-label-sm text-label-sm text-on-surface-variant">
        Encerrado
      </span>
      <span v-else class="font-label-sm text-label-sm text-on-surface-variant">
        {{ kickoffLabel }}
      </span>
      <span class="font-label-sm text-label-sm text-on-surface-variant">{{ game.status }}</span>
    </div>

    <!-- Times e placar -->
    <div class="p-lg flex justify-between items-center">
      <div class="flex flex-col items-center gap-sm w-1/3">
        <img
          v-if="game.home_team.flag"
          :src="game.home_team.flag"
          :alt="game.home_team.name"
          class="w-12 h-12 rounded-full object-cover border-2 border-surface shadow-sm"
          :class="{ 'grayscale-[20%]': isFinished }"
        />
        <div v-else class="w-12 h-12 rounded-full bg-surface-bright" />
        <span class="font-body-lg text-body-lg text-on-surface text-center">{{ game.home_team.name }}</span>
      </div>

      <div class="flex flex-col items-center justify-center w-1/3">
        <div v-if="isLive || isFinished" class="flex items-center gap-md">
          <span
            class="font-display-lg-mobile text-display-lg-mobile font-bold"
            :class="isLive ? 'text-secondary' : 'text-on-surface'"
          >
            {{ game.home_team_goals ?? 0 }}
          </span>
          <span class="font-body-md text-body-md text-on-surface-variant">-</span>
          <span class="font-display-lg-mobile text-display-lg-mobile text-on-surface font-bold">
            {{ game.away_team_goals ?? 0 }}
          </span>
        </div>
        <span
          v-else
          class="font-body-md text-body-md text-on-surface-variant text-center border border-outline-variant rounded px-sm py-xs"
        >
          vs
        </span>
      </div>

      <div class="flex flex-col items-center gap-sm w-1/3">
        <img
          v-if="game.away_team.flag"
          :src="game.away_team.flag"
          :alt="game.away_team.name"
          class="w-12 h-12 rounded-full object-cover border-2 border-surface shadow-sm"
          :class="{ 'grayscale-[20%]': isFinished }"
        />
        <div v-else class="w-12 h-12 rounded-full bg-surface-bright" />
        <span class="font-body-lg text-body-lg text-on-surface text-center">{{ game.away_team.name }}</span>
      </div>
    </div>

    <!-- Rodapé: palpite (HOME_TEAM / DRAW / AWAY_TEAM) -->
    <div v-if="!isFinished" class="p-md bg-surface border-t border-outline-variant/50">
      <div class="grid grid-cols-3 gap-sm">
        <PredictionChip
          v-for="prediction in PREDICTIONS"
          :key="prediction.key"
          :label="prediction.label"
          :selected="isSelected(prediction.key)"
          @select="selectPrediction(prediction)"
        />
      </div>
      <p class="mt-sm text-center font-label-sm text-label-sm text-on-surface-variant">
        O multiplicador só é conhecido depois de registrar a aposta.
      </p>
    </div>
    <div v-else class="p-sm bg-surface text-center border-t border-outline-variant/50">
      <span class="font-label-sm text-label-sm text-on-surface-variant flex items-center justify-center gap-xs">
        <span class="material-symbols-outlined text-[16px]">sports_score</span>
        Resultado: {{ game.winner_str === 'DRAW' ? 'Empate' : game.winner_str ? `Vitória (${game.winner_str})` : '—' }}
      </span>
    </div>
  </article>
</template>
