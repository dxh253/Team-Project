import { createStore } from 'vuex'
import { getAPI } from '@/plugins/axios'

export default createStore({
  state() {
    return {
      accessToken: localStorage.getItem('access'),
      refreshToken: localStorage.getItem('refresh'),
      posts: []
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
    },
    setPosts(state, posts) {
      state.posts = posts
    },
    addPost(state, post) {
      state.posts.push(post)
    }
  },
  getters: {
    loggedIn(state) {
      return state.accessToken !== null
    },
    posts(state) {
      return state.posts
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
    },
    async fetchPosts(context) {
      const response = await getAPI.get('/posts/')
      context.commit('setPosts', response.data)
    },
    async createPost(context, post) {
      const response = await getAPI.post('/posts/', post)
      context.commit('addPost', response.data)
      return response.data
    }
  }
})
