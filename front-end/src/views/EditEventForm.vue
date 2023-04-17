<template>
    <div class="container mt-6">
      <div class="columns">
        <div class="column is-half is-offset-one-quarter">
          <form @submit.prevent="submitForm">
            <div class="field">
              <label class="label">Name</label>
              <div class="control">
                <input class="input" type="text" v-model="events.name">
              </div>
            </div>
            <div class="field">
              <label class="label">Venue</label>
              <div class="control">
                <input class="input" type="text" v-model="events.venue">
              </div>
            </div>
            <div class="field">
              <label class="label">Date</label>
              <div class="control">
                <input class="input" type="date" v-model="events.date">
              </div>
            </div>
            <div class="field">
              <label class="label">Description</label>
              <div class="control">
                <textarea class="textarea" v-model="events.description"></textarea>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-primary" type="submit">Save</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import { getAPI } from '@/plugins/axios';
  
  export default {
    name: 'EditEventForm',
    data() {
      return {
        events: {}
      }
    },
    mounted() {
      this.getEvents()
    },
    methods: {
      getEvents() {
        const category_slug = this.$route.params.category_slug
        const events_slug = this.$route.params.events_slug
  
        axios
          getAPI.get(`api/v1/events/${category_slug}/${events_slug}/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => {
            this.events = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      submitForm() {
        const category_slug = this.$route.params.category_slug
        const events_slug = this.$route.params.events_slug
  
        axios
          getAPI.put(`api/v1/events/${category_slug}/${events_slug}/`, this.events, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => {
            // Redirect the user to the events detail page
            this.$router.push({ name: 'EventsDetail', params: { category_slug, events_slug } })
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
  </script>
