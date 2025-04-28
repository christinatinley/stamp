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
  <div class="quiz-form-container">
    <div class="quiz-form-card">
      <p class="text-2xl font-bold mb-4">Quiz Form</p>

      <div class="p-fluid mb-3">
        <div class="p-field mb-4">
          <label for="name">Your Name</label>
          <InputText id="name" v-model="name" />
        </div>

        <div class="p-field mb-4">
          <label for="favoriteColor">Favorite Color?</label>
          <InputText id="favoriteColor" v-model="favoriteColor" />
        </div>

        <Button label="Submit" icon="pi pi-check" @click="submitQuiz" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.quiz-form-container {
  min-height: 100vh;
  min-width: 100vh;
  background-color: #6D213C; 
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
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
