<script setup>
const appName = "Quiz Master"
const tagline = "Enhance your learning with interactive quizzes and personalized feedback" 

const features = [
  {
    title: "Dynamic Quiz Management",
    desc: "Create, edit, and organize quizzes with structured subjects and chapters."
  },
  {
    title: "Real-Time Score Tracking",
    desc: "Instant result calculation with detailed performance analysis."
  },
  {
    title: "Prepare for Exams",
    desc: "Smooth and efficient quiz-taking experience to help you prepare for exams effectively."
  }
]
</script>

<template>
  <div class="home-wrapper">

    <section class="hero-section text-center">
      <div class="container">
        <h1 class="hero-title mb-3">
          {{ appName }}
        </h1>

        <p class="hero-tagline mb-4">
          {{ tagline }}
        </p>

        <RouterLink to="/login" class="btn btn-primary btn-lg me-3">
          Get Started
        </RouterLink>

        <RouterLink to="/register" class="btn btn-outline-primary btn-lg">
          Create Account
        </RouterLink>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features-section">
      <div class="container">
        <div class="row text-center">

          <div 
            class="col-md-4 mb-4"
            v-for="(feature, index) in features"
            :key="index"
          >
            <div class="feature-card h-100">
              <h4 class="feature-title mb-3">
                {{ feature.title }}
              </h4>
              <p class="feature-desc">
                {{ feature.desc }}
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

  </div>
</template>

<style scoped>
.home-wrapper {
  background-color: var(--white);
}
.hero-section {
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--white);
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  color: var(--secondary-color);
}

.hero-tagline {
  font-size: 1.2rem;
  color: var(--text-color);
}
/*
.btn-primary {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
}
*/
.btn-primary:hover {
  background-color: #0b2f52;
  border-color: #0b2f52;
  
}
.features-section {
  background-color: var(--light-bg);
  padding: 60px 0;
}

.feature-card {
  background-color: var(--white);
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
  transition: 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-title {
  color: var(--primary-color);
  font-weight: 600;
}

.feature-desc {
  color: var(--muted-color);
}
</style>
