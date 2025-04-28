<script>
import NavBar from './components/NavBar.vue';
import QuizFormPage from './pages/QuizFormPage.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    QuizFormPage
  }
}
</script>

<template>
  <NavBar/>
  <QuizFormPage />
</template>

<style scoped>

</style>
