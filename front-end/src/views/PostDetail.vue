<template>
  <div class="container">
    <div class="column is-one-quarter-desktop is-hidden-mobile">
              <router-link to="/posts">
                  <button>
                      <i class="fas fa-arrow-left"></i>
                  </button>
              </router-link>
          </div>
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
              <img :src="post.get_image"
                :style="{ filter: blur ? 'blur(10px)' : 'none', 'max-height': '300px', 'max-width': '300px' }"
                alt="Post image">
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
          <div class="comments">
            <form class="mt-3" @submit.prevent="addComment">
              <div class="field">
                <label class="label">Add Comment</label>
                <div class="control">
                  <textarea class="textarea" v-model="newCommentText" placeholder="Write your comment here"></textarea>
                </div>
              </div>
              <div class="control">
                <button type="submit" class="button is-primary">Submit</button>
              </div>
            </form>
          </div>
          <CommentBox :comments="post.comments" @add-comment="addComment" @add-reply="addReply" />
        </div>
      </article>
    </div>
  </div>
</template>


<script>
import { getAPI } from '@/plugins/axios';
import CommentBox from '@/components/CommentBox.vue';

export default {
  name: 'PostDetail',
  components: {
    CommentBox,
  },
  data() {
    return {
      post: undefined,
      loading: false,
      newCommentText: '',
    };
  },
  computed: {
    postSlug() {
      return this.$route.params.slug;
    },
  },
  watch: {
    postSlug: {
      immediate: true,
      handler: async function () {
        await this.fetchPost();
      },
    },
  },
  methods: {
    async fetchPost() {
      const token = localStorage.getItem('access');
      const post_slug = this.postSlug;

      if (!post_slug) {
        this.$router.go();
      }

      console.log('API endpoint:', getAPI.defaults.baseURL);
      console.log('postSlug:', post_slug);

      this.loading = true;

      try {
        const response = await getAPI.get(`/api/v1/posts/${post_slug}/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        console.log('Post API has received data');
        this.post = Object.assign({}, response.data);

        const commentsResponse = await getAPI.get(`/api/v1/posts/${this.post.id}/comments/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.post.comments = commentsResponse.data;

        localStorage.setItem('post_slug', post_slug);
      } catch (error) {
        console.log(error);
        this.error = error;
        return Promise.reject(error);
      } finally {
        this.loading = false;
      }
    },

    async addComment() {
      const token = localStorage.getItem('access');
      const post_slug = this.postSlug;

      try {
        const response = await getAPI.post(`/api/v1/posts/${post_slug}/comments/`, {
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
    },
    // ...
    async addReply({ parentCommentId, text }) {
      const token = localStorage.getItem('access');
      const post_slug = this.postSlug;

      try {
        const response = await getAPI.post(`/api/v1/posts/${post_slug}/comments/`, {
          text: text,
          post_slug: post_slug,
          parent_comment: parentCommentId,
        }, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        console.log('Reply has been added');

        // Find the parent comment and add the reply to its children
        const parentComment = this.post.comments.find(comment => comment.id === parentCommentId);
        if (parentComment) {
          parentComment.children.push(response.data);
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  unmounted() {
    localStorage.removeItem('post_slug');
  },

};
</script>

<style scoped>
@media screen and (max-width: 768px) {
  .comments form {
    width: 100%;
  }
}
</style>
