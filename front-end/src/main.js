// import './plugins/axios'
// import { createApp } from 'vue'
// import App from './App.vue'
// import store from './store/store.js'
// import axios from 'axios'
// import router from './router/index.js'
// import Vue from 'vue'


// Vue.config.productionTip = false
// router.beforeEach((to, from, next) => {
//     if(to.matched.some(record => record.meta.requiresLogin)) {
//         if (!store.getters.loggedIn) {
//             next({name: 'Login'})
//             return
//         } else {
//             next()
//         }
//     } else{
//         next()
//     }
// })


// axios.defaults.baseURL = 'http://127.0.0.1:8000'

// createApp(App).use(store).use(router,axios).mount('#app')

import { createApp } from 'vue'
import App from './App.vue'
import store from './store/store.js'
import axios from 'axios'
import router from './router/index.js'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'




const app = createApp(App)
app.use(router)

const myAxios = axios.create({
    baseURL: 'http://127.0.0.1:8000'
})

app.config.globalProperties.$axios = myAxios
app.use(store)

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresLogin)) {
        if (!store.getters.loggedIn) {
            next({ name: 'Login' })
            return
        } else {
            next()
        }
    } else {
        next()
    }
})

// app.mount('#app')

createApp(App).use(store).use(router,axios).mount('#app').component('font-awesome-icon', FontAwesomeIcon)