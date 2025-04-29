import Home from "@/pages/Home.vue";
import QuizFormPage from "@/pages/QuizFormPage.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: Home,
        },
        {
            path: "/Quiz",
            component: QuizFormPage,
        }
    ],
});

export default router;