import { createStore } from 'vuex'
import { getAPI } from '@/plugins/axios'

export default createStore({
  state() {
    return {
      // Retrieve the access and refresh tokens from local storage, or set them to null if not present
      accessToken: localStorage.getItem('access') || null,
      refreshToken: localStorage.getItem('refresh') || null,
      tokenExpiration: localStorage.getItem('expiration') || null,
      APIData: ''
    }
  },
  mutations: {
    // Update the state and local storage with the new access and refresh tokens
    updateStorage(state, { access, refresh, expiration }) {
    state.accessToken = access
    state.refreshToken = refresh
    state.tokenExpiration = expiration
    localStorage.setItem('access', access)
    localStorage.setItem('refresh', refresh)
    localStorage.setItem('expiration', expiration)
  },
    // Clear the access and refresh tokens from the state and local storage
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
    },
    setAPIData(state, data) {
      console.log('setting APIData:', data);
      state.APIData = data;
    },
  },
  getters: {
    // Check if the user is logged in based on the presence of the access token
    loggedIn(state) {
      return state.accessToken !== null
    },
    events(state) {
      console.log('getting APIData:', state.APIData);
      return state.APIData
    },
  },
  actions: {
    // Call the API to log in the user with the provided credentials, and update the state and local storage with the new tokens
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

    async refreshAccessToken(context) {
    const response = await getAPI.post('/api/token/refresh/', {
      refresh: context.state.refreshToken
    })
    context.commit('updateStorage', {
      access: response.data.access,
      refresh: context.state.refreshToken, // Keep the same refresh token
      expiration: response.data.expires_in // Set the new expiration time
    })
    return response
  },
    // Clear the access and refresh tokens from the state and local storage
    userLogout(context) {
      context.commit('destroyToken')
    },
  },
})