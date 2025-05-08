<script>
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import { ScheduleXCalendar } from '@schedule-x/vue'
import {
  createCalendar,
  createViewDay,
  createViewMonthAgenda,
  createViewMonthGrid,
  createViewWeek,
} from '@schedule-x/calendar'
import '@schedule-x/theme-default/dist/index.css'
import { mapGetters } from 'vuex';
import { Card } from 'primevue';

export default {
  name: 'ItineraryPage',
  components: {
    NavBar,
    ScheduleXCalendar,
    Footer,
    Card
  },
  computed: {
    ...mapGetters(['itinerary']),
  }, 
  methods: {
    setupCalendarEvents(itinerary) {
      const events = [];
      let idCounter = 1;

      itinerary.forEach(day => {
        for (const [timeSlot, eventObj] of Object.entries(day)) {
          const [startStr, endStr] = timeSlot.split('–');
          const startDate = new Date(startStr);
          const endDate = new Date(endStr);

          events.push({
            id: idCounter++,
            title: eventObj.placeName,
            start: formatDate(startDate),
            end: formatDate(endDate),
            location: `https://www.google.com/maps?q=${eventObj.latitude},${eventObj.longitude}`
          });
        }
      });

      this.calendarApp = createCalendar({
        selectedDate: itinerary.length > 0
          ? Object.keys(itinerary[0])[0].slice(0, 10)
          : '',
        views: [
          createViewDay(),
          createViewWeek(),
          createViewMonthGrid(),
          createViewMonthAgenda(),
        ],
        events: events
      });
      function formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0'); // months are 0-based
        const day = String(date.getDate()).padStart(2, '0');
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        
        return `${year}-${month}-${day} ${hours}:${minutes}`;
      }
    }
  },
  watch: {
    itinerary: {
      handler(newItinerary) {
        if (newItinerary && Array.isArray(newItinerary)) {
          this.setupCalendarEvents(newItinerary);
        }
      },
      immediate: true
    }
  }
}
</script>

<template>
  <div class="relative w-full">
    <!-- HEADER SECTION with background image -->
    <div class="relative w-full h-[700px] flex flex-col justify-center items-center">
      <img
        src="@/assets/itinerary.svg"
        alt="german pic"
        class="w-full h-full object-cover absolute top-0 left-0 z-[-1]"
      />
      <NavBar class="absolute top-0 left-0 w-full" />
      <Card class="bg-transparent text-center w-1/3 border-none shadow-none mx-auto mt-10 align-middle">
        <template #title>
          <h1 class="leading-[1.25]">your personal itinerary</h1>
        </template>
        <template #content>
          <p class="text-text m-5">
            here’s your personal itinerary. if you dislike any suggestions feel free to change them (we take no offense)
          </p>
        </template>
      </Card>
    </div>

    <!-- CALENDAR BELOW (no overlapping) -->
    <ScheduleXCalendar
      :calendar-app="this.calendarApp"
      class="calendar w-4/5 mb-10 h-[700px] mx-auto mt-10"
    />
  </div>
  <Footer />
</template>

<style scoped>
.calendar {
    --sx-color-background: #FCF7EE;
    --sx-today-bg-color: #ffe0b2;
    --sx-color-on-primary-container: #475DFF;
    --sx-color-primary-container: #DDE1FF;
    --sx-color-primary: #475DFF;
}
</style>