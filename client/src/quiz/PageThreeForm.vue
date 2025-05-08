<script>
import Select from 'primevue/select';
import { mapActions, mapGetters } from 'vuex';

export default{
  name: 'PageThreeForm',
  components: {
    Select,
  },
  computed: {
    ...mapGetters(['formData']),
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
  methods: {
    ...mapActions(['setNumberOfTravelers', 'setLodging']),
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
        :modelValue="this.formData.numberOfTravelers"
        @update:modelValue="setNumberOfTravelers($event.value)"
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
        :modelValue="this.formData.lodging"
        @update:modelValue="setLodging($event.value)"
        :options="lodgingOptions"
        optionLabel="label"
        placeholder="Select lodging type"
        class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
      />
    </div>
  </div>
</template>