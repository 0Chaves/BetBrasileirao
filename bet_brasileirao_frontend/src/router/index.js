import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginView.vue'),
    meta: { public: true, layout: 'auth' }
  },
  {
    path: '/cadastro',
    name: 'register',
    component: () => import('@/views/RegisterView.vue'),
    meta: { public: true, layout: 'auth' }
  },
  {
    path: '/',
    name: 'games',
    component: () => import('@/views/GamesView.vue'),
    meta: { layout: 'default' }
  },
  {
    path: '/classificacao',
    name: 'standings',
    component: () => import('@/views/StandingsView.vue'),
    // Pública: a tabela pode ser vista por visitantes não autenticados.
    meta: { layout: 'default', public: true }
  },
  {
    path: '/ranking',
    name: 'ranking',
    component: () => import('@/views/RankingView.vue'),
    meta: { layout: 'default', public: true }
  },
  {
    path: '/minhas-apostas',
    name: 'my-bets',
    component: () => import('@/views/MyBetsView.vue'),
    meta: { layout: 'default' }
  },
  {
    path: '/perfil',
    name: 'profile',
    component: () => import('@/views/ProfileView.vue'),
    meta: { layout: 'default' }
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to) => {
  const auth = useAuthStore()
  if (!to.meta.public && !auth.isAuthenticated) {
    return { name: 'login', query: { redirect: to.fullPath } }
  }
  if ((to.name === 'login' || to.name === 'register') && auth.isAuthenticated) {
    return { name: 'games' }
  }
  return true
})

export default router
