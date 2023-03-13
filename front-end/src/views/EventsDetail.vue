<template>
    <div class="container mt-6 has-text-centered">
      <div class="columns is-multiline">
        <div class="column is-4">
          <div class="image-wrapper">
            <figure class="image is-cropped is-256x256">
              <img :src="events.get_image" alt="" style="object-fit: cover; width: 100%; height: 100%;">
            </figure>
          </div>
        </div>
        <div class="column is-8">
          <div class="box">
            <h1 class="title">{{ events.name }}</h1>
            <div class="event-details">
              <div class="event-detail">
                <h2 class="subtitle is-4">Venue</h2>
                <p>{{ events.venue }}</p>
              </div>
              <div class="event-detail">
                <h2 class="subtitle is-4">Date</h2>
                <p>{{ events.date }}</p>
              </div>
            </div>
            <hr>
            <div class="description">
              <h2 class="subtitle is-4">Description</h2>
              <p>{{ events.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  
    
  


<script>
import axios from 'axios'
import { getAPI } from '@/plugins/axios';
export default {
    name: 'EventsDetail',
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
                getAPI.get(`/events/${category_slug}/${events_slug}/`)
                .then(response => {
                    this.events = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    
    }
}
</script>