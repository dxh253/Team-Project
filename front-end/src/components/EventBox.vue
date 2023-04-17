<template>
  <div class="column is-3">
    <div class="box">
      <figure class="image mb-4">
        <img :src="event.get_thumbnail" class="event-thumbnail" alt="event image">
      </figure>
      <h3 class="is-size-4">{{ event.name }}</h3>
      <p class="is-size-6 has-text-grey">{{ event.date }}</p>
      <router-link :to="event.get_absolute_url" class="button is-dark mt-4">View details</router-link>
      <span class="icon is-large is-clickable" @click="saveEvent(event.id)">
        <font-awesome-icon class="right" icon="bookmark" />
      </span>
    </div>
  </div>
</template>
<script>
import { getAPI } from '@/plugins/axios';
import { notyf } from '@/plugins/notyf';

export default {
  name: 'EventBox',
  props: ['event'],
  methods: {
    async saveEvent(eventId) {
      try {
        const token = localStorage.getItem('access');
        const headers = {
          Authorization: `Bearer ${token}`,
        };

        const data = {
          event_id: eventId,
        };

        const response = await getAPI.post('/api/v1/save-event/', data, { headers });

        if (response.status === 201) {
          notyf.success('Event saved to your profile.');
        } else if (response.status === 200) {
          notyf.success('You have removed this item from your saved list');
        } else {
          notyf.error('Error saving the event.');
        }
      } catch (error) {
        console.error('Error saving event:', error);
        alert('Error saving the event. Please try again.');
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
