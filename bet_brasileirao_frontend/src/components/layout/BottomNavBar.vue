<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

const items = [
  { to: '/', label: 'Jogos', icon: 'sports_soccer' },
  { to: '/classificacao', label: 'Tabela', icon: 'leaderboard' },
  { to: '/minhas-apostas', label: 'Apostas', icon: 'receipt_long' },
  { to: '/perfil', label: 'Perfil', icon: 'person' }
]
</script>

<template>
  <nav
    class="bg-surface-container-highest fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 py-2 md:hidden border-t border-outline-variant shadow-lg"
  >
    <router-link
      v-for="item in items"
      :key="item.to"
      :to="item.to"
      class="flex flex-col items-center justify-center rounded-full p-2 scale-90 duration-200 w-16"
      :class="
        route.path === item.to
          ? 'bg-primary-container text-on-primary-container'
          : 'text-on-surface-variant hover:bg-surface-variant'
      "
    >
      <span
        class="material-symbols-outlined"
        :style="route.path === item.to ? { fontVariationSettings: '\'FILL\' 1' } : {}"
        >{{ item.icon }}</span
      >
      <span class="mt-1 text-[10px]">{{ item.label }}</span>
    </router-link>
  </nav>
</template>
