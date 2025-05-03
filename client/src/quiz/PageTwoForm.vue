<script>
export default {
  name: 'PageTwoForm',
  props: {
    distanceWillingToTravel: {
      type: String,
      required: true,
    },
  },
  emits: ['update:distanceWillingToTravel'],
  methods: {
    validateDistanceWillingToTravel() {
      const distance = parseInt(this.distanceWillingToTravel, 10);
      if (isNaN(distance) || distance < 0) {
        alert('Please enter a valid positive number for the distance you are willing to travel.');
        return false;
      }
      return true;
    },
  },
};
</script>

<template>
  <div class="flex flex-col">
    <label for="distanceWillingToTravel" class="text-black text-sm font-medium mb-1">
      How far are you willing to travel?
    </label>
    <input
      id="distanceWillingToTravel"
      :value="distanceWillingToTravel"
      @input="$emit('update:distanceWillingToTravel', $event.target.value)"
      type="text"
      class="rounded-md border border-gray-300 outline-none w-full text-black p-2"
      required
    />
  </div>
</template>
