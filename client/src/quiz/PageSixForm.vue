<script>
import Slider from 'primevue/slider';
import Button from 'primevue/button';

export default {
    name: 'PageSixForm',
    components: {
        Slider,
        Button,
    },
    props: {
        formData: Object
    },
    data() {
        return {
            localForm: {
                experiences: [],
            },
            experiences: [
                { name: 'historical sites', rating: 0 },
                { name: 'museums', rating: 0 },
                { name: 'adventure activities', rating: 0 },
                { name: 'nature exploration', rating: 0 },
                { name: 'local cuisine', rating: 0 },
            ],
        }
    },
    watch: {
        experiences: {
            handler(newVal) {
                this.$emit('update:formData', { experiences: newVal });
            },
            deep: true,
        },
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
    >
        submit
    </button>
    </div>


</template>