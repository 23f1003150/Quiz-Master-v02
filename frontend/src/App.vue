<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<template>
  <div class="container-fluid">
    <nav class="navbar navbar-expand-lg navbar-dark blue-navbar">

      <div class="container-fluid">
        <RouterLink class="navbar-brand" to="/dashboard">QuizMasterV2</RouterLink>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0" v-if="isAuthenticated">
            <li class="nav-item">
              <RouterLink class="nav-link" to="/dashboard">Home</RouterLink>
            </li>
            
            <li class="nav-item" v-if="isAdmin">
              <RouterLink class="nav-link" to="/admin/users">Operations</RouterLink>
            </li>

          </ul>

          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item" v-if="!isAuthenticated">
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
            <li class="nav-item" v-if="!isAuthenticated">
              <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </li>
            <li class="nav-item" v-if="isAuthenticated">
              <span class="nav-link text-white">Welcome, {{ userEmail }}</span>
            </li>
            <li class="nav-item" v-if="isAuthenticated">
              <button class="btn btn-outline-danger btn-sm mt-1" @click="logout">Logout</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container mt-2" v-if="ErrorMessages">
      <div class="alert alert-info text-center" role="alert">
        {{ ErrorMessages }}
      </div>
    </div>
    <RouterView />
  </div>
</template>


<style scoped>
.blue-navbar {
  background-color: #1f3c88; 
  padding: 12px 24px;
}
.navbar-brand {
  font-weight: 600;
  font-size: 1.2rem;
  color: #ffffff;
}
.navbar-brand:hover {
  color: #e6e6e6;
}
.nav-link {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  transition: 0.3s ease;
}
.nav-link:hover {
  color: #ffffff;
}
.router-link-active {
  color: #ffffff !important;
  border-bottom: 2px solid #ffffff;
}
.navbar span.nav-link {
  color: #ffffff;
}
.navbar-toggler {
  border-color: rgba(255, 255, 255, 0.5);
}
</style>
