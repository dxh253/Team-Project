<!-- <template>
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
</style> -->

<!-- <template>
  <div class="column is-3">
      <notification
      ref="notification"
      :message="notificationMessage"
      :type="notificationType"
      :duration="3000"
    ></notification>
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
import Notification from '@/components/Notification';

export default {
  name: 'EventBox',
  components: {
    Notification,
  },
  props: ['event'],
    data() {
      return {
        notificationMessage: '',
        notificationType: '',
      };
  },
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
          this.notificationMessage = 'Event saved to your profile.';
          this.notificationType = 'is-success';
        } else if (response.status === 200) {
          this.notificationMessage = 'You have removed this item from your saved list';
          this.notificationType = 'is-info';
        } else {
          this.notificationMessage = 'Error saving the event.';
          this.notificationType = 'is-danger';
        }
        this.$refs.notification.showNotification();
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
</style> -->


<template>
  <div class="column is-3">
    <notification ref="notification" :message="notificationMessage" :type="notificationType" :duration="3000">
    </notification>
    <div class="box">
      <figure class="image mb-4">
        <img :src="event.get_thumbnail" class="event-thumbnail" alt="event image">
      </figure>
      <h3 class="is-size-4">{{ event.name }}</h3>
      <p class="is-size-6 has-text-grey">{{ event.date }}</p>
      <router-link :to="event.get_absolute_url" class="button is-dark mt-4">View details</router-link>
      <span class="icon is-large is-clickable" @click="saveEvent(event.id)" @keydown.enter="saveEvent(event.id)" tabindex="0">
        <span v-if="!isSaved">
          <font-awesome-icon class="right" :icon="['far', 'bookmark']" />
        </span>
        <span v-else>
          <font-awesome-icon class="right" icon="bookmark" />
        </span>
      </span>
    </div>
  </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';
import Notification from '@/components/Notification';

export default {
  name: 'EventBox',
  components: {
    Notification,
  },
  props: ['event'],
  data() {
    return {
      notificationMessage: '',
      notificationType: '',
      isSaved: this.event.isSaved || false,
    };
  },
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
          this.notificationMessage = 'Event saved to your profile.';
          this.notificationType = 'is-success';
          this.isSaved = true;
        } else if (response.status === 200) {
          this.notificationMessage = 'You have removed this item from your saved list';
          this.notificationType = 'is-info';
          this.isSaved = false;
        } else {
          this.notificationMessage = 'Error saving the event.';
          this.notificationType = 'is-danger';
        }
        this.$refs.notification.showNotification();
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
.icon-overlay {
  position: relative;
}

.bookmark-icon {
  position: absolute;
}

.times-icon {
  position: absolute;
}
</style>
