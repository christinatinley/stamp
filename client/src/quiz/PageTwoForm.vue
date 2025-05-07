<script>
import MultiSelect from 'primevue/multiselect';
import DatePicker from 'primevue/datepicker';
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'PageTwoForm',
  components: {
    MultiSelect,
    DatePicker,
  },
  computed: {
    ...mapGetters(['formData']),
    selectedDates: {
      get() {
        return this.formData.selectedDates;
      },
      set(value) {
        const updated = { ...this.formData, selectedDates: value };
        this.$emit('update:formData', updated);
      },
    },
    blockedTimes: {
      get() {
        return this.formData.blockedTimes;
      },
      set(value) {
        const updated = { ...this.formData, blockedTimes: value };
        this.$emit('update:formData', updated);
      },
    },
    tripDates() {
      const start = new Date(this.formData.startDate);
      const end = new Date(this.formData.endDate);
      const dateArray = [];
      const currentDate = new Date(start);
      while (currentDate <= end) {
        const formattedDate = currentDate.toISOString().split('T')[0];
        dateArray.push(formattedDate);
        currentDate.setDate(currentDate.getDate() + 1);
      }
      return dateArray;
    },
  },
  methods: {
    ...mapActions(['setBlockedTimes']),
    updateTime(date, type, value) {
      const updated = { ...this.blockedTimes };
      if (!updated[date]) {
        updated[date] = { start: null, end: null };
      }
      updated[date][type] = value;
      this.blockedTimes = updated;
    },
  },
};
</script>

<template>
  <div class="p-4">
    <!-- Multiselect Dates to Block out -->
    <label for="startDate" class="mb-1 text-sm font-medium">Select dates to block:</label>
    <MultiSelect
      v-model="selectedDates"
      :options="tripDates"
      placeholder="Choose dates"
      display="chip"
      class="w-full md:w-80"
    />

    <!-- Per-date Time Block Inputs -->
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
              :modelValue="blockedTimes[date]?.start || null"
              @update:modelValue="updateTime(date, 'start', $event)"
              timeOnly
              class="w-full"
            />
          </div>
          <div>
            <label class="block text-sm font-medium mb-1">End Time</label>
            <DatePicker
              :modelValue="blockedTimes[date]?.end || null"
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
