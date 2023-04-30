<script setup>
import { RouterView } from "vue-router";
</script>

<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/dashboard" class="navbar-item"><strong>BrumConnect</strong></router-link>


        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="/events" class="navbar-item">Events</router-link>
          <router-link to="/posts" class="navbar-item">Discussion</router-link>
          <router-link to="/help" class="navbar-item">Help</router-link>
          <Accessibility />

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
      <router-view />
    </section>

    <footer class="footer">
      <p>Alpha Project Disclaimer: This server is provided by the School of Computer Science at the University of
        Birmingham to allow users to provide feedback on software developed by students as part of an assignment. While we
        take reasonable precautions, we cannot guarantee the security of the data entered into the system. Do NOT enter
        any real personal data (e.g. financial information or otherwise) into the system. The assignment runs until May
        31st 2023, at which time the server and all associated data will be destroyed.</p>
      <p class="has-text-centered">Copyright (c) 2023</p>
    </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma/bulma.sass';
</style>


<script>
import { mapState } from 'vuex';
import Accessibility from '@/components/AccessibilityPage.vue';

export default {
  data() {
    return {
      showMobileMenu: false,
    }
  },
  mounted() {
    document.title = "BrumConnect"; // Change the title here
  },
  computed: mapState(['accessToken']),
  components: {
    Accessibility
  },
  methods: {
    logout() {
      this.$store.dispatch('userLogout');
      this.$router.push('/');
    },
  },
}
</script>
