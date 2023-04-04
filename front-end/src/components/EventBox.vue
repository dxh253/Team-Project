<!-- <template>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <div class="column is-3">
    <div class="box">
      <figure class="image mb-4">
        <img :src="events.get_thumbnail" class="event-thumbnail">
      </figure>

      <h3 class="is-size-4">{{ events.name }}</h3>
      <p class="is-size-6 has-text-grey">{{ events.date }}</p>

      <router-link :to="events.get_absolute_url" class="button is-dark mt-4">View details</router-link>

      <span class="icon is-large is-clickable" @click="saveEvent">
          <font-awesome-icon class="right" icon="fa-solid fa-bookmark" />
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EventBox',
  props: {
    events: Object
  }
}
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}

.event-thumbnail {
  width: 150px;
  height: 150px;
}

</style> -->


<template>
  <div class="column is-3">
    <div class="box">
      <figure class="image mb-4">
        <img :src="event.get_thumbnail" class="event-thumbnail" alt="event image">
      </figure>
      <h3 class="is-size-4">{{ event.name }}</h3>
      <p class="is-size-6 has-text-grey">{{ event.date }}</p>
      <router-link :to="event.get_absolute_url" class="button is-dark mt-4">View details</router-link>
      <span class="icon is-large is-clickable" @click="saveEvent">
        <font-awesome-icon class="right" icon="bookmark" />
      </span>
    </div>
  </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';

export default {
  name: 'EventBox',
  props: {
    event: {
      type: Object,
      required: true,
    },
  },
  methods: {
    async saveEvent() {
      if (!this.$store.getters.loggedIn) {
        console.log('User not logged in');
        return;
      }

      const formData = new FormData();
      formData.append('event', this.event.id);
      formData.append('name', this.event.name);
      formData.append('date', this.event.date);
      formData.append('category', this.event.category);

      try {
        await getAPI.post('/api/v1/save_event/', formData, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        });
      console.log('Event saved');
      } catch (error) {
      console.log('Failed to save event:', error);
      }
    },
  },
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}

.event-thumbnail {
  width: 150px;
  height: 150px;
}

</style>
