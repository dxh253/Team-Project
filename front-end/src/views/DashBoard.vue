<template>

    <div>
      <div class="main2">
        <div class="event-card">
          <router-link to="/events">Events</router-link>
        </div>
        <div class="event-card">
          <router-link to="/discussions">Discussions</router-link>
        </div>
        <div class="event-card">
          <router-link to="/resources">Resources</router-link>
        </div>
        <div class="event-card">
          <router-link to="/study-group">Study group</router-link>
        </div>
        <div class="event-card">
          <router-link to="/help">Help</router-link>
        </div>
      </div>
      <div class="your-events">
        <h3>Your saved events:</h3>
        <ul>
            <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url">
            {{ event.event.name }}
            </router-link>
            </li>
        </ul>


      </div>
    </div>
  </template>
  
  <script>
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