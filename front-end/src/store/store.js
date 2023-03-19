import { createStore } from 'vuex'
import { getAPI } from '@/plugins/axios'

export default createStore({
  state() {
    return {
      accessToken: localStorage.getItem('access'),
      refreshToken: localStorage.getItem('refresh'),
      APIData: ''
    }
  },
  mutations: {
    updateStorage(state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
      localStorage.setItem('access', access)
      localStorage.setItem('refresh', refresh)
    },
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
    }
  },
    getters: {
      loggedIn(state) {
        return state.accessToken !== null
      }

    },

  actions: {
    async userLogin(context, userCredentials) {
        const response = await getAPI.post('/api-token/', {
          username: userCredentials.username,
          password: userCredentials.password
        })
        context.commit('updateStorage', {
          access: response.data.access,
          refresh: response.data.refresh,
        })
        return response
    },

  userLogout(context){
    if(context.getters.loggedIn){
      context.commit('destroyToken')
    }
  }
}

// state: {
//   accessToken: null,
//   refreshToken: null,
// },
// mutations: {
//   updateStorage(state, { access, refresh }) {
//     state.accessToken = access
//     state.refreshToken = refresh
//   },
// },
// actions: {
//   userLogin (context, userCredentials) {
//     return new Promise((resolve) => {
//       getAPI.post('/api-token/',{
//         username: userCredentials.username,
//         password: userCredentials.password
//       })
//       .then(response => {
//         context.commit('updateStorage', {
//           access: response.data.access,
//           refresh: response.data.refresh,
//         })
//         resolve(response)
//       })
//     })
//   }
// }

})
