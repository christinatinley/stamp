<script>
import MultiSelect from 'primevue/multiselect';
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'PageFiveForm',
    components: {
        MultiSelect,
    },
    computed: {
        ...mapGetters(['formData']),
    },
    data() {
        return {
            transportationOptions: [
                { label: 'Car', value: 'car' },
                { label: 'Bus', value: 'bus' },
                { label: 'Train', value: 'train' },
                { label: 'Plane', value: 'plane' },
                { label: 'Bicycle', value: 'bicycle' },
                { label: 'Walking', value: 'walking' },
            ],   
        };
    },
    methods: {
        ...mapActions(['setTransportationToDestination', 'setTransportationDuringTrip']),
    },
}
</script>

<template>
    <div class="space-y-6">
        <!-- Transportation to Destination MultiSelect -->
        <div class="flex flex-col">
            <label for="transportationToDestination" class="mb-1 text-sm text-black font-medium">
                How will you get to your destination?
            </label>
            <MultiSelect
                id="transportationToDestination"
                :modelValue="this.formData.transportationToDestination"
                @update:modelValue="setTransportationToDestination($event)"
                :options="transportationOptions"
                optionLabel="label"
                optionValue="value"
                placeholder="select your transportation options"
                class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
            />
        </div>

        <!-- Transportation During Trip MultiSelect -->
        <div class="flex flex-col">
            <label for="transportationDuringTrip" class="mb-1 text-sm text-black font-medium">
                How will you get around during your trip?
            </label>
            <MultiSelect
                id="transportationDuringTrip"
                :modelValue="this.formData.transportationDuringTrip"
                @update:modelValue="setTransportationDuringTrip($event)"
                :options="transportationOptions"
                optionLabel="label"
                placeholder="select your transportation options"
                class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
            />
        </div>
    </div>
</template>