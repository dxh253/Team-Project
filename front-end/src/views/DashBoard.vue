<template>
    <div class="main2">
        <div class="event-card">
            <router-link to="/events">Events</router-link>

        </div>
        <div class="event-card">
            <router-link to="/discussions">Discussions</router-link>
        </div>
        <div class="event-card">
            <router-link to="/resources">Resources</router-link>
        </div>
        <div class="event-card">
            <router-link to="/study-group">Study group</router-link>
        </div>
        <div class="event-card">
            <router-link to="/help">Help</router-link>
        </div>
    </div>
</template>

<script>
  export default {
      name: 'DashBoard',
      data(){

      }
  }

</script>