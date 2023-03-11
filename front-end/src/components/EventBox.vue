<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img :src="events.get_thumbnail">
            </figure>

            <h3 class="is-size-4">{{ events.name }}</h3>
            <p class="is-size-6 has-text-grey">{{ events.date }}</p>

            <router-link :to="events.get_absolute_url" class="button is-dark mt-4">View details</router-link>
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
</style>
