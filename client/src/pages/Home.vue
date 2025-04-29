<script setup>
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import Card from 'primevue/card';
import { Button } from 'primevue';
import { useRouter } from 'vue-router';

const router = useRouter();

</script>

<template>
    <div class="relative w-full h-screen overflow-hidden">
      <img src="@/assets/home_pic.svg" alt="german pic" class="w-full h-full object-cover absolute top-0 left-0 z-[-1] bg-blend-darken" />
      
      <NavBar />
      
      <div class="flex justify-center items-center w-full h-full">
        <Card class="bg-transparent text-center w-1/3 border-none shadow-none">
          <template #title>
            <h1 class="leading-[1.25]">seamless planning, lifelong memories</h1>
          </template>
          <template #content>
            <p class="text-text m-5">take the stress out of travel. you dream it, we take care of the rest</p>
          </template>
          <template #footer>
            <Button label="plan your trip today" class="p-5 bg-header-2 text-text rounded-lg" @click="router.push('/Quiz')" />
          </template>
        </Card>
      </div>
    </div>
    <Footer />
  </template>