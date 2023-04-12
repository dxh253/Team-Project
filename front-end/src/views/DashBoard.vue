<template>
  <div>
    <div class="main2">
      <div class="event-card">
        <router-link v-a11y-link="'Events'" to="/events">Events</router-link>
      </div>
      <div class="event-card">
        <router-link v-a11y-link="'Discussions'" to="/discussions">Discussions</router-link>
      </div>
      <div class="event-card">
        <router-link v-a11y-link="'Resources'" to="/resources">Resources</router-link>
      </div>
      <div class="event-card">
        <router-link v-a11y-link="'Study group'" to="/study-group">Study group</router-link>
      </div>
      <div class="event-card">
        <router-link v-a11y-link="'Help'" to="/help">Help</router-link>
      </div>
    </div>
    <div class="your-events">
      <h3>Your saved events:</h3>
      <ul>
        <li v-for="event in userEvents" :key="event.id">
          <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name">
            {{ event.event.name }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>
  
  <script>
  // import Vue from 'vue';
  import { getAPI } from '@/plugins/axios'
  
  export default {
    name: 'DashBoard',
    data() {
      return {
        userEvents: []
      };
    },
    created() {
      this.getUserEvents();
    },
    methods: {
      getUserEvents() {
        getAPI.get('/api/v1/saved-events/', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access')}`
          }
        })
          .then(response => {
            this.userEvents = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
    }
  };
  </script>
  
  <style>
  .your-events {
    margin-top: 20px;
  }
  </style>