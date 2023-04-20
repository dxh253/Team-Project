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
  <div class="container">
    <div v-if="loading">
      <div class="notification is-primary">
        Loading...
      </div>
    </div>
    <div v-else-if="post" class="box">
      <article class="media">
        <div class="media-content">
          <h1 class="title">{{ post.title }}</h1>
          <p class="subtitle">{{ post.description }}</p>
          <figure class="image">
            <a :href="post.get_image" target="_blank">
              <img :src="post.get_image" :style="{ filter: blur ? 'blur(10px)' : 'none', 'max-height':'300px', 'max-width':'300px' }" alt="Post image">
            </a>
          </figure>
          <div class="level">
            <div class="level-left">
              <p class="level-item">
                <span class="icon is-small">
                  <i class="fas fa-user"></i>
                </span>
                {{ post.author }}
              </p>
              <p class="level-item">
                <span class="icon is-small">
                  <i class="fas fa-clock"></i>
                </span>
                {{ post.time_since_post }}
              </p>
            </div>
            <div class="level-right">
              <span class="tag is-info">{{ post.category }}</span>
            </div>
          </div>
          <hr>
          <h2 class="subtitle">Comments</h2>
          <div class="comment-container">
            <form>
              <div class="field is-grouped">
                <div class="control is-expanded">
                  <input class="input" type="text" v-model="newCommentText" placeholder="Add a comment...">
                </div>
                <div class="control">
                  <button class="button is-info" @click.prevent="addComment">
                    Add Comment
                  </button>
                </div>
              </div>
            </form>
            <div class="comments">
              <div class="media">
                <div class="media-content">
                  <div class="content">
                    <p>
                      <strong>John Smith</strong>
                      <br>
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque
                      tortor vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </article>
    </div>
    <div v-else>
      <div class="notification is-danger">
        Error fetching post. Please try again later.
      </div>
    </div>
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
</script>
