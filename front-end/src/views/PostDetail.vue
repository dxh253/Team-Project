<!-- <template>
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
        post: {},
      };
    },
    computed: {
      ...mapState(['APIData']),
    },
    created() {
      this.fetchPost();
    },
    methods: {
      fetchPost() {
        const slug = this.$route.params.slug;
        const posts = this.$store.state.APIData;
        if (posts) {
          this.post = posts.find(post => post.slug === slug);
        }
      },
      addComment() {
        const token = localStorage.getItem('access');
        const postId = this.post.id;
        const data = { text: this.newCommentText };
  
        getAPI.post(`/posts/{{ post.id }}/comments/`, data, {
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
   -->

   <template>
    <div class="post-background">
      <div class="post-container">
        <h2>{{ post.title }}</h2>
        <p class="post-box-description">{{ post.description }}</p>
        <a :href="post.get_image" target="_blank"><img :src="post.get_image" :style="{ filter: blur ? 'blur(10px)' : 'none' }" @click="enlargeImage"></a>
        <span class="post-box-time-since">posted {{ post.time_since_post }}</span>
        <hr>
        <h3>Comments</h3>
        <div class="comment-container">
          <p>Placeholder for comments...</p>
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
      post: {},
    };
  },
  created() {
    const token = localStorage.getItem('access');
    const postId = this.$route.params.id;

    getAPI
      .get(`/posts/${postId}/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        console.log('Post API has received data');
        this.post = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
