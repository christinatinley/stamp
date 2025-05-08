<script>
import Slider from 'primevue/slider';
import Button from 'primevue/button';
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'PageSixForm',
    components: {
        Slider,
        Button,
    },
    computed: {
        // Assuming you have a Vuex store and formData is a getter
        ...mapGetters(['formData']),
    },
    methods: {
        // Assuming you have Vuex actions to set the experience ratings
        ...mapActions(['setExperiences',  'fetchHome', 'fetchItinerary']),
        async submitForm() {
            await this.fetchItinerary();
        }
    },
    data() {
        return {
            experiences: [
                { name: 'exploring local culture', rating: 0 },
                { name: 'historical sites & museums', rating: 0 },
                { name: 'art sites & museums', rating: 0 },
                { name: 'nature exploration', rating: 0 },
                { name: 'tours', rating: 0 },
                { name: 'shopping', rating: 0 },
            ],
        }
    },
}
</script>

<template>

<!-- experience rating section -->
       <div class="flex flex-col mb-4">
         <label class="text-2l text-black font-semi mb-4">What experiences are you interested in?</label>

         <!-- experience rating sliders -->
         <div v-for="(experience, index) in experiences" :key="index" class="flex flex-col">
           <label :for="'experience-' + experience.name" class="mb-2 text-black">
             rate your interest in {{ experience.name }}:
           </label>
           <Slider
             v-model="experience.rating"
            @change="setExperiences({ experience: experience.name, rating: experience.rating })"
             :min="0"
             :max="10"
             :step="1"
             :tooltip="true"
             :tooltipPosition="'top'"
             class="w-full"
             :id="'experience-' + experience.name"
          />
           <div class="text-center text-black mt-2">rating: {{ experience.rating }}</div>
         </div>
       </div>

<!-- Submit Button -->
    <div class="flex justify-center">
    <button
        type="submit"
        class="bg-[#CB769E] text-white font-semibold py-2 px-4 rounded-md hover:bg-[#b35f87] transition duration-200"
        @click="submitForm"
        >
        submit
    </button>
    </div>


</template>