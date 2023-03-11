import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: () => import("../views/HomepageView.vue"),
        },
        {
            path: "/study",
            name: "studyGroups",
            component: () => import("../views/StudyGroupsView.vue"),
        },
    ],
});

export default router;
