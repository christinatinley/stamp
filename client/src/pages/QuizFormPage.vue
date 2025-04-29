<script>
import { Form } from '@primevue/forms';
import DatePicker from 'primevue/datepicker';
import Message from 'primevue/message';

export default {
  name: 'QuizFormPage',
  components: {
    DatePicker,
    Message,
  },
  data() {
    return {
      destination: '',
      description: '',
      startDate: '',
      endDate: '',
      budget: '',
    };
  },
  methods: {
    submitForm() {
      console.log('Form submitted!', {
        destination: this.destination,
        description: this.description,
        startDate: this.startDate,
        endDate: this.endDate,
        budget: this.budget,
      });
    },
  },
};
</script>

<template>
  <div class="flex flex-col w-full">
    <h2 class="px-6 text-2xl font-bold mb-4">Travel Quiz</h2>
    <Form
      v-slot="$form"
      @submit="submitForm"
      class="flex flex-col gap-4 w-full p-6"
    >
      <div class="p-fluid w-full flex flex-col gap-4">
        <!-- destination input -->
        <div class="flex flex-col">
          <label for="destination" class="mb-1 text-sm font-medium">Where will you be going?</label>
          <input
            id="destination"
            v-model="destination"
            type="text"
            class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
            required
          />
        </div>

        <!-- start and end date pickers (side by side) -->
        <div class="flex gap-4">
          <!-- start date -->
          <div class="flex flex-col w-1/2">
            <label for="start-date" class="mb-1 text-sm font-medium">Start Date</label>
            <DatePicker
              v-model="startDate"
              name="start-date"
              class="w-full"
              :class="{'text-black': startDate}"
            />
          </div>

          <!-- End Date -->
          <div class="flex flex-col w-1/2">
            <label for="end-date" class="mb-1 text-sm font-medium">End Date</label>
            <DatePicker
              v-model="endDate"
              name="end-date"
              class="w-full"
              :class="{'text-black': endDate}"
            />
          </div>
        </div>

        <!-- <div class="flex flex-col">
          <label for="description" class="mb-1 text-sm font-medium">Please enter your budget for the trip:</label>
          <textarea
            id="description"
            v-model="description"
            class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
            required
          ></textarea>
        </div> -->

        <!-- budget input -->
        <div class="flex flex-col">
          <label for="budget" class="mb-1 text-sm font-medium">Please enter your budget for the trip:</label>
          <label for="budget" class="mb-1 text-sm font-medium">Enter the maximum amount you are willing to spend on your trip:</label>

          <input
            id="budget"
            v-model="budget"
            type="text"
            class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
            required
          />
        </div>

        <!-- submit button -->
        <button type="submit" class="p-button p-component w-full bg-[#F9F0DC] hover:bg-[#E5D9A2] text-black">
          submit
        </button>
      </div>
    </Form>
  </div>
</template>

<style scoped>
/* ensure text input is black */
.p-inputtext {
  color: black !important;
}
</style>
