<script>
import DatePicker from 'primevue/datepicker';

export default {
  name: 'PageOneForm',
  components: {
    DatePicker
  },
  props: {
    formData: Object
  },
  data() {
    return {
      localForm: {
        destination: '',
        startDate: '',
        endDate: '',
        budget: ''  // Budget will hold the selected value
      }
    };
  },
  watch: {
    localForm: {
      handler(newVal) {
        this.$emit('update:formData', newVal);
      },
      deep: true
    }
  }
};
</script>

<template>
  <div class="flex flex-col gap-6">
    <!-- Destination Input -->
    <div class="flex flex-col">
      <label for="destination" class="mb-1 text-sm font-medium">Where will you be going?</label>
      <input
        id="destination"
        v-model="localForm.destination"
        type="text"
        class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
        required
      />
    </div>

    <!-- Start and End Dates -->
    <div class="flex gap-4">
      <div class="flex flex-col w-1/2">
        <label for="startDate" class="mb-1 text-sm font-medium">Start Date</label>
        <DatePicker
          v-model="localForm.startDate"
          name="startDate"
          class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
          />
      </div>

      <div class="flex flex-col w-1/2">
        <label for="endDate" class="mb-1 text-sm font-medium">End Date</label>
        <DatePicker
          v-model="localForm.endDate"
          name="endDate"
          class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
          />
      </div>
    </div>

    <!-- Budget Input -->
    <div class="flex flex-col">
      <label for="budget" class="mb-1 text-sm font-medium">Enter the maximum amount you are willing to spend on your trip:</label>
      <input
        id="budget"
        v-model="localForm.budget"
        type="text"
        class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
      />
      <!-- <CascadeSelect
        id="budget"
        v-model="localForm.budget"
        :options="budgetRanges"
        optionLabel="label"
        optionValue="value"
        class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
        placeholder="Select a budget range"
        required
      /> -->
    </div>  
  </div>
</template>

<style scoped>
  label {
    color: black;
    font-size: 0.875rem; /* matching text-sm size for the labels */
  }

  input, .p-datepicker {
    color: black;
    font-size: 0.875rem; /* matching text-sm size for the input text */
  }
</style>
