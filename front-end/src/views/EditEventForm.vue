<!-- <template>
    <div>
      <h1>Edit Event</h1>
      <form @submit.prevent="handleSubmit">
        <div>
          <label>Name:</label>
          <input type="text" v-model="form.name" required>
        </div>
        <div>
          <label>Description:</label>
          <textarea v-model="form.description"></textarea>
        </div>
        <div>
          <label>Venue:</label>
          <textarea v-model="form.venue"></textarea>
        </div>
        <div>
          <label>Date:</label>
          <input type="date" v-model="form.date" required>
        </div>
        <button type="submit">Save Changes</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          name: '',
          description: '',
          venue: '',
          date: '',
        },
        categorySlug: '', // add the category slug here
        eventsSlug: '', // add the events slug here
      };
    },
    created() {
      // fetch the event data and populate the form fields
      this.fetchEvent();
    },
    methods: {
      async fetchEvent() {
        try {
          const response = await fetch(`/api/v1/events/${this.categorySlug}/${this.eventsSlug}/`);
          const data = await response.json();
          this.form = {
            name: data.name,
            description: data.description,
            venue: data.venue,
            date: data.date,
          };
        } catch (error) {
          console.log(error);
        }
      },
      async handleSubmit() {
        try {
          const response = await fetch(`/api/v1/events/${this.categorySlug}/${this.eventsSlug}/`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${localStorage.getItem('access_token')}`,
            },
            body: JSON.stringify(this.form),
          });
          const data = await response.json();
          // do something with the response data, e.g. redirect to the event detail page
        } catch (error) {
          console.log(error);
        }
      },
    },
  };
  </script> -->

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
  