<script>
import MultiSelect from 'primevue/multiselect';

export default {
    name: 'PageFourForm',
    props: {
        formData: Object,
    },
    components: {
        MultiSelect,
    },
    data() {
        return {
            localForm: {
                cuisine: [],
                dietaryRestrictions: [],
            },
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
        <!-- Cuisine Preference MultiSelect -->
        <div class="flex flex-col">
            <label for="cuisine" class="mb-1 text-sm text-black font-medium">
                What type of cuisine do you prefer?
            </label>
            <MultiSelect
                id="cuisine"
                v-model="localForm.cuisine"
                :options="cuisineOptions"
                optionLabel="label"
                placeholder="Select your preferred cuisines"
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
                v-model="localForm.dietaryRestrictions"
                :options="dietaryOptions"
                optionLabel="label"
                placeholder="Select your dietary restrictions"
                class="rounded-md border border-gray-300 outline-none w-full text-black text-sm p-2"
            />
        </div>
    </div>

</template>