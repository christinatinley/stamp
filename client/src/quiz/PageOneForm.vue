<script>
import itineraryStore from '@/modules/itineraryStore';
import DatePicker from 'primevue/datepicker';
import Select from 'primevue/select';
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'PageOneForm',
  components: {
    DatePicker,
    Select,
  },
  computed: {
    ...mapGetters(['formData']),
  },
  data() {
    return {
      budgetOptions: [
        { label: '$', value: '$' },
        { label: '$$', value: '$$' },
        { label: '$$$', value: '$$$' },
        { label: '$$$$', value: '$$$$' },
        { label: '$$$$$', value: '$$$$$' },
      ],
    };
  },
  methods: {
    ...mapActions(['setDestination', 'setStartDate', 'setEndDate', 'setBudget']),
  },
};
</script>

<template>
  <div class="flex flex-col gap-6">
    <!-- Destination Input -->
    <div class="flex flex-col">
      <label class="mb-1 text-sm font-medium">Where will you be going?</label>
      <input
        id="destination"
        v-model="this.formData.destination"
        type="text"
        placeholder="city, state"
        class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
        required
        @input="setDestination($event.target.value)"
      />
    </div>

    <!-- Start and End Dates -->
    <div class="flex gap-4">
      <div class="flex flex-col w-1/2">
        <label class="mb-1 text-sm font-medium">Start Date</label>
        <DatePicker
          :modelValue="this.formData.startDate"
          @update:modelValue="setStartDate($event.target.value)"
          name="startDate"
          placeholder="MM/DD/YYYY"
          class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
          />
      </div>

      <div class="flex flex-col w-1/2">
        <label class="mb-1 text-sm font-medium">End Date</label>
        <DatePicker
          v-model="this.formData.endDate"
          name="endDate"
          placeholder="MM/DD/YYYY"
          class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
          />
      </div>
    </div>

    <!-- Budget Input -->
    <div class="flex flex-col">
      <label class="mb-1 text-sm font-medium">
        How much do you want to spend on this trip?
      </label>
      <Select
        id="budget"
        v-model="this.formData.budget"
        :options="budgetOptions"
        optionLabel="label"
        placeholder="select your maximum budget"
        class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
        @input="setBudget($event.target.value)"
      />
    </div>
     
  </div>
</template>

<style scoped>
  label {
    color: black;
    font-size: 0.875rem; /* matching text-sm size for the labels */
  }

  input, .p-datepicker, .p-select {
    color: black;
    font-size: 0.875rem; /* matching text-sm size for the input text */
  }

  ::v-deep(.p-dropdown-items .p-dropdown-item) {
    font-size: 0.875rem; 
  }
</style>
