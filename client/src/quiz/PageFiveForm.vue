<script>
import MultiSelect from 'primevue/multiselect';

export default {
    name: 'PageFiveForm',
    props: {
        formData: Object,
    },
    components: {
        MultiSelect,
    },
    data() {
        return {
            localForm: {
                transportationToDestination: [],
                transportationDuringTrip: [],
            },
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
    watch: {
        localForm: {
            handler(newVal) {
                this.$emit('update:formData', newVal);
            },
            deep: true,
        },
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
                v-model="localForm.transportationToDestination"
                :options="transportationOptions"
                optionLabel="label"
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
                v-model="localForm.transportationDuringTrip"
                :options="transportationOptions"
                optionLabel="label"
                placeholder="select your transportation options"
                class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
            />
        </div>
    </div>
</template>