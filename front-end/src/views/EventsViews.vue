<!-- 
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
        <button class="button is-primary is-light">Add Event</button>
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
</template> -->

<!-- <script> -->
  // import { getAPI } from '@/plugins/axios';
  // import EventBox from '@/components/EventBox';
  // import {mapState} from 'vuex';


  // export default{
  //   name: 'EventsViews',
  //   data(){
  //     return {
  //       allEvents: []
  //     }
  //   },
  //     components: {
  //       EventBox
  //     }, 
  //     computed: mapState(['APIData']),
  //     created(){
  //       getAPI.get('/events/', {headers:{Authorization: `Bearer ${this.$store.state.accessToken}`}})
  //       .then(response => {
  //         console.log("Post API has received data")
  //         this.allEvents = response.data
  //       })
  //       .catch(error => {
  //         console.log(error)
  //       })
  //     }
  //   }


<!-- </script> -->

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
        <button class="button is-primary is-light">Add Event</button>
      </div>
    </div>
    <div class="columns is-multiline">
      <EventBox v-for="events in allEvents" v-bind:key="events.id" v-bind:events="events" />
    </div>
  </div>
</template>

<!-- <script> -->
// import { getAPI } from '@/plugins/axios';
// import EventBox from '@/components/EventBox';
// import { mapState } from 'vuex';

// export default {
//   name: 'EventsViews',
//   data() {
//     return {
//       allEvents: [],
//     };
//   },
//   components: {
//     EventBox,
//   },
//   computed: mapState(['APIData']),
//   created() {
//     getAPI
//       .get('/events/', {
//         headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
//       })
//       .then((response) => {
//         console.log('Post API has received data');
//         this.allEvents = response.data;
//       })
//       .catch((error) => {
//         console.log(error);
//       });
//   },
// };
<!-- </script> -->

<script>
import { getAPI } from '@/plugins/axios';
import EventBox from '@/components/EventBox';
// import axios from 'axios';
// const BASE_URL = 'https://team22-22.bham.team/';

export default {
    name: 'EventsView',
    data(){
        return{
            allEvents: []
        }
    },
    components: {
        EventBox
    },
    created() {
    getAPI
      .post('/api-token/', {
        username: 'abc',
        password: 'abc',
      })
      .then((response) => {
        console.log('Token API has received data');
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  },
}   
</script>