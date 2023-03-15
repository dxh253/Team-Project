
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
        <h2 class="title">Upcoming Events</h2>
      </div>
      <div class="column is-4 is-offset 8">
        <router-link to="/events_form">
          <button class="button is-primary is-light">Add Event</button>
        </router-link>
      </div>
  </div>
  <div class="columns is-multiline">
    <EventBox
        v-for="events in allEvents"
        v-bind:key="events.id"
        v-bind:events="events"
      />
  </div>
  </div>
</template>

<script>
  import { getAPI } from '@/plugins/axios';
  import EventBox from '@/components/EventBox';
  import {mapState} from 'vuex';

  export default{
    name: 'EventsViews',
    data(){
      return {
        allEvents: []
      }
    },
      components: {
        EventBox
      }, 
      computed: mapState(['APIData']),
      created(){
        getAPI.get('api/v1/events/')
        .then(response => {
          console.log("Post API has received data")
          this.allEvents = response.data
        })
        .catch(error => {
          console.log(error)
        })
      }
    }


</script>