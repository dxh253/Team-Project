<!-- <template>
  <div v-if="loading">
    Loading...
  </div>
  <div v-else-if="post" class="post-background">
    <div class="post-container">
      <h2>{{ post.title }}</h2>
      <p class="post-box-description">{{ post.description }}</p>
      <a :href="post.get_image" target="_blank"><img :src="post.get_image"
          :style="{ filter: blur ? 'blur(10px)' : 'none' }" @click="enlargeImage"></a>
      <span class="post-box-time-since">posted {{ post.time_since_post }}</span>
      <hr>
      <h3>Comments</h3>
      <div class="comment-container">
        <form>
          <input type="text" v-model="newCommentText" placeholder="Add a comment...">
          <button @click="addComment">Add Comment</button>
        </form>
        <p>Placeholder for comments...</p>
      </div>
    </div>
  </div>
  <div v-else>
    Error fetching post. Please try again later.
  </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';

export default {
  name: 'PostDetail',
  data() {
    return {
      post: undefined,
      loading: false,
      newCommentText: '',
    };
  },
  async created() {
    try {
      this.loading = true; // set loading to true before calling fetchPost
      await this.fetchPost();
    } catch (error) {
      console.log(error);
      this.post = null;
    } finally {
      this.loading = false;
    }
  },

  watch: {
    $route() {
      this.fetchPost();
    },
  },
  methods: {
    async fetchPost() {
      const token = localStorage.getItem('access');
      console.log('this.$route:', this.$route);
      console.log('this.$route.params:', this.$route.params);
      const postId = this.$route.params.id || localStorage.getItem('postId');

      console.log('API endpoint:', getAPI.defaults.baseURL);
      console.log('postSlug:', postId);

      if (postId) {
        this.loading = true;

        try {
          const response = await getAPI.get(`/posts/${postId}/`, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          console.log('Post API has received data');
          this.post = response.data;
          localStorage.setItem('postId', postId); // store postId in local storage
        } catch (error) {
          console.log(error);
          this.error = error;
          return Promise.reject(error);
        } finally {
          this.loading = false;
        }
      }
    },
  },
};
</script> -->

<template>
  <div v-if="loading">
    Loading...
  </div>
  <div v-else-if="post" class="post-background">
    <div class="post-container">
      <h2>{{ post.title }}</h2>
      <p class="post-box-description">{{ post.description }}</p>
      <a :href="post.get_image" target="_blank"><img :src="post.get_image"
          :style="{ filter: blur ? 'blur(10px)' : 'none' }"></a>
      <span class="post-box-time-since">posted {{ post.time_since_post }}</span>
      <hr>
      <h3>Comments</h3>
      <div class="comment-container">
        <form @submit.prevent="addComment">
          <input type="text" v-model="newCommentText" placeholder="Add a comment...">
          <button>Add Comment</button>
        </form>
        <div v-for="comment in post.comments" :key="comment.id" class="comment-box">
          <p class="comment-text">{{ comment.text }}</p>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    Error fetching post. Please try again later.
  </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';

export default {
  name: 'PostDetail',
  data() {
    return {
      post: undefined,
      loading: false,
      newCommentText: '',
    };
  },
  async created() {
    console.log("This is the created hook: ", this.$route.params);
    try {
      this.loading = true; // set loading to true before calling fetchPost
      await this.fetchPost();
    } catch (error) {
      console.log(error);
      this.post = null;
    } finally {
      this.loading = false;
    }
  },

  watch: {
    $route() {
      this.fetchPost();
    },
  },
  methods: {
    async fetchPost() {
      const token = localStorage.getItem('access');
      const post_slug = this.$route.params.slug || localStorage.getItem('post_slug');

      console.log('API endpoint:', getAPI.defaults.baseURL);
      console.log('postSlug:', post_slug);

      if (post_slug) {
        this.loading = true;

        try {
          const response = await getAPI.get(`/posts/${post_slug}/`, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          console.log('Post API has received data');
          this.post = response.data;
          localStorage.setItem('post_slug', post_slug); // store post_slug in local storage
        } catch (error) {
          console.log(error);
          this.error = error;
          return Promise.reject(error);
        } finally {
          this.loading = false;
        }
      }
    },
    async addComment() {
      const token = localStorage.getItem('access');
      const post_slug = this.$route.params.slug || localStorage.getItem('post_slug');

      try {
        const response = await getAPI.post(`/posts/${post_slug}/comments/`, {
          text: this.newCommentText,
          post_slug: post_slug,
        }, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        console.log('Comment has been added');
        this.post.comments.push(response.data);
        this.newCommentText = '';
      } catch (error) {
        console.log(error);
      }
    }
  },
};
</script>

 // async fetchPost() {
    //   const token = localStorage.getItem('access');
    //   console.log('this.$route:', this.$route);
    //   console.log('this.$route.params:', this.$route.params);
    //   const post_id = this.$route.params.id || localStorage.getItem('post_id');
    //   console.log("Post Id is: " + post_id + ', ' + 'Params is: ' + this.$route.params.id)

    //   console.log('API endpoint:', getAPI.defaults.baseURL);
    //   console.log('postSlug:', post_id);

    //   if (post_id) {
    //     this.loading = true;

    //     try {
    //       const response = await getAPI.get(`/posts/${post_id}/`, {
    //         headers: {
    //           Authorization: `Bearer ${token}`,
    //         },
    //       });
    //       console.log('Post API has received data');
    //       this.post = response.data;
    //       localStorage.setItem('post_id', post_id); // store post_id in local storage
    //     } catch (error) {
    //       console.log(error);
    //       this.error = error;
    //       return Promise.reject(error);
    //     } finally {
    //       this.loading = false;
    //     }
    //   }
    // },
        // async addComment() {
    //   const token = localStorage.getItem('access');
    //   const post_id = this.$route.params.id || localStorage.getItem('post_id');
    //   console.log("Post Id is: " + post_id + ', ' + 'Params is: ' + this.$route.params.id)

    //   try {
    //     const response = await getAPI.post(`/posts/${post_id}/comments/`, {
    //       text: this.newCommentText,
    //       post_id: post_id, // change to post_id
    //     }, {
    //       headers: {
    //         Authorization: `Bearer ${token}`,
    //       },
    //     });
    //     console.log('Comment has been added');
    //     this.post.comments.push(response.data); // add the new comment to the post's comments array
    //     this.newCommentText = ''; // reset the newCommentText field
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },