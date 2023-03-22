<script setup>
import { RouterView } from "vue-router";
</script>

<template>
  <div id ="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>UoB Forum</strong></router-link>
      
      
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="/events" class="navbar-item">Events</router-link>
          <router-link to="" class="navbar-item">Discussion</router-link>
          
      <div class="navbar-item">
        <div class="buttons">
          <router-link v-if="!accessToken" to="/login" class="button is-success">Log in</router-link>
          <button v-if="accessToken" @click="logout" class="button is-success">Log out</button>
        </div>
      </div>
        </div>
      </div>

    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2023</p>
    </footer>
  </div>
  
</template>

<style lang="scss">
  @import '../node_modules/bulma/bulma.sass'
</style>


  <script>
  import { mapState } from 'vuex'
  export default {
    computed: mapState(['accessToken']),

    methods: {
      logout() {
        this.$store.dispatch('userLogout')
        this.$router.push('/')
      },
    },
  }
  </script>
