<script setup>
import { onMounted } from 'vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import { useRankingStore } from '@/stores/ranking'

const ranking = useRankingStore()

onMounted(() => {
  ranking.fetchRanking('points')
})
</script>

<template>
  <DefaultLayout>
    <main class="flex-1 w-full px-margin-mobile md:px-margin-desktop py-lg pb-32 max-w-3xl mx-auto flex flex-col gap-lg">
      <h2 class="text-display-lg-mobile md:text-display-lg font-display-lg text-on-surface tracking-tight">
        Ranking de Apostadores
      </h2>

      <div class="flex gap-md">
        <button
          type="button"
          class="px-lg py-sm rounded-full font-label-sm text-label-sm transition-colors"
          :class="
            ranking.orderBy === 'points'
              ? 'bg-primary-container text-on-primary-container'
              : 'bg-surface-variant text-on-surface-variant hover:bg-surface-container-high'
          "
          @click="ranking.fetchRanking('points')"
        >
          Por saldo de pontos
        </button>
        <button
          type="button"
          class="px-lg py-sm rounded-full font-label-sm text-label-sm transition-colors"
          :class="
            ranking.orderBy === 'right_calls'
              ? 'bg-primary-container text-on-primary-container'
              : 'bg-surface-variant text-on-surface-variant hover:bg-surface-container-high'
          "
          @click="ranking.fetchRanking('right_calls')"
        >
          Por acertos
        </button>
      </div>

      <p v-if="ranking.loading" class="text-on-surface-variant font-body-md text-body-md">Carregando...</p>
      <p v-else-if="ranking.error" class="text-error font-body-md text-body-md">{{ ranking.error }}</p>

      <div v-else class="bg-surface-container-low border border-surface-container rounded-xl overflow-hidden">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="text-label-sm font-label-sm text-on-surface-variant uppercase border-b border-surface-container bg-surface-container/50">
              <th class="py-3 px-4 w-12 font-medium">#</th>
              <th class="py-3 px-4 font-medium">Apostador</th>
              <th class="py-3 px-4 font-medium text-center">Saldo</th>
              <th class="py-3 px-4 font-medium text-center">Maior saldo</th>
              <th class="py-3 px-4 font-medium text-center">Acertos</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(row, index) in ranking.rows"
              :key="row.name + index"
              class="hover:bg-surface-variant/50 transition-colors border-b border-surface-container/50 last:border-b-0"
            >
              <td class="py-3 px-4 text-on-surface-variant">{{ index + 1 }}</td>
              <td class="py-3 px-4 text-on-surface">{{ row.name }}</td>
              <td class="py-3 px-4 text-center font-odds-display text-odds-display text-primary">{{ row.points }}</td>
              <td class="py-3 px-4 text-center text-on-surface-variant">{{ row.max_points }}</td>
              <td class="py-3 px-4 text-center text-on-surface-variant">{{ row.right_calls }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </DefaultLayout>
</template>
