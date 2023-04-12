import { createApp } from 'vue'
import App from './App.vue'
import store from './store/store.js'
import axios from 'axios'
import router from './router/index.js'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {faBookmark } from '@fortawesome/free-solid-svg-icons'
import '@/plugins/accessibility.js'

const app = createApp(App)
app.use(router)

const myAxios = axios.create({
    baseURL: 'https://team22-22.bham.team'
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

library.add(faBookmark)
createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(store).use(router,axios).mount('#app')