<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import AuthLayout from '@/layouts/AuthLayout.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()

const form = reactive({
  name: '',
  email: '',
  login: '',
  birthDate: '',
  cpf: '',
  password: '',
  confirmPassword: ''
})
const submitting = ref(false)
const localError = ref(null)

async function handleSubmit() {
  localError.value = null
  if (form.password !== form.confirmPassword) {
    localError.value = 'As senhas não coincidem.'
    return
  }

  submitting.value = true
  try {
    await auth.register({
      name: form.name,
      email: form.email,
      login: form.login,
      birthDate: form.birthDate,
      cpf: form.cpf,
      password: form.password
    })
    router.push({ name: 'login', query: { registered: '1' } })
  } catch {
    // erro já fica disponível em auth.error para exibição no template
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <AuthLayout>
    <header class="bg-surface-container-low border-b border-outline-variant z-50 sticky top-0">
      <div class="flex justify-between items-center w-full px-margin-mobile md:px-margin-desktop max-w-7xl mx-auto h-16">
        <div class="flex items-center gap-sm">
          <span
            class="material-symbols-outlined text-primary font-headline-md text-headline-md"
            style="font-variation-settings: 'FILL' 1"
          >
            sports_soccer
          </span>
          <h1 class="font-headline-md text-headline-md font-bold text-primary">Aposta Copa</h1>
        </div>
      </div>
    </header>

    <main class="flex-grow flex items-center justify-center relative overflow-hidden px-margin-mobile py-xl">
      <div class="z-10 w-full max-w-md glass-card rounded-xl p-lg shadow-2xl flex flex-col gap-lg">
        <div class="text-center flex flex-col gap-xs">
          <h2 class="font-headline-md text-headline-md text-on-surface font-bold">Criar conta</h2>
          <p class="font-body-md text-body-md text-on-surface-variant">
            É preciso ter 18 anos ou mais para se cadastrar
          </p>
        </div>

        <form class="flex flex-col gap-md" @submit.prevent="handleSubmit">
          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Nome</label>
            <input
              v-model="form.name"
              type="text"
              required
              class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
            />
          </div>

          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">E-mail</label>
            <input
              v-model="form.email"
              type="email"
              required
              class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
            />
          </div>

          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Usuário</label>
            <input
              v-model="form.login"
              type="text"
              required
              class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
            />
          </div>

          <div class="grid grid-cols-2 gap-md">
            <div class="flex flex-col gap-xs">
              <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Nascimento</label>
              <input
                v-model="form.birthDate"
                type="date"
                required
                class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
              />
            </div>
            <div class="flex flex-col gap-xs">
              <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">CPF</label>
              <input
                v-model="form.cpf"
                type="text"
                required
                placeholder="somente números"
                class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
              />
            </div>
          </div>

          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Senha</label>
            <input
              v-model="form.password"
              type="password"
              required
              placeholder="mín. 8 caracteres, maiúscula, minúscula, número e símbolo"
              class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
            />
          </div>

          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Confirmar senha</label>
            <input
              v-model="form.confirmPassword"
              type="password"
              required
              class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
            />
          </div>

          <p v-if="localError" class="text-error text-label-sm font-label-sm">{{ localError }}</p>
          <p v-if="auth.error" class="text-error text-label-sm font-label-sm">{{ auth.error }}</p>

          <button
            type="submit"
            :disabled="submitting"
            class="w-full bg-primary hover:bg-primary-fixed-dim text-on-primary font-bold py-4 rounded-xl transition-all active:scale-95 flex items-center justify-center gap-sm mt-sm shadow-lg shadow-primary/20 disabled:opacity-60"
          >
            {{ submitting ? 'Cadastrando...' : 'Criar conta' }}
          </button>
        </form>

        <p class="text-center font-body-md text-body-md text-on-surface-variant mt-sm">
          Já tem uma conta?
          <router-link
            :to="{ name: 'login' }"
            class="text-primary font-bold hover:underline decoration-primary/40 underline-offset-4"
          >
            Entrar
          </router-link>
        </p>
      </div>
    </main>
  </AuthLayout>
</template>
