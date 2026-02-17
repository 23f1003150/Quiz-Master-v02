<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const name = ref('');
const email = ref('');
const password = ref('');

const checkEmailMessage = ref('');
const passwordMessage = ref('');

function validatePassword() {
  if (password.value.length < 8) {
    passwordMessage.value = 'Password must be at least 8 characters long';
    return false;
  } else {
    passwordMessage.value = '';
    return true;
  }
}

async function register() {
  if (!validatePassword()) {
    alert('Please enter a valid password');
    return;
  }
  if (checkEmailMessage.value !== 'Email address is available') {
    alert('Use a valid email address');
    return;
  }

  const user = {
    name: name.value,
    email: email.value,
    password: password.value,
  };

  const response = await fetch('http://127.0.0.1:5000/api/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(user),
  });

  if (!response.ok) {
    const errorData = await response.json();
    alert(errorData.message);
  } else {
    const data = await response.json();
    alert(data.message);
    router.push('/login');
  }
}

function checkEmailAvailibility() {
  fetch('http://127.0.0.1:5000/api/check-email', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: email.value }),
  })
    .then((response) => (response.ok ? response.json() : null))
    .then((data) => {
      if (!data) return;
      if (data.available) {
        checkEmailMessage.value = 'Email address is available';
      } else {
        checkEmailMessage.value = 'Email address already taken';
      }
    })
    .catch(() => {
      console.error('Error checking email availability');
    });
}
</script>

<template>
  <div class="container-fluid min-vh-100 d-flex align-items-center justify-content-center bg-light">
    <div class="card shadow-lg rounded-4 p-4" style="max-width: 500px; width: 100%;">
      <h2 class="text-center text-primary mb-4">Create Your Quiz Master Account</h2>

      <form @submit.prevent="register">
        <!-- Name -->
        <div class="mb-3">
          <label for="nameInput" class="form-label fw-semibold">Full Name</label>
          <div class="input-group">
            <span class="input-group-text bg-white"><i class="bi bi-person"></i></span>
            <input
              type="text"
              class="form-control"
              id="nameInput"
              placeholder="Enter your full name"
              v-model="name"
              required
            />
          </div>
        </div>

        <!-- Email -->
        <div class="mb-3">
          <label for="emailInput" class="form-label fw-semibold">Email Address</label>
          <div class="input-group">
            <span class="input-group-text bg-white"><i class="bi bi-envelope"></i></span>
            <input
              type="email"
              class="form-control"
              id="emailInput"
              placeholder="Enter your email"
              v-model="email"
              @input="checkEmailAvailibility"
              required
            />
          </div>
          <p class="form-text" :class="checkEmailMessage.includes('available') ? 'text-success' : 'text-danger'">
            {{ checkEmailMessage }}
          </p>
        </div>

        <!-- Password -->
        <div class="mb-3">
          <label for="passwordInput" class="form-label fw-semibold">Password</label>
          <div class="input-group">
            <span class="input-group-text bg-white"><i class="bi bi-lock"></i></span>
            <input
              type="password"
              class="form-control"
              id="passwordInput"
              placeholder="Enter a strong password"
              v-model="password"
              @input="validatePassword"
              required
            />
          </div>
          <p class="form-text text-danger" v-if="passwordMessage">{{ passwordMessage }}</p>
        </div>

        <!-- Submit button -->
        <button type="submit" class="btn btn-success w-100 py-2 mt-2">
          <i class="bi bi-person-plus me-2"></i> Register
        </button>
      </form>

      <!-- Divider -->
      <div class="text-center my-3">
        <small class="text-muted">Already have an account?</small>
      </div>

      <!-- Login link -->
      <button @click="router.push('/login')" class="btn btn-outline-secondary w-100">
        <i class="bi bi-box-arrow-in-right me-2"></i> Login
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
