<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()

const links = [
  { to: '/', label: 'Jogos' },
  { to: '/classificacao', label: 'Classificação' },
  { to: '/ranking', label: 'Ranking' },
  { to: '/minhas-apostas', label: 'Minhas Apostas' },
  { to: '/perfil', label: 'Perfil' }
]

const balanceLabel = computed(() =>
  new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(auth.balance)
)

function goToLogin() {
  router.push({ name: 'login' })
}

function logout() {
  auth.logout()
  router.push({ name: 'login' })
}
</script>

<template>
  <header
    class="bg-surface-container-low border-b border-outline-variant fixed w-full top-0 z-40 flex justify-between items-center px-margin-mobile md:px-margin-desktop max-w-7xl mx-auto h-16 left-0 right-0"
  >
    <div class="flex items-center gap-lg">
      <h1 class="font-headline-md text-headline-md font-bold text-primary tracking-tight">
        Bet Brasileirão
      </h1>
      <nav class="hidden md:flex items-center gap-lg ml-xl">
        <router-link
          v-for="link in links"
          :key="link.to"
          :to="link.to"
          class="pb-1 transition-colors scale-95 duration-150"
          :class="
            route.path === link.to
              ? 'text-primary border-b-2 border-primary'
              : 'text-on-surface-variant hover:text-primary'
          "
        >
          {{ link.label }}
        </router-link>
      </nav>
    </div>
    <div class="flex items-center gap-md">
      <span
        v-if="auth.isAuthenticated"
        class="font-label-sm text-label-sm bg-surface-variant px-md py-sm rounded-full text-secondary"
      >
        Saldo: {{ balanceLabel }}
      </span>
      <button
        v-if="auth.isAuthenticated"
        class="hidden md:inline-flex text-on-surface-variant hover:text-primary transition-colors"
        @click="logout"
      >
        <span class="material-symbols-outlined">logout</span>
      </button>
      <button
        v-else
        class="bg-primary-container text-on-primary-container px-md py-1.5 rounded-full font-label-sm text-label-sm uppercase font-bold hover:opacity-80 transition-opacity"
        @click="goToLogin"
      >
        Entrar
      </button>
      <button class="md:hidden text-on-surface hover:text-primary transition-colors">
        <span class="material-symbols-outlined">menu</span>
      </button>
    </div>
  </header>
  <!-- Espaçador para compensar o header fixo -->
  <div class="h-16" />
</template>
