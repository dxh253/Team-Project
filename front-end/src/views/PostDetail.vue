<template>
    <div class="post-detail">
      <h2>{{ post.title }}</h2>
      <p>{{ post.content }}</p>
      <hr>
      <h3>Comments:</h3>
      <ul>
        <li v-for="comment in post.comments" :key="comment.id">
          {{ comment.text }}
        </li>
      </ul>
      <textarea v-model="newCommentText"></textarea>
      <button @click="addComment">Add Comment</button>
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex';
  import { getAPI } from '@/plugins/axios';
  
  export default {
    name: 'PostDetail',
    data() {
      return {
        newCommentText: '',
      };
    },
    computed: {
      ...mapState(['APIData']),
    // post() {
    //     const slug = this.$route.params.slug;
    //     return this.$store.dispatch('getPostBySlug', slug);
    //     },
        post() {
            const slug = this.$route.params.slug;
            // const posts = this.$store.state.APIData;
            const posts = this.$store.dispatch('getPostBySlug', slug);
            return posts.then(response => response.data.find(post => post.slug === slug));
        },
    },
    methods: {
      addComment() {
        const token = localStorage.getItem('access');
        const postId = this.$route.params.id;
        const data = { text: this.newCommentText };
  
        getAPI.post(`/posts/${postId}/comments/`, data, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
            // Add the new comment to the post in the store
            const postIndex = this.$store.state.APIData.findIndex(post => post.id === postId);
            const post = this.$store.state.APIData[postIndex];
            post.comments.push(response.data);
            this.$store.commit('setAPIData', this.$store.state.APIData);
            
            // Clear the input field
            this.newCommentText = '';
            })
        .catch((error) => {
          console.log(error);
        });
      },
    },
  };
  </script>
  