import { createRouter, createWebHistory} from "vue-router";
// import {VueRouter} from "vue-router";
import Login from "../views/Login.vue"
import RegisterForm from "../views/RegisterForm.vue"
import EventsView from "../views/EventsViews.vue"
import EventsDetail from "../views/EventsDetail.vue"
import EventsForm from "../views/EventsForm.vue"
import PrivacyPolicy from "../views/PrivacyPolicy.vue"
import EventsCategory from "../views/EventsCategory.vue"

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
            meta: {
                requiresAuth: true
            }

        },
        {
            path: "/events/:category_slug/:events_slug/",
            name: "EventsDetail",
            component: EventsDetail,
            meta: {
                requiresAuth: true
            }

        },
        {
            path: "/events/:category_slug/",
            name: "EventsCategory",
            component: EventsCategory,
            meta: {
                requiresAuth: true
            }

        },
        {
            path: "/events_form/",
            name: "EventsForm",
            component: EventsForm,
            meta: {
                requiresAuth: true
            }

        },
        {
            path: "/privacy_policy/",
            name: "PrivacyPolicy",
            component: PrivacyPolicy,

        }
    ]
});


export default router 