<script>
import NavBar from './components/NavBar.vue';
import QuizFormPage from './quiz/QuizFormPage.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    QuizFormPage
  }
}
</script>

<template>
  <router-view/>
</template>

<style scoped>
</style>
