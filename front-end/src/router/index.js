import { createRouter, createWebHistory} from "vue-router";
import HomeView from "../views/HomeView.vue"
import RegisterForm from "../views/RegisterForm.vue"
import EventsView from "../views/EventsViews.vue"


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [
        {

            path: "/",
            name: "HomeView",
            component: HomeView
        },
        // {
        //     path: "help",
        //     name: "HelpSection",
        //     component: HelpSection
        // },
        {
            path: "/register/",
            name: "RegisterForm",
            component: RegisterForm
        },
        {
            path: "/events/",
            name: "EventsView",
            component: EventsView
        },
    ]
})

export default router 