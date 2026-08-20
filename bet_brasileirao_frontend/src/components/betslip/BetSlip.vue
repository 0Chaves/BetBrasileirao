<script setup>
import { computed } from 'vue'
import { useBetSlipStore } from '@/stores/betslip'

const betSlip = useBetSlipStore()

const formatPoints = (value) => new Intl.NumberFormat('pt-BR').format(Number(value) || 0)

const totalStakeLabel = computed(() => formatPoints(betSlip.totalStake))

async function handleSubmit() {
  try {
    await betSlip.submit()
  } catch {
    // erro já fica exposto em betSlip.error para exibição no template
  }
}
</script>

<template>
  <aside
    class="hidden md:flex flex-col bg-surface-container text-secondary font-label-sm text-label-sm fixed right-0 top-16 bottom-0 w-80 border-l border-outline-variant shadow-sm z-30"
  >
    <!-- Cabeçalho -->
    <div class="p-md border-b border-outline-variant/50">
      <h3 class="font-headline-md text-headline-md text-on-surface flex items-center justify-between">
        Bilhete de Aposta
        <span
          v-if="betSlip.count > 0"
          class="bg-error text-on-error rounded-full w-6 h-6 flex items-center justify-center text-label-sm font-bold shadow"
        >
          {{ betSlip.count }}
        </span>
      </h3>
      <p class="font-label-sm text-label-sm text-on-surface-variant mt-xs">Escolha um resultado para começar</p>
    </div>

    <!-- Últimos resultados registrados -->
    <div v-if="betSlip.lastResults.length" class="p-md border-b border-outline-variant/50 bg-surface-container-high">
      <p class="font-label-sm text-label-sm text-on-surface-variant uppercase mb-xs">Apostas registradas</p>
      <div v-for="result in betSlip.lastResults" :key="result.id" class="text-on-surface font-body-md text-body-md mb-xs">
        {{ result.teams }} — {{ result.label }}: multiplicador {{ Number(result.multiplier).toFixed(2) }}x
      </div>
    </div>

    <!-- Seleções -->
    <div class="flex-1 overflow-y-auto p-md space-y-md">
      <div
        v-if="betSlip.isEmpty"
        class="flex flex-col items-center justify-center h-full text-on-surface-variant opacity-50"
      >
        <span class="material-symbols-outlined text-[48px] mb-sm">receipt_long</span>
        <p class="text-center">Seu bilhete está vazio.</p>
      </div>

      <div
        v-for="sel in betSlip.selections"
        :key="sel.id"
        class="bg-surface rounded-lg p-sm border border-outline-variant relative group"
      >
        <button
          type="button"
          class="absolute top-sm right-sm text-on-surface-variant hover:text-error transition-colors"
          @click="betSlip.removeSelection(sel.id)"
        >
          <span class="material-symbols-outlined text-[18px]">close</span>
        </button>
        <div class="pr-lg">
          <div class="font-body-md text-body-md text-on-surface font-semibold mb-xs">{{ sel.label }}</div>
          <div class="font-label-sm text-label-sm text-on-surface-variant">{{ sel.teams }}</div>
        </div>
        <div class="mt-md flex justify-between items-center border-t border-outline-variant/30 pt-sm">
          <span class="font-label-sm text-label-sm text-on-surface-variant">Pontos</span>
          <div class="w-1/2">
            <input
              type="number"
              min="1"
              step="1"
              class="w-full bg-surface-variant text-on-surface border border-outline-variant rounded px-sm py-xs text-right font-label-sm focus:ring-1 focus:ring-secondary focus:border-secondary outline-none transition-shadow"
              :value="sel.points"
              @input="betSlip.updatePoints(sel.id, Number($event.target.value) || 0)"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Rodapé: total e CTA -->
    <div v-if="!betSlip.isEmpty" class="p-md bg-surface-container-high border-t border-outline-variant">
      <p v-if="betSlip.error" class="text-error text-label-sm font-label-sm mb-sm">{{ betSlip.error }}</p>
      <div class="flex justify-between items-center mb-md">
        <span class="font-body-md text-body-md text-on-surface-variant">Total em pontos</span>
        <span class="font-body-md text-body-md text-on-surface font-bold">{{ totalStakeLabel }}</span>
      </div>
      <button
        type="button"
        :disabled="betSlip.submitting"
        class="w-full bg-primary hover:bg-primary-fixed-dim text-on-primary-fixed font-body-md text-body-md font-bold py-md rounded-lg shadow-md hover:shadow-lg transition-all duration-200 transform active:scale-[0.98] disabled:opacity-60"
        @click="handleSubmit"
      >
        {{ betSlip.submitting ? 'Enviando...' : 'Finalizar Aposta' }}
      </button>
    </div>
  </aside>
</template>
