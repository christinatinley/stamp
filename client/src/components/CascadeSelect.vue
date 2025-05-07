<script>
    import CascadeSelect from 'primevue/cascadeselect';

    export default {
        data() {
            return {
            selectedCity: null,
            cities: [
                {
                name: 'North America',
                items: [
                    {
                    name: 'USA',
                    items: ['New York', 'Los Angeles', 'Chicago']
                    },
                    {
                    name: 'Canada',
                    items: ['Toronto', 'Montreal', 'Vancouver']
                    }
                ]
                },
                {
                name: 'Europe',
                items: [
                    {
                    name: 'UK',
                    items: ['London', 'Manchester', 'Birmingham']
                    },
                    {
                    name: 'France',
                    items: ['Paris', 'Marseille', 'Lyon']
                    }
                ]
                }
            ]
            };
        }
        };
</script>

<template>

    <CascadeSelect v-model="selectedCity" :options="cities" optionGroupLabel="name" optionGroupChildren="items" />

</template>