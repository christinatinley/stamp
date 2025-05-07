<script>
import Select from 'primevue/select';

export default{
  name: 'PageThreeForm',
  components: {
    Select,
  },
  props: {
    formData: Object
  },
  data() {
    return {
      localForm: {
        numberOfTravelers: null,
        lodging: '',
      },
      numberOptions: Array.from({ length: 10 }, (_, i) => ({
        label: `${i + 1}`,
        value: i + 1,
      })),
      lodgingOptions: [
        { label: 'Hotel', value: 'hotel' },
        { label: 'Hostel', value: 'hostel' },
        { label: 'Airbnb', value: 'airbnb' },
        { label: 'Camping', value: 'camping' },
      ],
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
}
</script>

<template>
  <div class="space-y-6">
    <!-- Number of Travelers Select -->
    <div class="flex flex-col">
      <label for="numberOfTravelers" class="mb-1 text-sm text-black font-medium">
        How many travelers will be on this trip?
      </label>
      <Select
        id="numberOfTravelers"
        v-model="localForm.numberOfTravelers"
        :options="numberOptions"
        optionLabel="label"
        placeholder="Select number of travelers"
        class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
      />
    </div>

    <!-- Lodging Preference Select -->
    <div class="flex flex-col">
      <label for="lodging" class="mb-1 text-sm text-black font-medium">
        What type of lodging do you prefer?
      </label>
      <Select
        id="lodging"
        v-model="localForm.lodging"
        :options="lodgingOptions"
        optionLabel="label"
        placeholder="Select lodging type"
        class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
      />
    </div>
  </div>
</template>