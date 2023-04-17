import { createRouter, createWebHistory} from "vue-router";
// import {VueRouter} from "vue-router";
import Login from "../views/Login.vue"
import RegisterForm from "../views/RegisterForm.vue"
import EventsView from "../views/EventsViews.vue"
import EventsDetail from "../views/EventsDetail.vue"
import EventsForm from "../views/EventsForm.vue"
import PrivacyPolicy from "../views/PrivacyPolicy.vue"
import PostCreate from "../views/PostCreate.vue"
import PostThread from "../views/PostThread.vue"

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
        },
        {
            path: "/posts/:slug/",
            name: "post-detail",
            component: () => import("../views/PostDetail.vue")
        },
        {
            path: "/create/",
            name: "create",
            component: PostCreate
        },

        {
            path: "/thread/",
            name: "thread",
            component: PostThread
        }
        
    ]
})

export default router 