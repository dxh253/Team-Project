import { createApp } from 'vue'
import App from './App.vue'
import store from './store/store.js'
import axios from 'axios'
import router from './router/index.js'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {faBookmark } from '@fortawesome/free-solid-svg-icons'

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

// app.mount('#app')
library.add(faBookmark)
createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(store).use(router,axios).mount('#app')


// import { createApp } from 'vue'
// import App from './App.vue'
// import store from './store/store.js'
// import axios from 'axios'
// import router from './router/index.js'
// import { library } from '@fortawesome/fontawesome-svg-core'
// import { faSave } from   '@fortawesome/free-solid-svg-icons'
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
//
// // Add the Font Awesome icon to the library
// library.add(faSave)
//
// const app = createApp(App)
//
// // Register the Font Awesome component globally
// app.component('font-awesome-icon', FontAwesomeIcon)
//
// // Use the router and axios plugins
// app.use(router)
// app.use(axios)
//
// // Set the base URL for axios
// const myAxios = axios.create({
//   baseURL: 'https://team22-22.bham.team'
// })
// app.config.globalProperties.$axios = myAxios
//
// // Use the Vuex store
// app.use(store)
//
// // Set up the route guards
// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresLogin)) {
//     if (!store.getters.loggedIn) {
//       next({ name: 'Login' })
//       return
//     } else {
//       next()
//     }
//   } else {
//     next()
//   }
// })
//
// // Mount the app to the DOM
// //app.mount('#app')
// createApp(App).use(store).use(router,axios).mount('#app')