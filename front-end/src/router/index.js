import { createRouter, createWebHistory} from "vue-router";
// import {VueRouter} from "vue-router";
import Login from "../views/Login.vue"
import RegisterForm from "../views/RegisterForm.vue"
import EventsView from "../views/EventsViews.vue"
import EventsDetail from "../views/EventsDetail.vue"

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "Home",
            component: Login
        },
        {

            path: "/login/",
            name: "Login",
            component: Login
        },
        {
            path: "/register/",
            name: "RegisterForm",
            component: RegisterForm
        },
        {
            path: "/events/",
            name: "EventsView",
            component: EventsView,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: "/:category_slug/:events_slug/",
            name: "EventsDetail",
            component: EventsDetail
        }
    ]
})

export default router 