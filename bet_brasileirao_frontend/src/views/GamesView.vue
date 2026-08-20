<script setup>
import { onMounted } from 'vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import MatchFilters from '@/components/games/MatchFilters.vue'
import MatchCard from '@/components/games/MatchCard.vue'
import BetSlip from '@/components/betslip/BetSlip.vue'
import { useGamesStore } from '@/stores/games'

const games = useGamesStore()

onMounted(() => {
  games.fetchGames()
})
</script>

<template>
  <DefaultLayout>
    <div class="flex flex-col md:flex-row w-full max-w-7xl mx-auto min-h-screen relative">
      <!-- Conteúdo principal -->
      <main class="flex-1 w-full px-margin-mobile md:px-margin-desktop py-lg pb-32 md:pb-lg md:mr-80">
        <!-- Banner contextual -->
        <div
          class="w-full bg-surface-container-high rounded-xl p-lg mb-xl relative overflow-hidden flex items-center justify-between border border-outline-variant/30"
        >
          <div class="relative z-10">
            <h2 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-sm">
              Brasileirão Série A
            </h2>
            <p class="font-body-md text-body-md text-on-surface-variant">Acompanhe os jogos e registre seu palpite</p>
          </div>
          <div class="relative z-10 hidden md:block">
            <span class="material-symbols-outlined text-secondary" style="font-size: 64px; font-variation-settings: 'FILL' 1">
              emoji_events
            </span>
          </div>
          <div class="absolute -right-20 -top-20 w-64 h-64 bg-primary/10 rounded-full blur-3xl pointer-events-none"></div>
          <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-secondary/10 rounded-full blur-3xl pointer-events-none"></div>
        </div>

        <MatchFilters :active="games.activeFilter" @update:active="games.setFilter" />

        <p v-if="games.error" class="text-error font-body-md text-body-md mb-md">{{ games.error }}</p>
        <p v-else-if="games.loading" class="text-on-surface-variant font-body-md text-body-md mb-md">
          Carregando jogos...
        </p>

        <p
          v-if="!games.loading && !games.error && games.filteredGames.length === 0"
          class="text-on-surface-variant font-body-md text-body-md mb-md"
        >
          Nenhum jogo nesta categoria no momento.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-lg">
          <MatchCard v-for="game in games.filteredGames" :key="game.id" :game="game" />
        </div>
      </main>

      <BetSlip />
    </div>
  </DefaultLayout>
</template>
