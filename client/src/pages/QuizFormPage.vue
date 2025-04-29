<script>
import { Form } from '@primevue/forms';
import DatePicker from 'primevue/datepicker';
import Message from 'primevue/message';
import Slider from 'primevue/slider';

export default {
  name: 'QuizFormPage',
  components: {
    DatePicker,
    Message,
    Slider,
  },
  data() {
    return {
      destination: '',
      description: '',
      startDate: '',
      endDate: '',
      budget: '',
      numberOfTravelers: '',
      lodging: '',
      experiences: [
        { name: 'Historical Sites', rating: 0 },
        { name: 'Museums', rating: 0 },
        { name: 'Adventure Activities', rating: 0 },
        { name: 'Nature Exploration', rating: 0 },
        { name: 'Local Cuisine', rating: 0 },
      ],
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
        numberOfTravelers: this.numberOfTravelers,
        lodging: this.lodging,
        experiences: this.experiences,
      });
    },
  },
};
</script>

<template>
  <div class="flex flex-col w-full">
    <h2 class="px-40 text-4xl font-bold mb-4">Travel Quiz</h2>
    <Form
      v-slot="$form"
      @submit="submitForm"
      class="flex flex-col gap-4 w-full px-40 py-6"
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
          <label for="budget" class="mb-1 text-sm font-medium">Enter the maximum amount you are willing to spend on your trip:</label>

          <input
            id="budget"
            v-model="budget"
            type="text"
            class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
            required
          />
        </div>

        <!-- number of people input -->
        <div class="flex flex-col">
            <label for="numberOfTravelers" class="mb-1 text-sm font-medium">How many people will be traveling for this trip?</label>

            <input
                id="numberOfTravelers"
                v-model="numberOfTravelers"
                type="text"
                class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
                required
                />
        </div>

        <!-- lodging input -->
        <div class="flex flex-col">
            <label for="lodging" class="mb-1 text-sm font-medium">what type of lodging are you interested in?</label>

            <input
                id="lodging"
                v-model="lodging"
                type="text"
                class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
                required
                />
        </div>

        <!-- Experience Rating Section -->
        <div class="flex flex-col mb-4">
          <h2 class="text-2xl font-semibold mb-4">What experiences are you interested in?</h2>

          <!-- Experience Rating Sliders -->
          <div v-for="(experience, index) in experiences" :key="index" class="flex flex-col mb-4">
            <label :for="'experience-' + experience.name" class="mb-2">
              Rate your interest in {{ experience.name }}:
            </label>
            <Slider 
              v-model="experience.rating"
              :min="0"
              :max="10"
              :step="1"
              :tooltip="true"
              :tooltipPosition="'top'"
              class="w-full"
              :id="'experience-' + experience.name"
            />
            <div class="text-center mt-2">Rating: {{ experience.rating }}</div>
          </div>
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
