<template>
  <div>
    <div class="main2">
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Events'" to="/events" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="far fa-calendar" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Events
        </router-link>
      </div>
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Discussions'" to="/posts" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fab fa-rocketchat" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Discussions
        </router-link>
      </div>
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Resources'" to="/resources" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fas fa-file-alt" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Resources
        </router-link>
      </div>
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Study group'" to="/study-group" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fas fa-users" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Study group
        </router-link>
      </div>
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Help'" to="/help" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fa fa-question-circle" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Help
        </router-link>
      </div>
    </div>
    <div class="your-events">
      <h3>SAVED EVENTS:</h3>
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
    margin-top: 60px;
    font-size: 23px;
    color: rgb(0, 0, 0);
    font-weight: bold;
    font-family: 'Times New Roman'
    

  }
  

  
  </style>