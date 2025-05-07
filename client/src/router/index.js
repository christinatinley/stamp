import HomePage from "@/pages/HomePage.vue";
import ItineraryPage from "@/pages/ItineraryPage.vue";
import QuizFormPage from "@/pages/QuizFormPage.vue";
import TakeTheQuizPage from "@/pages/TakeTheQuizPage.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: HomePage,
        },
        {
            path: "/Quiz",
            component: QuizFormPage,
        },
        {
            path: "/TakeQuiz",
            component: TakeTheQuizPage
        },
        {
            path: "/Itinerary",
            component: ItineraryPage,
        }
    ],
});

export default router;