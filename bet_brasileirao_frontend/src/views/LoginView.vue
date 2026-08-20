<script setup>
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import AuthLayout from '@/layouts/AuthLayout.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()

const form = reactive({
  login: '',
  password: ''
})
const showPassword = ref(false)
const submitting = ref(false)

async function handleSubmit() {
  submitting.value = true
  try {
    await auth.login({ login: form.login, password: form.password })
    router.push(route.query.redirect || { name: 'games' })
  } catch {
    // erro já fica disponível em auth.error para exibição no template
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <AuthLayout>
    <!-- TopNavBar -->
    <header class="bg-surface-container-low border-b border-outline-variant z-50 sticky top-0">
      <div class="flex justify-between items-center w-full px-margin-mobile md:px-margin-desktop max-w-7xl mx-auto h-16">
        <div class="flex items-center gap-sm">
          <span
            class="material-symbols-outlined text-primary font-headline-md text-headline-md"
            style="font-variation-settings: 'FILL' 1"
          >
            sports_soccer
          </span>
          <h1 class="font-headline-md text-headline-md font-bold text-primary">Bet Brasileirão</h1>
        </div>
      </div>
    </header>

    <!-- Conteúdo principal -->
    <main class="flex-grow flex items-center justify-center relative overflow-hidden px-margin-mobile py-xl">
      <div
        class="z-10 w-full max-w-md glass-card rounded-xl p-lg shadow-2xl flex flex-col gap-lg"
      >
        <div class="text-center flex flex-col gap-xs">
          <div class="w-16 h-16 bg-primary-container rounded-full flex items-center justify-center mx-auto mb-sm">
            <span
              class="material-symbols-outlined text-on-primary-container text-[32px]"
              style="font-variation-settings: 'FILL' 1"
            >
              stadium
            </span>
          </div>
          <h2 class="font-headline-md text-headline-md text-on-surface font-bold">Bem-vindo de volta</h2>
          <p class="font-body-md text-body-md text-on-surface-variant">Acesse sua conta para apostar no Brasileirão</p>
        </div>

        <form class="flex flex-col gap-md" @submit.prevent="handleSubmit">
          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">
              E-mail ou Usuário
            </label>
            <div class="relative">
              <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline text-md">
                person
              </span>
              <input
                v-model="form.login"
                type="text"
                required
                placeholder="seu@email.com ou usuário"
                class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 pl-10 pr-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
              />
            </div>
          </div>

          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">
              Senha
            </label>
            <div class="relative">
              <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline text-md">
                lock
              </span>
              <input
                v-model="form.password"
                :type="showPassword ? 'text' : 'password'"
                required
                placeholder="••••••••"
                class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 pl-10 pr-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
              />
              <button
                type="button"
                class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-outline text-md hover:text-on-surface transition-colors"
                @click="showPassword = !showPassword"
              >
                {{ showPassword ? 'visibility_off' : 'visibility' }}
              </button>
            </div>
          </div>

          <p v-if="route.query.registered" class="text-primary text-label-sm font-label-sm">
            Cadastro concluído! Faça login para continuar.
          </p>
          <p v-if="auth.error" class="text-error text-label-sm font-label-sm">{{ auth.error }}</p>

          <button
            type="submit"
            :disabled="submitting"
            class="w-full bg-primary hover:bg-primary-fixed-dim text-on-primary font-bold py-4 rounded-xl transition-all active:scale-95 flex items-center justify-center gap-sm mt-sm shadow-lg shadow-primary/20 disabled:opacity-60"
          >
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1">login</span>
            {{ submitting ? 'Entrando...' : 'Entrar' }}
          </button>
        </form>

        <p class="text-center font-body-md text-body-md text-on-surface-variant mt-sm">
          Não tem uma conta?
          <router-link
            :to="{ name: 'register' }"
            class="text-primary font-bold hover:underline decoration-primary/40 underline-offset-4"
          >
            Cadastre-se
          </router-link>
        </p>
      </div>
    </main>
  </AuthLayout>
</template>
