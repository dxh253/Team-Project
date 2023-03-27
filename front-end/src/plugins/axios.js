// "use strict";

// import Vue from 'vue';
// import axios from "axios";

// // Full config:  https://github.com/axios/axios#request-config
// // axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
// // axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// // axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// let config = {
//   // baseURL: process.env.baseURL || process.env.apiUrl || ""
//   // timeout: 60 * 1000, // Timeout
//   // withCredentials: true, // Check cross-site Access-Control
// };

// const _axios = axios.create(config);

// _axios.interceptors.request.use(
//   function(config) {
//     // Do something before request is sent
//     return config;
//   },
//   function(error) {
//     // Do something with request error
//     return Promise.reject(error);
//   }
// );

// // Add a response interceptor
// _axios.interceptors.response.use(
//   function(response) {
//     // Do something with response data
//     return response;
//   },
//   function(error) {
//     // Do something with response error
//     return Promise.reject(error);
//   }
// );

// Plugin.install = function(Vue) {
//   Vue.axios = _axios;
//   window.axios = _axios;
//   Object.defineProperties(Vue.prototype, {
//     axios: {
//       get() {
//         return _axios;
//       }
//     },
//     $axios: {
//       get() {
//         return _axios;
//       }
//     },
//   });
// };

// Vue.use(Plugin)

// export default Plugin;

// team22-22.bham.team/register


// import axios from "axios";

// const getAPI = axios.create({
//     baseURL: "http://127.0.0.1:8000",
//     timeout: 1000,
// })

// export {getAPI}

// import axios from "axios";

// const getAPI = axios.create({
//     baseURL: "https://team22-22.bham.team",
//     // baseURL: "http://127.0.0.1:8000",
//     // timeout: 1000,
// })

import axios from 'axios';

    const getCsrfToken = () => {
    let csrfToken = null;
    const csrfTokenCookie = document.cookie.match('(^|;)\\s*csrftoken\\s*=\\s*([^;]+)');
    if (csrfTokenCookie) {
        csrfToken = csrfTokenCookie.pop();
    } else {
        // Generate new CSRF token
        csrfToken = Math.random().toString(36).slice(-12);
        document.cookie = `csrftoken=${csrfToken}; path=/; SameSite=Strict`;
    }
    return csrfToken;
    };

    const getAPI = axios.create({
    baseURL: 'https://team22-22.bham.team',
    headers: {
        'X-CSRFToken': getCsrfToken(),
        'Content-Type': 'application/json',
        Accept: 'application/json',
    },
    });

export default getAPI;
