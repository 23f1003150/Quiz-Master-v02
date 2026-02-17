import { createRouter, createWebHistory } from 'vue-router'

import LoginPage from '../views/LoginPage.vue'


const RegisterPage = () => import('../views/RegisterPage.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: () => import('../views/Home.vue') },
    {
      path: '/login',
      name: 'Login',
      component: LoginPage
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterPage
    }

  ],
})

export default router
