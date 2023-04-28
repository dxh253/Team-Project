<!-- <template>
  <div>
    <div class="main2">
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Events'" to="/events"
          style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="far fa-calendar" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Events and Study
          group
        </router-link>
      </div>
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Discussions'" to="/posts"
          style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fas fa-file-alt" style="display: block;  font-size: 100px; color: #7B57AA;"> </i> Resources and
          Discussions
        </router-link>
      </div>
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Help'" to="/help"
          style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fa fa-question-circle" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Help
        </router-link>
      </div>
      <div class="your-events">
        <h3>
          <i class="fa-solid fa-bookmark"></i> SAVED EVENTS:
        </h3>
        <ul>
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
              v-if="event.event.category === 1">
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-calendar event-icon"></i> {{
                event.event.name }}
            </router-link>
          </li>
        </ul>
      </div>
      <div class="your-studyg">
        <h3>
          <i class="fa-solid fa-bookmark"></i> SAVED STUDY GROUP:
        </h3>
        <ul>
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
              v-if="event.event.category === 2">
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-users event-icon"></i> {{ event.event.name
              }}
            </router-link>
          </li>
        </ul>
      </div>
      <div class="upcoming">
        <h3>
          <i class="fa-sharp fa-solid fa-arrow-up-from-bracket"></i> UPCOMING:
        </h3>
        <ul>
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link">
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa-sharp fa-solid fa-clock event-icon"></i>
              <span class="event-name">{{ event.event.name }}</span>
              <span class="event-reminder">{{ getReminder(event.event.date) }}</span>
            </router-link>
          </li>

        </ul>
      </div>
    </div>
  </div>
</template>
<script>


import { getAPI } from '@/plugins/axios'

export default {
  name: 'DashBoard',
  data() {
    return {
      userEvents: []
    };
  },
  created() {
    this.getUserEvents();
  },

  methods: {
    getUserEvents() {
      getAPI.get('/api/v1/saved-events/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
        .then(response => {
          this.userEvents = response.data.sort((b, a) => {
            return new Date(a.event.date) - new Date(b.event.date);
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    getReminder(eventDate) {
      const m = 24 * 60 * 60 * 1000;
      const a = new Date();
      const t = new Date(eventDate).getTime();
      const r = t - m;
      const d = r - a.getTime();
      const dd = Math.abs(Math.floor(d / m));
      return `${dd} day${dd > 1 ? 's' : ''} left`;
    }
  }
};
</script> 


<style scoped>
.your-events {
  text-align: justify;
  background-color: #d4bbf4;
  padding: 20px;
  margin-top: 60px;
  font-size: 23px;
  color: rgb(0, 0, 0);
  font-weight: bold;
  font-family: 'Times New Roman'
}

.your-studyg {
  text-align: justify;
  background-color: #d4bbf4;
  padding: 20px;
  margin-top: 60px;
  font-size: 23px;
  color: rgb(0, 0, 0);
  font-weight: Bold;
  font-family: 'Times New Roman'
}

.upcoming {
  text-align: justify;
  background-color: #d4bbf4;
  padding: 20px;
  margin-top: 60px;
  font-size: 23px;
  color: rgb(0, 0, 0);
  font-weight: Bold;
  font-family: 'Times New Roman'
}

.event-link {
  color: grey;
  font-size: 18px;
  font-family: 'Monospace'
}

.event-icon {
  color: #7B57AA;
}

.event-item {
  margin-bottom: 10px;
  list-style: none;
}

.event-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
}

.event-icon {
  margin-right: 10px;
  font-size: 20px;
}

.event-name {
  flex-grow: 1;
}

.event-reminder {
  margin-left: 10px;
  font-weight: 400;
  font-size: 14px;
  color: #888;
}
</style> -->

<!-- 
<template>
  <div>
    <div class="main2">
      <div class="event-card has-background-purple">
        <router-link v-a11y-link="'Events'" to="/events"
          class="has-text-white is-size-3 has-text-weight-bold has-text-centered">
          <i class="far fa-calendar is-block  fa-5x has-text-primary"></i> Events and Study
          group
        </router-link>
      </div>
      <div class="event-card has-background-purple">
        <router-link v-a11y-link="'Discussions'" to="/posts"
          class="has-text-white is-size-3 has-text-weight-bold has-text-centered">
          <i class="fas fa-file-alt is-block fa-5x has-text-primary"> </i> Resources and
          Discussions
        </router-link>
      </div>
      <div class="event-card has-background-purple">
        <router-link v-a11y-link="'Help'" to="/help"
          class="has-text-white is-size-3 has-text-weight-bold has-text-centered">
          <i class="fa fa-question-circle is-block fa-5x has-text-primary"></i> Help
        </router-link>
      </div>
      <div class="your-events">
        <h3 class="title is-3 has-text-weight-bold">
          <i class="fas fa-bookmark has-text-purple"></i> SAVED EVENTS:
        </h3>
        <ul class="has-text-weight-bold">
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
              v-if="event.event.category === 1">
              <i class="far fa-calendar event-icon has-text-primary"></i> {{ event.event.name }}
            </router-link>
          </li>
        </ul>
      </div>
      <div class="your-studyg">
        <h3 class="title is-3 has-text-weight-bold">
          <i class="fas fa-bookmark has-text-purple"></i> SAVED STUDY GROUP:
        </h3>
        <ul class="has-text-weight-bold">
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
              v-if="event.event.category === 2">
              <i class="fas fa-users event-icon has-text-primary"></i> {{ event.event.name }}
            </router-link>
          </li>
        </ul>
      </div>
      <div class="upcoming">
        <h3 class="title is-3 has-text-weight-bold">
          <i class="fas fa-arrow-up-from-bracket has-text-purple"></i> UPCOMING:
        </h3>
        <ul class="has-text-weight-bold">
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link">
              <i class="fas fa-clock event-icon has-text-primary"></i>
              <span class="event-name">{{ event.event.name }}</span>
              <span class="event-reminder">{{ getReminder(event.event.date) }}</span>
            </router-link>
          </li>
    </ul>
  </div>
</div>
  </div>
</template>

<script>
import { getAPI } from '@/plugins/axios'

export default {
  name: 'DashBoard',
  data() {
    return {
      userEvents: []
    };
  },
  created() {
    this.getUserEvents();
  },
  methods: {
    getUserEvents() {
      getAPI.get('/api/v1/saved-events/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
        .then(response => {
          this.userEvents = response.data.sort((b, a) => {
            return new Date(a.event.date) - new Date(b.event.date);
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    getReminder(eventDate) {
      const m = 24 * 60 * 60 * 1000;
      const a = new Date();
      const t = new Date(eventDate).getTime();
      const r = t - m;
      const d = r - a.getTime();
      const dd = Math.abs(Math.floor(d / m));
      return `${dd} day${dd > 1 ? 's' : ''} left`;
    }
  }
};
</script> -->


<!-- <template>
  <div class="container">
    <div class="columns">
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Events'" to="/events"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="far fa-calendar is-block  fa-5x has-text-white"></i> Events and Study
            group
          </router-link>
        </div>
      </div>
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Discussions'" to="/posts"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="fas fa-file-alt is-block fa-5x has-text-white"> </i> Resources and
            Discussions
          </router-link>
        </div>
      </div>
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Help'" to="/help"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="fa fa-question-circle is-block fa-5x has-text-white"></i> Help
          </router-link>
        </div>
      </div>
    </div>

    <div class="columns">
      <div class="column is-half">
        <h3 class="title is-3 has-text-weight-bold">
          <i class="fas fa-bookmark has-text-primary"></i> SAVED EVENTS:
        </h3>
        <ul class="has-text-weight-bold">
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
              v-if="event.event.category === 1">
              <i class="far fa-calendar event-icon has-text-primary"></i> {{ event.event.name }}
            </router-link>
          </li>
        </ul>
      </div>
      <div class="column is-half">
        <h3 class="title is-3 has-text-weight-bold">
          <i class="fas fa-bookmark has-text-primary"></i> SAVED STUDY GROUP:
        </h3>
        <ul class="has-text-weight-bold">
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
              v-if="event.event.category === 2">
              <i class="fas fa-users event-icon has-text-primary"></i> {{ event.event.name }}
            </router-link>
          </li>
        </ul>
      </div>
    </div>

    <div class="upcoming">
      <h3 class="title is-3 has-text-weight-bold">
        <i class="fas fa-arrow-up-from-bracket has-text-primary"></i> UPCOMING:
      </h3>
      <ul class="has-text-weight-bold">
        <li v-for="event in userEvents" :key="event.id">
          <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link">
            <i
            class="fas fa-clock event-icon has-text-primary"></i>
        <span class="event-name">{{ event.event.name }}</span>
        <span class="event-reminder">{{ getReminder(event.event.date) }}</span>
      </router-link>
    </li>
  </ul>
</div>

  </div>
</template>


<script>
import { getAPI } from '@/plugins/axios'

export default {
  name: 'DashBoard',
  data() {
    return {
      userEvents: []
    };
  },
  created() {
    this.getUserEvents();
  },
  methods: {
    getUserEvents() {
      getAPI.get('/api/v1/saved-events/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
        .then(response => {
          this.userEvents = response.data.sort((b, a) => {
            return new Date(a.event.date) - new Date(b.event.date);
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    getReminder(eventDate) {
      const m = 24 * 60 * 60 * 1000;
      const a = new Date();
      const t = new Date(eventDate).getTime();
      const r = t - m;
      const d = r - a.getTime();
      const dd = Math.abs(Math.floor(d / m));
      return `${dd} day${dd > 1 ? 's' : ''} left`;
    }
  }
};
</script>
<style scoped>
.event-card {
  border-radius: 0.25rem;
  margin-bottom: 1.5rem;
}

.event-icon {
  margin-right: 0.5rem;
}

.event-name {
  font-weight: bold;
}
.event-link {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}
.event-reminder {
  margin-left: auto;
}
</style> -->


<!-- <template>
  <div class="container">
    <div class="columns">
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Events'" to="/events"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="far fa-calendar is-block  fa-5x has-text-white"></i> Events and Study
            group
          </router-link>
        </div>
      </div>
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Discussions'" to="/posts"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="fas fa-file-alt is-block fa-5x has-text-white"> </i> Resources and
            Discussions
          </router-link>
        </div>
      </div>
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Help'" to="/help"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="fa fa-question-circle is-block fa-5x has-text-white"></i> Help
          </router-link>
        </div>
      </div>
    </div>

    <div class="columns">
      <div class="column is-half">
        <div class="box">
          <h3 class="title is-3 has-text-weight-bold">
            <i class="fas fa-bookmark has-text-primary"></i> SAVED EVENTS:
          </h3>
          <ul class="has-text-weight-bold">
            <li v-for="event in userEvents" :key="event.id">
              <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
                v-if="event.event.category === 1">
                <i class="far fa-calendar event-icon has-text-primary"></i> {{ event.event.name }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
      <div class="column is-half">
        <div class="box">
          <h3 class="title is-3 has-text-weight-bold">
            <i class="fas fa-bookmark has-text-primary"></i> SAVED STUDY GROUP:
          </h3>
          <ul class="has-text-weight-bold">
            <li v-for="event in userEvents" :key="event.id">
              <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
                v-if="event.event.category === 2">
                <i class="fas fa-users event-icon has-text-primary"></i> {{ event.event.name }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="box">
      <h3 class="title is-3 has-text-weight-bold">
        <i class="fas fa-arrow-up-from-bracket has-text-primary"></i> UPCOMING:
      </h3>
      <ul class="has-text-weight-bold">
        <li v-for="event in userEvents" :key="event.id">
          <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link">
            <i class="fas fa-clock event-icon has-text-primary"></i>
            <span class="event-name">{{ event.event.name }}</span>
            <span class="event-reminder">{{ getReminder(event.event.date) }}</span>
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { getAPI } from '@/plugins/axios'

export default {
  name: 'DashBoard',
  data() {
    return {
      userEvents: []
    };
  },
  created() {
    this.getUserEvents();
  },
  methods: {
    getUserEvents() {
      getAPI.get('/api/v1/saved-events/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
        .then(response => {
          this.userEvents = response.data.sort((b, a) => {
            return new Date(a.event.date) - new Date(b.event.date);
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    getReminder(eventDate) {
      const m = 24 * 60 * 60 * 1000;
      const a = new Date();
      const t = new Date(eventDate).getTime();
      const r = t - m;
      const d = r - a.getTime();
      const dd = Math.abs(Math.floor(d / m));
      return `${dd} day${dd > 1 ? 's' : ''} left`;
    }
  }
};
</script>

<style scoped>
.event-card {
  border-radius: 0.25rem;
  margin-bottom: 1.5rem;
}

.event-icon {
  margin-right: 0.5rem;
}

.event-name {
  font-weight: bold;
}
.event-link {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}
.event-reminder {
  margin-left: auto;
}
</style> -->


<!-- <template>
  <div class="container">
    <div class="columns">
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Events'" to="/events"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="far fa-calendar is-block  fa-5x has-text-white"></i> Events and Study
            group
          </router-link>
        </div>
      </div>
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Discussions'" to="/posts"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="fas fa-file-alt is-block fa-5x has-text-white"> </i> Resources and
            Discussions
          </router-link>
        </div>
      </div>
      <div class="column is-4">
        <div class="card event-card has-background-primary">
          <router-link v-a11y-link="'Help'" to="/help"
            class="card-content has-text-white is-size-3 has-text-weight-bold has-text-centered">
            <i class="fa fa-question-circle is-block fa-5x has-text-white"></i> Help
          </router-link>
        </div>
      </div>
    </div>

    <div class="columns">
      <div class="column is-half">
        <div class="box">
          <h3 class="title is-3 has-text-weight-bold">
            <i class="fas fa-bookmark has-text-primary"></i> SAVED EVENTS:
          </h3>
          <ul class="has-text-weight-bold">
            <li v-for="event in userEvents" :key="event.id">
              <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
                v-if="event.event.category === 1">
                <i class="far fa-calendar event-icon has-text-primary"></i> {{ event.event.name }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
      <div class="column is-half">
        <div class="box">
          <h3 class="title is-3 has-text-weight-bold">
            <i class="fas fa-bookmark has-text-primary"></i> SAVED STUDY GROUP:
          </h3>
          <ul class="has-text-weight-bold">
            <li v-for="event in userEvents" :key="event.id">
              <router-link :to="event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link" v-if="event.event.category === 2">
              <i class="fas fa-users event-icon has-text-primary"></i> {{ event.event.name }}
              </router-link>
            </li>
          </ul>
        </div>
    </div>
      </div>
      <div class="box">
        <h3 class="title is-3 has-text-weight-bold">
          <i class="fas fa-arrow-up-from-bracket has-text-primary"></i> UPCOMING:
        </h3>
        <ul class="has-text-weight-bold">
          <li v-for="event in userEvents" :key="event.id">
            <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link">
              <i class="fas fa-clock event-icon has-text-primary"></i>
              <span class="event-name">{{ event.event.name }}</span>
              <span class="event-reminder">{{ getReminder(event.event.date) }}</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>

</template>
<script>
import { getAPI } from '@/plugins/axios'

export default {
  name: 'DashBoard',
  data() {
    return {
      userEvents: []
    };
  },
  created() {
    this.getUserEvents();
  },
  methods: {
    getUserEvents() {
      getAPI.get('/api/v1/saved-events/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
        .then(response => {
          this.userEvents = response.data.sort((b, a) => {
            return new Date(a.event.date) - new Date(b.event.date);
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    getReminder(eventDate) {
      const m = 24 * 60 * 60 * 1000;
      const a = new Date();
      const t = new Date(eventDate).getTime();
      const r = t - m;
      const d = r - a.getTime();
      const dd = Math.abs(Math.floor(d / m));
      return `${dd} day${dd > 1 ? 's' : ''} left`;
    }
  }
};
</script>
<style scoped>
.event-card {
  border-radius: 0.25rem;
  margin-bottom: 1.5rem;
}

.event-icon {
  margin-right: 0.5rem;
}

.event-name {
  font-weight: bold;
}
.event-link {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}
.event-reminder {
  margin-left: auto;
}

.columns {
  display: flex;
  flex-wrap: wrap;
}

.box {
  height: 300px;
  overflow-y: auto;
}
</style> -->

<template>
  <div class="container">
    <section class="hero is-medium is-dark mb-6 is-fullwidth" style="padding: 0 20px;">
      <div class="has-text-centered">
        <h1 class="title" style="margin-top:90px;">Welcome to BrumConnect</h1>
        <p class="subtitle">Connect with other students in The University of Birmingham, get involved.</p>
      </div>
      <div class="columns is-multiline is-mobile">
        <div class="column is-full-mobile">
          <button class="button is-primary event-card is-small is-fullwidth" style="height: 150px;" tabindex="-1">
            <router-link v-a11y-link="'Events'" to="/events"
              class="card-content has-text-white is-size-5 has-text-weight-bold has-text-centered is-flex is-flex-direction-column is-align-items-center is-justify-content-center"
              style="width: 100%;">
              <div class="is-flex is-align-items-center is-justify-content-center">
                <i class="far fa-calendar is-block fa-3x has-text-white is-hidden-mobile"></i>
              </div>
              <div style="margin-top: 0.5rem;">
                Events and Study
              </div>
            </router-link>
          </button>
        </div>
        <div class="column is-full-mobile">
          <button class="button is-primary event-card is-small is-fullwidth" style="height: 150px;" tabindex="-1">
            <router-link v-a11y-link="'Discussions'" to="/posts"
              class="card-content has-text-white is-size-5 has-text-weight-bold has-text-centered is-flex is-flex-direction-column is-align-items-center is-justify-content-center"
              style="width: 100%;">
              <div class="is-flex is-align-items-center is-justify-content-center">
                <i class="fas fa-file-alt is-block fa-3x has-text-white is-hidden-mobile"></i>
              </div>
              <div style="margin-top: 0.5rem;">
                Discussions
              </div>
            </router-link>
          </button>
        </div>
        <div class="column is-full-mobile">
          <button class="button is-primary event-card is-small is-fullwidth" style="height: 150px;" tabindex="-1">
            <router-link v-a11y-link="'Help'" to="/help"
              class="card-content has-text-white is-size-5 has-text-weight-bold has-text-centered is-flex is-flex-direction-column is-align-items-center is-justify-content-center"
              style="width: 100%;">
              <div class="is-flex is-align-items-center is-justify-content-center">
                <i class="fa fa-question-circle is-block fa-3x has-text-white is-hidden-mobile"></i>
              </div>
              <div style="margin-top: 0.5rem;">
                Help
              </div>
            </router-link>
          </button>
        </div>
      </div>
    </section>




    <div class="columns">
      <div class="column is-one-third">
        <div class="box">
          <h3 class="title is-3 has-text-weight-bold">
            <i class="fas fa-bookmark has-text-primary"></i> SAVED EVENTS:
          </h3>
          <ul class="has-text-weight-bold">
            <li v-for="event in userEvents" :key="event.id">
              <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
                v-if="event.event.category === 1">
                <i class="far fa-calendar event-icon has-text-primary"></i> {{ event.event.name }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
      <div class="column is-one-third">
        <div class="box">
          <h3 class="title is-3 has-text-weight-bold">
            <i class="fas fa-bookmark has-text-primary"></i> SAVED STUDY GROUP:
          </h3>
          <ul class="has-text-weight-bold">
            <li v-for="event in userEvents" :key="event.id">
              <router-link :to="event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link"
                v-if="event.event.category === 2">
                <i class="fas fa-users event-icon has-text-primary"></i> {{ event.event.name }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
      <div class="column is-one-third">
        <div class="box">
          <h3 class="title is-3 has-text-weight-bold">
            <i class="fas fa-arrow-up-from-bracket has-text-primary"></i> UPCOMING:
          </h3>
          <ul class="has-text-weight-bold">
            <li v-for="event in userEvents" :key="event.id">
              <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link">
                <i class="fas fa-clock event-icon has-text-primary"></i>
                <span class="event-name">{{ event.event.name }}</span>
                <span class="event-reminder">{{ getReminder(event.event.date) }}</span>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getAPI } from '@/plugins/axios'

export default {
  name: 'DashBoard',
  data() {
    return {
      userEvents: []
    };
  },
  created() {
    this.getUserEvents();
  },
  methods: {
    getUserEvents() {
      getAPI.get('/api/v1/saved-events/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
        .then(response => {
          this.userEvents = response.data.sort((a, b) => {
            return new Date(a.event.date) - new Date(b.event.date);
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    getReminder(eventDate) {
      const m = 24 * 60 * 60 * 1000;
      const a = new Date();
      const t = new Date(eventDate).getTime();
      const r = t - m;
      const d = r - a.getTime();
      const dd = Math.abs(Math.floor(d / m));
      return `${dd} day${dd > 1 ? 's' : ''} left`;
    }
  }
};
</script>

<style scoped>
.event-card {
  border-radius: 0.25rem;
  margin-bottom: 3.5rem;
}

.event-card .card-content {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
}

.event-link {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
  color: #3273dc;
}

.event-link:hover {
  text-decoration: underline;
}

.event-icon {
  margin-right: 0.5rem;
}

.event-name {
  font-weight: bold;
  margin-left: 0.5rem;
}

.event-reminder {
  margin-left: auto;
}

.box {
  height: 300px;
  overflow-y: auto;
  margin-bottom: 2rem;
}

.box .title {
  font-weight: bold;
  color: #3273dc;
}

.box ul {
  margin-top: 1.5rem;
}

.box ul li {
  margin-bottom: 0.5rem;
}

.box ul li:last-child {
  margin-bottom: 0;
}

.columns{
  margin-top: 0rem;
}


@media screen and (max-width: 768px) {
  .event-card {
    height: 100px;
    font-size: 1rem;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
  }

  .event-card .card-content {
    font-size: 1rem;
  }

  .event-link {
    margin-bottom: 0;
  }

  .event-icon {
    display: none;
  }

  .box {
    height: auto;
  }
}
</style>

