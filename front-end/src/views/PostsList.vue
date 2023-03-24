<template>
  <div>
    <h2>Posts</h2>
    <div v-for="post in allposts" :key="post.id">
      <post-box :post="post" />
      <vote :post-id="post.id" :initial-score="post.score"></vote>
    </div>
  </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';
import PostBox from '../components/PostBox.vue';
import { mapState } from 'vuex';
import Vote from '../components/Vote.vue';

export default {
  name: 'PostsList',
  components: {
    'post-box': PostBox,
    Vote
  },
  data() {
    return {
      allposts: [],
    }
  },
  computed: mapState(['APIData']),
  created() {
    getAPI.get('/allposts/')
      .then(response => {
        console.log("Post API has received data")
        this.allposts = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>
