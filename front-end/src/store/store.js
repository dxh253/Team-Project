import { createStore } from 'vuex'
import { getAPI } from '@/plugins/axios'
import jwtDecode from "jwt-decode";
import router from '@/router/index.js'

export default createStore({
  state() {
    return {
      // Retrieve the access and refresh tokens from local storage, or set them to null if not present
      accessToken: localStorage.getItem('access') || null,
      // refreshToken: localStorage.getItem('refresh') || null,
      APIData: ''
    }
  },
  mutations: {
    // Update the state and local storage with the new access and refresh tokens
    updateStorage(state, { access,
      //  refresh
       }) {
    state.accessToken = access
    // state.refreshToken = refresh
    localStorage.setItem('access', access)
    // localStorage.setItem('refresh', refresh)
  },
    // Clear the access and refresh tokens from the state and local storage
    destroyToken(state) {
      state.accessToken = null
      // state.refreshToken = null
      localStorage.removeItem('access')
      // localStorage.removeItem('refresh')
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
    postById: (state) => (postId) => {
      return state.APIData.find(post => post.id === postId)
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
      })
      context.dispatch("waitForTokenExpiration");
      return response
    },
    
    // Clear the access and refresh tokens from the state and local storage
    userLogout(context) {
      context.commit("destroyToken");
      router.push({ name: "Home", query: { sessionExpired: true } });
    },    

    async waitForTokenExpiration(context) {
      const token = context.state.accessToken;
      if (token) {
        const decodedToken = jwtDecode(token);
        const currentTime = Date.now() / 1000;
        const expiresIn = (decodedToken.exp - currentTime) * 1000;
        await new Promise((resolve) => setTimeout(resolve, expiresIn));
        if (context.state.accessToken === token) {
          context.dispatch("userLogout");
        }
      }
    },

    async getPostBySlug(context, slug) {
      const response = await getAPI.get(`/posts/?slug=${slug}`)
      return response.data
    },
    
  },
})