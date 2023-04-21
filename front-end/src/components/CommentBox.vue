<template>
    <div class="comment-box">
      <div v-if="loading">Loading comments...</div>
      <div v-else>
        <div v-if="comments.length === 0">No comments yet.</div>
        <div v-else>
          <div v-for="comment in comments" :key="comment.id" class="comment">
            <h3>{{ comment.owner }}</h3>
            <p>{{ comment.text }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  
  
  
  <script>
  import { getAPI } from '@/plugins/axios';
  
  export default {
    name: 'CommentBox',
    props: {
      postId: {
        type: Number,
        required: true,
      },
      token: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        loading: false,
        comments: [],
      };
    },
    watch: {
      postId(newVal, oldVal) {
        if (newVal !== oldVal && this.token) {
          this.fetchComments();
        }
      },
      token(newVal, oldVal) {
        if (newVal !== oldVal && this.postId) {
          this.fetchComments();
        }
      },
    },
    methods: {
        async fetchComments() {
        try {
            this.loading = true;
            const response = await getAPI.get(`/posts/${this.postId}/comments/`, {
            headers: {
                Authorization: `Bearer ${this.token}`,
            },
            });
            console.log('Comments API has received data');
            console.log('hi');
            console.log(response); // add this line to log the response
            this.comments = response.data;
            console.log('Fetched comments:', this.comments);
            
        } catch (error) {
            console.log(error);
            return Promise.reject(error);
        } finally {
            this.loading = false;
        }
        },
    },
  };
  </script>
  