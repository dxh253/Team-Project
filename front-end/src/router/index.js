import { createRouter, createWebHistory} from "vue-router";
// import {VueRouter} from "vue-router";
import Login from "../views/Login.vue"
import RegisterForm from "../views/RegisterForm.vue"
import EventsView from "../views/EventsViews.vue"
import EventsDetail from "../views/EventsDetail.vue"
import EventsForm from "../views/EventsForm.vue"
import ForumViews from "../views/ForumViews.vue"
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
            meta:{
                requiresLogin: false
            }
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
            component: EventsDetail,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: "/events_form/",
            name: "EventsForm",
            component: EventsForm,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: "/privacy_policy/",
            name: "PrivacyPolicy",
            component: PrivacyPolicy,
            meta: {
                requiresLogin: false
            }
        },
        {
            path: "/forums/",
            name: "ForumViews",
            component: ForumViews,
        },
    ]
})

export default router 