<script setup>
import NavBar from '@/components/NavBar.vue';
import { ScheduleXCalendar } from '@schedule-x/vue'
import {
  createCalendar,
  createViewDay,
  createViewMonthAgenda,
  createViewMonthGrid,
  createViewWeek,
} from '@schedule-x/calendar'
import '@schedule-x/theme-default/dist/index.css'

const calendarApp = createCalendar({
  selectedDate: '2023-12-19',
  views: [
    createViewDay(),
    createViewWeek(),
    createViewMonthGrid(),
    createViewMonthAgenda(),
  ],
  events: [
    {
      id: 1,
      title: 'New York Stock Exchange',
      start: '2023-12-19',
      end: '2023-12-19',
    },
    {
      id: 2,
      title: 'Event 2',
      start: '2023-12-20 12:00',
      end: '2023-12-20 13:00',
    },
  ],
})
</script>

<template>
    <NavBar/>
    <div class="flex justify-center items-center w-full h-full pl-20 pr-20">
        <ScheduleXCalendar :calendar-app="calendarApp" class="calendar w-full"/>
    </div>
</template>

<style scoped>
.calendar {
    --sx-color-background: #FCF7EE;
    --sx-today-bg-color: #ffe0b2;
}
</style>