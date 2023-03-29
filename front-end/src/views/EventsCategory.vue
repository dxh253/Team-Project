<template>
    <div class="home">
      <section class="hero is-medium is-dark mb-6">
            <div class="hero-body has-text-centered">
              <h1 class="title">
                Looking For Something To Do?
              </h1>
              <p class="subtitle">
                  Here are some upcoming events!
              </p>
            </div>
          
      </section>
  
      <div class="columns">
        <div class="column is-10 ">
          <h2 class="title">Party Events</h2>
        </div>
        <div class="column is-4 is-offset 8">
          <router-link to="/events_form">
            <button class="button is-primary is-light">Add Event</button>
          </router-link>
        </div>
      </div>
    
    
      <div class="columns is-multiline">
        <EventBox
            v-for="events in category.events"
            v-bind:key="events.id"
            v-bind:events="events"
          />
      </div>
    </div>
  </template>

<script>
import EventBox from '@/components/EventBox';
import { getAPI } from '@/plugins/axios';

export default{
    name : 'EventsCategory',
    components: {
        EventBox,
    },
    data(){
        return{
            category: {
                events: []
            }
        }
    },
    mounted(){
        this.getCategory()
    },
    methods: {
        getCategory(){
            const category_slug = this.$route.params.category_slug
            getAPI.get(`api/v1/events/${category_slug}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
            .then(response => {
                this.category = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
