<script>
import NavBar from '@/components/NavBar.vue';
import PageOneForm from '@/quiz/PageOneForm.vue';
import PageTwoForm from '@/quiz/PageTwoForm.vue';
import Paginator from 'primevue/paginator';

export default {
  name: 'QuizFormPage',
  components: {
    NavBar,
    PageOneForm,
    PageTwoForm,
    Paginator,
  },
  data() {
    return {
      currentPage: 0,
      formData: {
        destination: '',
        startDate: '',
        endDate: '',
        budget: '',
        numberOfTravelers: '',
        lodging: '',
        distanceWillingToTravel: '',
      },
    };
  },
  computed: {
    totalPages() {
      return this.pages.length;
    },
    currentFormComponent() {
      return this.pages[this.currentPage] || null;
    },
    pages() {
      return [PageOneForm, PageTwoForm];
    },
  },
};
</script>

<template>
  <div class="relative min-h-screen flex flex-col">

    <!-- Navigation bar -->
    <NavBar />

    <!-- Background image -->
    <img
      src="@/assets/travel_quiz_background.jpg"
      alt="Travel Quiz Background"
      class="w-full h-[45vh] object-cover absolute top-0 left-0 z-[-1] opacity-70"
    />

    <!-- Header -->
    <div class="pt-44 text-center text-white">
      <h2 class="text-4xl font-bold mb-4 drop-shadow-md">Travel Quiz</h2>
    </div>

    <!-- Form Container -->
    <div class="bg-white mt-10 p-8 mx-auto w-full max-w-3xl rounded-lg shadow-md z-10">
      <component
        :is="currentFormComponent"
        v-model:destination="formData.destination"
        v-model:startDate="formData.startDate"
        v-model:endDate="formData.endDate"
        v-model:budget="formData.budget"
        v-model:numberOfTravelers="formData.numberOfTravelers"
        v-model:lodging="formData.lodging"
        v-model:distanceWillingToTravel="formData.distanceWillingToTravel"
      />
    </div>

    <!-- Paginator -->
    <div class="mt-6 mb-10 flex justify-center z-10">
      <Paginator
        :rows="1"
        :totalRecords="totalPages"
        :first="currentPage"
        @page="e => currentPage = e.page"
      />
    </div>
  </div>
</template>

<style scoped>
.p-inputtext {
 color: black !important;
}

</style>
