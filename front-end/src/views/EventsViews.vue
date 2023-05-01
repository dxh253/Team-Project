<template>
  <div class="container">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <h1 class="title">Looking For Something To Do? Or Study pals?</h1>
        <p class="subtitle">Here are some upcoming events!</p>
      </div>
    </section>

    <div class="columns">
      <div class="column is-3">
        <h2 class="title">Upcoming Events</h2>
      </div>
      <div class="field column is-3" style="">
        <div class="control">
          <input v-model="searchText" class="input" type="text" placeholder="Search" />
        </div>
      </div>
      <div class="select field column is-3 is-narrow">
        <select v-model="categoryFilter">
          <option value="0">Events and study groups</option>
          <option value="1">Events only</option>
          <option value="2">Study groups only</option>
        </select>
      </div>
      <div class="column is-1">
        <button class="button is-primary is-light" @click="filterEvents">
          My Events
        </button>
      </div>
      <div class="column is-1">
        <router-link to="/events_form" tabindex="-1">
          <button class="button is-primary is-light" tabindex="0" style="">Add Event</button>
        </router-link>
      </div>
    </div>

    <div class="columns is-multiline">
      <EventBox v-for="event in filteredEvents" v-bind:key="event.id" v-bind:event="event" />
    </div>
  </div>
</template>

<style scoped>
.field:not(:last-child) {
  margin-bottom: 0;
}

.select select::-ms-expand {
    display: none;
}
.select select {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="10" height="6"><path fill="gray" d="M0 0l5 4.998L10 0z"/></svg>');
    background-repeat: no-repeat;
    background-position: right .7em top 50%, 0 0;
    background-size: 10px 6px, 100%;
    padding-right: 2.5em;
}

/* .select:not(.is-multiple) {
  height: 100px;
} */
</style>

<script>
import { getAPI } from "@/plugins/axios";
import EventBox from "@/components/EventBox";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";

export default {
  name: "EventsViews",
  data() {
    return {
      searchText: "",
      categoryFilter: "0",
      allEvents: [],
      displayedEvents: [],
      filterByOwner: false,
    };
  },
  components: {
    EventBox,
  },
  async created() {
    console.log("created method is executed");
    if (!this.$store.getters.loggedIn) {
      // User is not logged in
      return;
    }

    getAPI
      .get("/api/v1/events/", {
        headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
      })
      .then((response) => {
        console.log("API response data:", response.data);
        this.allEvents = response.data;
        this.displayedEvents = response.data;
        this.$store.state.APIData = response.data;
      })
      .catch((error) => {
        console.log("API error:", error);
      });
  },
  methods: {
    filterEvents() {
      if (this.filterByOwner) {
        this.displayedEvents = this.allEvents;
        this.filterByOwner = false;
      } else {
        const userId = jwt_decode(this.$store.state.accessToken).user_id;
        const filteredEvents = this.allEvents.filter((event) => {
          return event.owner === userId;
        });
        this.displayedEvents = filteredEvents;
        this.filterByOwner = true;
      }
    },
    fuzzyMatch(searchText, textToMatch) {
      // Checks that all characters in `searchText` appear in the same order
      // in `textToMatch`
      // e.g. `prty` will match `party` but not `piracy` or `try please`
      searchText = searchText.toLowerCase();
      textToMatch = textToMatch.toLowerCase();
      let charIndex = 0;
      for (const c of textToMatch) {
        if (c == searchText[charIndex]) ++charIndex;
      }
      return charIndex == searchText.length;
    },
  },
  computed: {
    computed: mapState(["APIData"]),
    filteredEvents: function () {
      let result = this.displayedEvents;

      // First filter events by category
      result = result.filter(
        (event) =>
          (this.categoryFilter == 0) | (event.category == this.categoryFilter)
      );

      // Then by search string
      result = result.filter((event) =>
        this.fuzzyMatch(this.searchText, event.name)
      );

      return result;
    },
  },
};
</script>

