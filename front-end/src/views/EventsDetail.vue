<template>
    <div class="page-events">
         <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="events.get_image">
                </figure>

                <h1 class="title">{{ events.name }}</h1>

                <p>{{ events.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>
                <p><strong>Venue: </strong>{{ events.venue }}</p>
                <p><strong>Date: </strong>{{ events.date }}</p>

            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    name: 'EventsDetail',
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
                .get(`/api/v1/events/${category_slug}/${events_slug}/`)
                .then(response => {
                    this.events = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    
    }
}
</script>