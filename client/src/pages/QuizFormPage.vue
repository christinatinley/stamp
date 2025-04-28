<script>
export default {
  name: 'QuizFormPage',
  data() {
    return {
      name: '',
      favoriteColor: ''
    };
  },
  methods: {
    submitQuiz() {
      console.log('Submitting quiz:', {
        name: this.name,
        favoriteColor: this.favoriteColor
      });
    }
  }
};
</script>

<template>
  <div class="full-screen-wrapper">
    <div class="quiz-form-card">
      <p class="text-2xl font-bold mb-4">Quiz Form</p>
      <i class="pi pi-check"></i>
    </div>
  </div>
</template>

<style scoped>
.full-screen-wrapper {
  min-height: 100vh;
  min-width: 100vw; 
  background-color: #f0f4f8; /* Your background color */
  display: flex;
  justify-content: center;
  align-items: center;
}

.quiz-form-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
}
</style>