<template>
  <div class="container mt-6 has-text-centered">
    <div class="columns is-multiline">
      <div class="column is-4">
        <div class="image-wrapper">
          <figure>
            <img :src="events.get_image" alt="" style="max-width: 30%; max-height: 30%;" />
          </figure>
        </div>
      </div>
      <div class="column is-8">
        <div class="box">
          <h1 class="title">{{ events.name }}</h1>
          <p>{{ eventIdToName() }}</p>
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
          <hr />
          <div class="description">
            <h2 class="subtitle is-4">Description</h2>
            <p>{{ events.description }}</p>
          </div>
          <hr />

          <div v-if="isOwner" class="dropdown is-hoverable">
            <div class="dropdown-trigger">
              <button class="button is-small" aria-haspopup="true" aria-controls="dropdown-menu">
                <span>Options</span>
                <span class="icon is-small">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu" role="menu">
              <div class="dropdown-content">
                <a href="#" class="dropdown-item" @click="showEditForm">
                  <span class="icon">
                    <i class="fas fa-edit"></i>
                  </span>
                  <span>Edit Event</span>
                </a>
                <a href="#" class="dropdown-item" @click="deleteEvents">
                  <span class="icon">
                    <i class="fas fa-trash-alt"></i>
                  </span>
                  <span>Delete Event</span>
                </a>
              </div>
            </div>
          </div>
          <div v-if="showForm" class="container mt-6 has-text-centered">
            <div class="columns is-centered">
              <div class="column is-half">
                <form>
                  <div class="field">
                    <label class="label">Name</label>
                    <div class="control">
                      <input class="input" type="text" v-model="updatedName" />
                    </div>
                  </div>
                  <div class="field">
                    <label class="label">Venue</label>
                    <div class="control">
                      <input class="input" type="text" v-model="updatedVenue" />
                    </div>
                  </div>
                  <div class="field">
                    <label class="label">Description</label>
                    <div class="control">
                      <textarea class="textarea" v-model="updatedDescription"></textarea>
                    </div>
                  </div>
                  <div class="field">
                    <label class="label">Date</label>
                    <div class="control">
                      <input class="input" type="date" v-model="updatedDate" />
                    </div>
                  </div>
                  <div class="field">
                    <div class="control">
                      <button class="button is-primary" type="submit" @click.prevent="updateEvents">
                        Save Changes
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { getAPI } from "@/plugins/axios";
import jwt_decode from "jwt-decode";

export default {
  name: "EventsDetail",
  data() {
    return {
      events: {},
      editEvents: false,
      name: "",
      venue: "",
      description: "",
      date: "",
      showForm: false,
      isOwner: false,
    };
  },
  mounted() {
    this.getEvents();
  },
  methods: {
    getEvents() {
      const category_slug = this.$route.params.category_slug;
      const events_slug = this.$route.params.events_slug;
      const token = this.$store.state.accessToken;
      const decodedToken = jwt_decode(token);
      const userId = decodedToken.user_id;

      axios;
      getAPI
        .get(`api/v1/events/${category_slug}/${events_slug}/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.events = response.data;
          // Check if the user is the owner of the event
          if (this.events.owner === userId) {
            this.isOwner = true;
          }
          console.log("user:", this.$store.state.user);
          console.log("event owner:", this.events.owner);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteEvents() {
      const category_slug = this.$route.params.category_slug;
      const events_slug = this.$route.params.events_slug;

      axios;
      getAPI
        .delete(`/api/v1/events/${category_slug}/${events_slug}/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          // Redirect the user to the /events page
          window.location.href = "/events";
        })
        .catch((error) => {
          if (error.response.status === 403) {
            alert("You are not authorized to delete this event.");
          } else {
            console.log(error);
          }
        });
    },
    toggleEditEvents() {
      this.editEvents = !this.editEvents;
      this.name = this.events.name;
      this.venue = this.events.venue;
      this.description = this.events.description;
      this.date = this.events.date;
    },
    updateEvents() {
      this.submitEditEvents();
    },
    eventIdToName() {
      const categories = ["Event", "Study group"];
      return categories[this.events.category - 1];
    },
    submitEditEvents() {
      const category_slug = this.$route.params.category_slug;
      const events_slug = this.$route.params.events_slug;

      axios;
      getAPI
        .put(
          `/api/v1/events/${category_slug}/${events_slug}/`,
          {
            name: this.updatedName,
            venue: this.updatedVenue,
            description: this.updatedDescription,
            date: this.updatedDate,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.editEvents = false;
          this.getEvents();
          this.showEditForm();
        })
        .catch((error) => {
          if (error.response.status === 403) {
            alert("You are not authorized to delete this event.");
          } else {
            console.log(error);
          }
        });
    },
    showEditForm() {
      this.showForm = !this.showForm;
    },
  },
};
</script>
