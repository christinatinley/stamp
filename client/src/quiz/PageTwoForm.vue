<script setup>
import { ref, computed, onMounted } from 'vue';
import MultiSelect from 'primevue/multiselect';
import DatePicker from 'primevue/datepicker';
import { useStore } from 'vuex';

const store = useStore();
const formData = computed(() => store.getters.formData);

const selectedDates = ref([]);

onMounted(() => {
  if (formData.value?.blockedTimes) {
    selectedDates.value = Object.keys(formData.value.blockedTimes);
  }
});

// console.log('blockedTimes:', formData.value.blockedTimes['2025-05-13'].end);
// console.log('selectedDates:', selectedDates.value);
// console.log('start time for first date:', formData.value.blockedTimes[selectedDates.value[0]]?.start);

const tripDates = computed(() => {
  console.log('Form data:', formData.value.blockedTimes);
  const start = new Date(formData.value.startDate);
  const end = new Date(formData.value.endDate);
  const dateArray = [];
  const currentDate = new Date(start);
  while (currentDate <= end) {
    const formattedDate = currentDate.toISOString().split('T')[0];
    dateArray.push(formattedDate);
    currentDate.setDate(currentDate.getDate() + 1);
  }
  return dateArray;
});

function updateTime(date, type, value) {
   // Get hours and minutes from selected time
  const hours = value.getHours();
  const minutes = value.getMinutes();

  // Create a Date object using the date + selected time
  const combinedDateTime = new Date(date + 'T00:00:00');
  combinedDateTime.setHours(hours);
  combinedDateTime.setMinutes(minutes);

  const currentTimes = formData.value.blockedTimes[date] || { start: null, end: null };
  const newTimes = { ...currentTimes, [type]: combinedDateTime };
  console.log('Saving datetime:', newTimes);

  store.dispatch('setBlockedTimes', { date, times: newTimes });
}

</script>

<template>
  <div class="p-4">
    <label class="mb-1 text-sm font-medium">Select dates to block:</label>
    <MultiSelect
      v-model="selectedDates"
      :options="tripDates"
      placeholder="Choose dates"
      display="chip"
      class="w-full md:w-80"
    />

    <div v-if="selectedDates.length" class="mt-6 space-y-6">
      <div
        v-for="date in selectedDates"
        :key="date"
        class="border p-4 rounded shadow-sm bg-white"
      >
        <p class="font-semibold text-black mb-2">{{ date }}</p>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium mb-1">Start Time</label>
            <DatePicker
              :modelValue="formData.value?.blockedTimes[date]?.start || null"
              @update:modelValue="updateTime(date, 'start', $event)"
              timeOnly
              class="w-full"
            />
          </div>
          <div>
            <label class="block text-sm font-medium mb-1">End Time</label>
            <DatePicker
              :modelValue="formData.value?.blockedTimes[date]?.end || null"
              @update:modelValue="updateTime(date, 'end', $event)"
              timeOnly
              class="w-full"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
label {
  color: black;
  font-size: 0.875rem;
}

input,
.p-datepicker,
.p-select {
  color: black;
  font-size: 0.875rem;
}

::v-deep(.p-dropdown-items .p-dropdown-item) {
  font-size: 0.875rem;
}
</style>
