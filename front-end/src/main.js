// import { createApp } from 'vue'
// import App from './App.vue'
// import store from './store/store.js'
// import axios from 'axios'
// import router from './router/index.js'
// import { library } from '@fortawesome/fontawesome-svg-core'
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// import {faBookmark } from '@fortawesome/free-solid-svg-icons'
// import '@fortawesome/fontawesome-free/css/all.css'
// import '@/plugins/accessibility.js'

// const app = createApp(App)
// app.use(router)

// const myAxios = axios.create({
//     baseURL: 'https://team22-22.bham.team'
// })

// app.config.globalProperties.$axios = myAxios
// app.use(store)

// router.beforeEach((to, from, next) => {
//     if (to.matched.some(record => record.meta.requiresLogin)) {
//         if (!store.getters.loggedIn) {
//             next({ name: 'Login' })
//             return
//         } else {
//             next()
//         }
//     } else {
//         next()
//     }
// })

// library.add(faBookmark)
// createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(store).use(router,axios).mount('#app')

import { createApp } from 'vue';
import App from './App.vue';
import store from './store/store.js';
import axios from 'axios';
import router from './router/index.js';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faBookmark } from '@fortawesome/free-solid-svg-icons';
import { faBookmark as farBookmark } from '@fortawesome/free-regular-svg-icons'; // Add this line
import '@fortawesome/fontawesome-free/css/all.css';
import '@/plugins/accessibility.js';

const app = createApp(App);
app.use(router);

const myAxios = axios.create({
  baseURL: 'https://team22-22.bham.team',
});

app.config.globalProperties.$axios = myAxios;
app.use(store);

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'Login' });
      return;
    } else {
      next();
    }
  } else {
    next();
  }
});

library.add(faBookmark, farBookmark); // Update this line to include farBookmark
createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(store).use(router, axios).mount('#app');
