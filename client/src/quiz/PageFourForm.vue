<script>
import MultiSelect from 'primevue/multiselect';
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'PageFourForm',
    components: {
        MultiSelect,
    },
    computed: {
        ...mapGetters(['formData']),
    },
    data() {
        return {
            cuisineOptions: [
                { label: 'Cuban', value: 'cuban' },
                { label: 'American', value: 'american' },
                { label: 'French', value: 'french' },
                { label: 'Italian', value: 'italian' },
                { label: 'Chinese', value: 'chinese' },
                { label: 'Japanese', value: 'japanese' },
            ],
            dietaryOptions: [
                { label: 'Vegetarian', value: 'vegetarian' },
                { label: 'Vegan', value: 'vegan' },
                { label: 'Gluten-Free', value: 'gluten-free' },
                { label: 'Dairy-Free', value: 'dairy-free' },
            ],
        };
    },
    methods: {
        ...mapActions(['setCuisine', 'setDietaryRestrictions']),
    },
}
</script>

<template>

    <div class="space-y-6">
        <!-- Cuisine Preference MultiSelect -->
        <div class="flex flex-col">
            <label for="cuisine" class="mb-1 text-sm text-black font-medium">
                What type of cuisine do you prefer?
            </label>
            <MultiSelect
                id="cuisine"
                :modelValue="this.formData.cuisines"
                @update:modelValue="setCuisine($event)"
                :options="cuisineOptions"
                optionLabel="label"
                optionValue="value"
                placeholder="select your preferred cuisines"
                class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
            />
        </div>

        <!-- Dietary Restrictions MultiSelect -->
        <div class="flex flex-col">
            <label for="dietaryRestrictions" class="mb-1 text-sm text-black font-medium">
                Do you have any dietary restrictions?
            </label>
            <MultiSelect
                id="dietaryRestrictions"
                :modelValue="this.formData.dietaryRestrictions"
                @update:modelValue="setDietaryRestrictions($event)"
                :options="dietaryOptions"
                optionLabel="label"
                optionValue="value"
                placeholder="select your dietary restrictions"
                class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
            />
        </div>
    </div>

</template>