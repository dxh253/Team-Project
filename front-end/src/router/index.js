import { createRouter, createWebHistory} from "vue-router";
import jwtDecode from "jwt-decode";
import Login from "../views/Login.vue"
import RegisterForm from "../views/RegisterForm.vue"
import EventsView from "../views/EventsViews.vue"
import EventsDetail from "../views/EventsDetail.vue"
import EventsForm from "../views/EventsForm.vue"
import Dashboard from "../views/DashBoard.vue"
import PrivacyPolicy from "../views/PrivacyPolicy.vue"
import PostCreate from "../views/PostCreate.vue"
import EditPost from "../views/EditPost.vue"
import HelpSection from "../views/HelpSection.vue"
import ProblemsDetail from "../views/ProblemsDetail.vue"


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
                requiresLogin: true
            }

        },
        {
            path: "/edit-post/:id/",
            name: "edit-post",
            component: EditPost,
            meta: {
              requiresLogin: true
            }
        },
        {
            path: '/posts/:id/edit',
            name: 'edit-post',
            component: EditPost,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: "/posts/",
            name: "Posts",
            component: () => import("../views/PostsList.vue"),
            meta: {
                requiresLogin: true
            }
        },
        {
            path: "/create/",
            name: "create",
            component: PostCreate,
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
            path: "/posts/:slug/",
            name: "post-detail",
            // component: () => import("../views/PostDetail.vue")
        },
        {
            path: "/privacy_policy/",
            name: "PrivacyPolicy",
            component: PrivacyPolicy,

        },
        {
            path: "/help/",
            name: "HelpSection",
            component: HelpSection,
            meta: {
                requiresLogin: true
            }

        },
        {
            path: "/help/:problem_id/",
            name: "ProblemsDetail",
            component: ProblemsDetail,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: "/dashboard/",
            name: "Dashboard",
            component: Dashboard,
            meta: {
                requiresLogin: true
            }
        }
    ]
});


router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem("access") !== null;
    const requiresLogin = to.matched.some((record) => record.meta.requiresLogin);
    const token = localStorage.getItem("access");
  
    if (to.name === "Login" && to.query.sessionExpired) {
      // If already on login page with sessionExpired prop, don't redirect again
      return next();
    }
  
    if (loggedIn && token) {
      const decodedToken = jwtDecode(token);
      const currentTime = Date.now() / 1000;
  
      // If token is expired, redirect to login page with sessionExpired prop set to true
      if (currentTime > decodedToken.exp) {
        localStorage.removeItem("access");
        return next({ name: "Login", query: { sessionExpired: true } });
      }
  
      // If already logged in, redirect to dashboard
      if (to.name === "Login") {
        return next({ name: "Dashboard" });
      }
    }
  
    if (requiresLogin && !loggedIn) {
      next({ name: "Login" });
    } else {
      next();
    }
  });
  
  
export default router 