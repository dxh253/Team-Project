import { createRouter, createWebHistory} from "vue-router";
// import {VueRouter} from "vue-router";
import Login from "../views/Login.vue"
import RegisterForm from "../views/RegisterForm.vue"
import EventsView from "../views/EventsViews.vue"
import EventsDetail from "../views/EventsDetail.vue"
import EventsForm from "../views/EventsForm.vue"
import PrivacyPolicy from "../views/PrivacyPolicy.vue"

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
            component: Login,

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

        },
        {
            path: "/:category_slug/:events_slug/",
            name: "EventsDetail",
            component: EventsDetail,

        },
        {
            path: "/events_form/",
            name: "EventsForm",
            component: EventsForm,

        },
        {
            path: "/privacy_policy/",
            name: "PrivacyPolicy",
            component: PrivacyPolicy,

        },
        {
            path: "/posts/",
            name: "Posts",
            component: () => import("../views/PostsList.vue")
        }
    ]
})

export default router 