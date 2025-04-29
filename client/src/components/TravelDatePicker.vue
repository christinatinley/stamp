<script setup>
import { ref } from 'vue';
import Calendar from 'primevue/calendar';

const selectedDates = ref([]);
</script>

<template>
    <div class="w-full">
      <Calendar
        v-model="selectedDates"
        selectionMode="range"
        showIcon
        dateFormat="yy-mm-dd"
        class="w-full h-[300px] bg-white border"
      />
    </div>
  </template>
  

  
  
