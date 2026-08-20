<script setup>
import { onMounted } from 'vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import StandingsLegend from '@/components/standings/StandingsLegend.vue'
import StandingsTable from '@/components/standings/StandingsTable.vue'
import { useStandingsStore } from '@/stores/standings'

const standings = useStandingsStore()

onMounted(() => {
  standings.fetchStandings()
})
</script>

<template>
  <DefaultLayout>
    <main class="flex-1 w-full px-margin-mobile md:px-margin-desktop py-lg pb-32 max-w-7xl mx-auto">
      <div class="mb-lg flex flex-col gap-2">
        <div class="flex items-center gap-2 text-primary">
          <span class="material-symbols-outlined text-[24px]">trophy</span>
          <span class="text-label-sm font-label-sm uppercase tracking-widest">Temporada Atual</span>
        </div>
        <h2 class="text-display-lg-mobile md:text-display-lg font-display-lg text-on-surface tracking-tight">
          Tabela Brasileirão Série A
        </h2>
        <p class="text-body-md font-body-md text-on-surface-variant max-w-2xl">
          Acompanhe a classificação atualizada em tempo real. Posições garantem vagas em competições continentais ou
          determinam o rebaixamento.
        </p>
      </div>

      <div class="bg-surface-container-low border border-surface-container rounded-xl overflow-hidden shadow-2xl shadow-black/50">
        <StandingsLegend />

        <p v-if="standings.loading" class="p-md text-on-surface-variant font-body-md text-body-md">
          Carregando classificação...
        </p>
        <StandingsTable v-else :rows="standings.rows" />
      </div>
    </main>
  </DefaultLayout>
</template>
