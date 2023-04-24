<template>
  <div>
    <div class="main2">
      <!--- <img src="@/assets/background-.png" style="display: block; width: 100px; height: 100px;"> -->
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Events'" to="/events" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="far fa-calendar" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Events and Study group
        </router-link>
      </div>
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Discussions'" to="/posts" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fas fa-file-alt" style="display: block;  font-size: 100px; color: #7B57AA;"> </i> Resources and Discussions
        </router-link>
      </div>
      <!--
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Resources'" to="/resources" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fas fa-file-alt" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Resources
        </router-link>
      </div>
       
     <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Study group'" to="/study-group" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fas fa-users" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Study group
        </router-link>
      </div>
         -->
      <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Help'" to="/help" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="fa fa-question-circle" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Help
        </router-link>
      </div>
      <!-- <div class="event-card" style="background-color: #c5aaf0;">
        <router-link v-a11y-link="'Savedfile'" to="/Savedfile/" style="color: white; font-size: 30px; font-weight: bold; font-family: 'Times New Roman', sans-serif;">
          <i class="far fa-calendar" style="display: block;  font-size: 100px; color: #7B57AA;"></i> Saved File
        </router-link>
      </div> --> 
      <div class="your-events">
        <h3>
    <i class="fa-solid fa-bookmark"></i> SAVED EVENTS:
  </h3>
      <ul>
        <li v-for="event in userEvents" :key="event.id">
          <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link" v-if="event.event.category === 1"  >
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-calendar event-icon"></i> {{ event.event.name }}
          </router-link>
        </li>
      </ul>
    </div>
    <div class="your-studyg">
      <h3>
    <i class="fa-solid fa-bookmark"></i> SAVED STUDY GROUP:
  </h3>
      <ul>
        <!-- <li v-for="event in userEvents" :key="event.id">
          <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link" v-if="event.event.category === 2">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-users event-icon"></i> {{ event.event.name }}
</router-link>
        </li> --> 

        <li v-for="event in userEvents" :key="event.id">
          <router-link :to="'' + event.event.get_absolute_url" v-a11y-link="event.event.name" class="event-link" v-if="event.event.category === 2">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-users event-icon"></i> {{ event.event.name }}
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
          //this.userEvents = response.data;
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




<style>
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



</style>

<style>
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



</style>

<style>
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

/* Style the icon */
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











</style>