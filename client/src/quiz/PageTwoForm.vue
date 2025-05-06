<script>
import MultiSelect from 'primevue/multiselect';

export default {
  name: 'PageTwoForm',
  props: {
    formData: Object,
  },
  components: {
    MultiSelect,
  },
  data() {
    return {
      selectedDates: [], 
    };
  },
  computed: {
    tripDates() {
      const start = new Date(this.formData.startDate);
      print(start);
      const end = new Date(this.formData.endDate);
      print(end);
      const dateArray = [];
      const currentDate = new Date(start);
      while (currentDate <= end) {
        const formattedDate = currentDate.toISOString().split('T')[0]; // Format: YYYY-MM-DD
        dateArray.push(formattedDate);
        currentDate.setDate(currentDate.getDate() + 1);
      }
      return dateArray;
    },
  },
};
</script>

<template>
  <!-- Multiselect Dates to Block out -->
  <div class="p-4">
    <label for="startDate" class="mb-1 text-sm font-medium">Select dates to block:</label>
    <MultiSelect
      v-model="selectedDates"
      :options="tripDates"
      placeholder="choose dates"
      display="chip"
      class="w-full md:w-80"
    />
    <div v-if="selectedDates.length" class="mt-4">
      <p class="font-medium text-black">Blocked Dates:</p>
      <ul class="list-disc text-black pl-5">
        <li v-for="date in selectedDates" :key="date">{{ date }}</li>
      </ul>
    </div>
  </div>
</template>


<style scoped>
  label {
    color: black;
    font-size: 0.875rem; 
  }

  input, .p-datepicker, .p-select {
    color: black;
    font-size: 0.875rem; 
  }

  ::v-deep(.p-dropdown-items .p-dropdown-item) {
    font-size: 0.875rem; 
  }
</style>


