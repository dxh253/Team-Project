<!-- <template> # NOT DONE
    <div>
      <h1>{{ subreddit.name }}</h1>
      <p>{{ subreddit.description }}</p>
      <ul>
        <li v-for="post in posts" :key="post.id">
          <h2>{{ post.title }}</h2>
          <p>{{ post.description }}</p>
          <a :href="post.link">{{ post.link }}</a>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name : 'ForumView',
    data () {
      return {
        subreddit: {},
        posts: []
      }
    },
    mounted () {
      axios.get(`/api/v1//${this.$route.params.slug}`)
        .then(response => {
          this.subreddit = response.data.subreddit
          this.posts = response.data.posts
        })
    }
  }
  </script>
   -->

<!-- <template>
    <div>
      <h1>Reddit Clone</h1>
      <div v-for="post in posts" :key="post.id">
        <h2>{{ post.title }}</h2>
        <p>{{ post.description }}</p>
        <p>{{ post.username }}</p>
      </div>
    </div>
</template>
  
<script>
  import { mapState, mapActions } from 'vuex'
  
  export default {
    computed: {
      ...mapState(['posts']),
    },
    mounted() {
      this.fetchPosts()
    },
    methods: {
      ...mapActions(['fetchPosts']),
    },
  }
</script> -->

<!-- <template>
  <div>
    <h1>Posts</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <router-link :to="{ name: 'post-detail', params: { postId: post.id }}">
          {{ post.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
    };
  },
  mounted() {
    axios
      .get('/api/posts/')
      .then((response) => {
        this.posts = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script> -->

<template>
  <div>
    <h1>Posts</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
      </li>
    </ul>
    <form @submit.prevent="submitPost">
      <label>Title</label>
      <input type="text" v-model="post.title" required>
      <label>Content</label>
      <textarea v-model="post.content" required></textarea>
      <button type="submit">Create Post</button>
    </form>
  </div>
</template>

<script>
export default {
  computed: {
    posts() {
      return this.$store.getters.posts
    }
  },
  data() {
    return {
      post: {
        title: '',
        content: ''
      }
    }
  },
  mounted() {
    this.$store.dispatch('fetchPosts')
  },
  methods: {
    async submitPost() {
      await this.$store.dispatch('createPost', this.post)
      this.post = { title: '', content: '' }
    }
  }
}
</script>
