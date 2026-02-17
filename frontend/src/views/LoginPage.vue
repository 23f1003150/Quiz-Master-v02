<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useMessageStore } from '@/stores/counter.js';
import { useAuthStore } from '@/stores/auth.js';

const router = useRouter();
const message_store = useMessageStore();
const auth_store = useAuthStore();

const email = ref('');
const password = ref('');

async function login() {
  const user = {
    email: email.value,
    password: password.value,
  };

  const response = await fetch('http://127.0.0.1:5000/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(user),
  });

  if (!response.ok) {
    const errordata = await response.json();
    alert(errordata.message);
  } else {
    const data = await response.json();
    message_store.updateErrorMessages(data.message);

    const user = {
      email: data.user_details.email,
      roles: data.user_details.roles,
    };
    auth_store.setUserCred(data.user_details.auth_token, user);

    localStorage.setItem('auth_token', data.user_details.auth_token);

    router.push('/dashboard');
  }
}
</script>

<template>
  <div class="container-fluid min-vh-100 d-flex align-items-center justify-content-center bg-light">
    <div class="card shadow-lg rounded-4 p-4" style="max-width: 450px; width: 100%;">
      <h2 class="text-center text-primary mb-4">Quiz Master Login</h2>
      
      <form @submit.prevent="login">
        <!-- Email -->
        <div class="mb-3">
          <label for="email" class="form-label fw-semibold">Email Address</label>
          <div class="input-group">
            <span class="input-group-text bg-white"><i class="bi bi-envelope"></i></span>
            <input
              type="email"
              id="email"
              class="form-control"
              placeholder="Enter your email"
              v-model="email"
              required
            />
          </div>
        </div>

        <!-- Password -->
        <div class="mb-3">
          <label for="password" class="form-label fw-semibold">Password</label>
          <div class="input-group">
            <span class="input-group-text bg-white"><i class="bi bi-lock"></i></span>
            <input
              type="password"
              id="password"
              class="form-control"
              placeholder="Enter your password"
              v-model="password"
              required
            />
          </div>
        </div>

        <!-- Submit button -->
        <button type="submit" class="btn btn-primary w-100 py-2 mt-2">
          <i class="bi bi-box-arrow-in-right me-2"></i> Login
        </button>
      </form>

      <!-- Divider -->
      <div class="text-center my-3">
        <small class="text-muted">Don’t have an account?</small>
      </div>

      <!-- Register link -->
      <button @click="router.push('/register')" class="btn btn-outline-secondary w-100">
        <i class="bi bi-person-plus me-2"></i> Register
      </button>
    </div>
  </div>
</template>

<style scoped>
body {
  background-color: #f8f9fa;
}
.card {
  border: none;
}
</style>
