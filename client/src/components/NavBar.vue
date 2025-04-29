<script setup>
import { Menubar } from 'primevue';
import Avatar from 'primevue/avatar';
import { ref } from 'vue';

const items = ref([
    {
        label: "home",
        to: "/",
    }, 
    {
        label: "take the quiz",
        to: "/TakeQuiz",
    }
])

</script>

<template>
        <Menubar :model="items" class="bg-transparent px-10 items-center">
            <template #start>
                <div class="mr-5">
                    <h3>stamp</h3>
                </div>
            </template>
            <template #item="{item}">
                <router-link :to="item.to" class="m-5 flex items-center text-lg">
                    <span>{{ item.label }}</span>
                </router-link>
            </template>
            <template #end>
                <Avatar label="C" shape="circle" size="large" class="bg-accent-1 font-abril text-background"/>
            </template>
        </Menubar>
</template>