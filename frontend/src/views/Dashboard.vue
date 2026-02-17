<template>
  <div>
    <component :is="dashboardComponent" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '@/stores/auth.js'
import AdminDashboard from './AdminDashboard.vue'
import UserDashboard from './UserDashboard.vue'

const auth = useAuthStore()

const dashboardComponent = computed(() => {
  return auth.isAdmin ? AdminDashboard : UserDashboard
})

console.log('Current User Roles:', auth.getUserRoles)
console.log('Is Admin?', auth.isAdmin)
</script>
