<script setup>
import { reactive, ref, onMounted } from 'vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()

const form = reactive({ password: '', confirmPassword: '' })
const submitting = ref(false)
const localError = ref(null)
const success = ref(false)

onMounted(() => {
  auth.refreshUser()
})

async function handleSubmit() {
  localError.value = null
  success.value = false
  if (form.password !== form.confirmPassword) {
    localError.value = 'As senhas não coincidem.'
    return
  }

  submitting.value = true
  try {
    await auth.updatePassword(form.password)
    success.value = true
    form.password = ''
    form.confirmPassword = ''
  } catch {
    // erro já fica disponível em auth.error
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <DefaultLayout>
    <main class="flex-1 w-full px-margin-mobile md:px-margin-desktop py-lg pb-32 max-w-3xl mx-auto flex flex-col gap-lg">
      <h2 class="text-display-lg-mobile md:text-display-lg font-display-lg text-on-surface tracking-tight">
        Meu Perfil
      </h2>

      <section
        v-if="auth.user"
        class="bg-surface-container-low border border-surface-container rounded-xl p-lg grid grid-cols-1 md:grid-cols-2 gap-md"
      >
        <div>
          <p class="font-label-sm text-label-sm text-on-surface-variant uppercase">Nome</p>
          <p class="font-body-lg text-body-lg text-on-surface">{{ auth.user.name }}</p>
        </div>
        <div>
          <p class="font-label-sm text-label-sm text-on-surface-variant uppercase">Usuário</p>
          <p class="font-body-lg text-body-lg text-on-surface">{{ auth.user.login }}</p>
        </div>
        <div>
          <p class="font-label-sm text-label-sm text-on-surface-variant uppercase">E-mail</p>
          <p class="font-body-lg text-body-lg text-on-surface">{{ auth.user.email }}</p>
        </div>
        <div>
          <p class="font-label-sm text-label-sm text-on-surface-variant uppercase">Nascimento</p>
          <p class="font-body-lg text-body-lg text-on-surface">{{ auth.user.birthDate }}</p>
        </div>
        <div>
          <p class="font-label-sm text-label-sm text-on-surface-variant uppercase">Saldo de pontos</p>
          <p class="font-odds-display text-odds-display text-primary">{{ auth.user.points }}</p>
        </div>
        <div>
          <p class="font-label-sm text-label-sm text-on-surface-variant uppercase">Maior saldo já alcançado</p>
          <p class="font-body-lg text-body-lg text-on-surface">{{ auth.user.max_points }}</p>
        </div>
        <div>
          <p class="font-label-sm text-label-sm text-on-surface-variant uppercase">Palpites certeiros</p>
          <p class="font-body-lg text-body-lg text-on-surface">{{ auth.user.right_calls }}</p>
        </div>
      </section>

      <section class="bg-surface-container-low border border-surface-container rounded-xl p-lg">
        <h3 class="font-headline-md text-headline-md text-on-surface mb-md">Alterar senha</h3>
        <form class="flex flex-col gap-md max-w-sm" @submit.prevent="handleSubmit">
          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Nova senha</label>
            <input
              v-model="form.password"
              type="password"
              required
              class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
            />
          </div>
          <div class="flex flex-col gap-xs">
            <label class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Confirmar nova senha</label>
            <input
              v-model="form.confirmPassword"
              type="password"
              required
              class="w-full bg-surface-container-high border border-outline-variant rounded-lg py-3 px-4 text-on-surface focus:outline-none focus:border-primary transition-all font-body-md text-body-md"
            />
          </div>

          <p v-if="localError" class="text-error text-label-sm font-label-sm">{{ localError }}</p>
          <p v-if="auth.error" class="text-error text-label-sm font-label-sm">{{ auth.error }}</p>
          <p v-if="success" class="text-primary text-label-sm font-label-sm">Senha alterada com sucesso.</p>

          <button
            type="submit"
            :disabled="submitting"
            class="bg-primary hover:bg-primary-fixed-dim text-on-primary font-bold py-3 rounded-xl transition-all active:scale-95 disabled:opacity-60"
          >
            {{ submitting ? 'Salvando...' : 'Salvar nova senha' }}
          </button>
        </form>
      </section>
    </main>
  </DefaultLayout>
</template>
