<template>
  <div class="columns is-mobile">
    <div class="column is-one-quarter-desktop is-hidden-mobile">
      <div class="box">
        <p class="title is-5">hello</p>
      </div>
    </div>
    <div class="column">
      <h2 class="title is-4" style="margin-bottom: 1rem; display: flex; align-items: center;">
        <span style="flex-grow: 1;">Posts</span>
        <router-link to="/create">
          <button class="button is-primary">New Post</button>
        </router-link>
      </h2>
      <div class="searchbar">
        <input class="search" type="text" v-model="searchTerm" placeholder="Search posts" >
      </div> 
      <div v-if="filteredPosts.length > 0">
            <div v-for="post in filteredPosts" :key="post.id">
        <div class="box">
          <div class="columns is-vcentered">
            <div class="column">
              <post-box
                :post="post"
                @postDeleted="removePostFromList"
                @vote-updated="updatePostVote"
              />
            </div>
          </div>
        </div>
      </div>
      <button @click="scrollToTop" class="button is-info is-hidden-desktop is-fullwidth">Scroll to top</button>
    </div>
  </div>
  </div>
  <button @click="scrollToTop" class="myBtn is-hidden-mobile">Scroll to top</button>
</template>


<script>
import { getAPI } from '@/plugins/axios';
import PostBox from '../components/PostBox.vue';

export default {
  name: 'PostsList',
  components: {
    'post-box': PostBox,
  },
  data() {
    return {
      allposts: [],
      searchTerm: '',


    }
  },
  computed: {
    filteredPosts() {
            return this.allposts.filter(post => {
                // filter posts that include the search term in the title
                return post.title.toLowerCase().includes(this.searchTerm.toLowerCase());
            });
        }
  },
  methods: {
    scrollToTop() {
      // Scroll to top with smooth behavior
      window.scrollTo({ top: 0, behavior: 'instant' });
    },
    removePostFromList(postId) {
      this.allposts = this.allposts.filter((post) => post.id !== postId);
    },
    updatePostVote(postId, vote) {
      const postToUpdate = this.allposts.find((post) => post.id === postId);
      if (postToUpdate) {
        postToUpdate.score += vote;
      }
    },
    updatePostScore(postId, updatedScore) {
      const postToUpdate = this.allposts.find((post) => post.id === postId);
      if (postToUpdate) {
        postToUpdate.score = updatedScore;
      }
    }
  },
  created() {
    const token = localStorage.getItem("access");

    getAPI
      .get("/posts/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        console.log("Post API has received data");
        this.allposts = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
}
</script>

<style lang="scss">
.box {
  margin-bottom: 1.5rem;
}

@media screen and (max-width: 1023px) {
  .column.is-one-quarter-desktop {
    display: none;
  }

  .button.is-hidden-desktop {
    display: block !important;
    margin-left: auto;
    margin-right: auto;
    margin-top: 1rem;
    margin-bottom: 1rem;
  }
}

.myBtn {
    position: fixed;
    bottom: 20px;
    right: 30px;
    z-index: 99;
    border: none;
    outline: none;
    background-color: hsl(171, 100%, 41%);
    color: white;
    cursor: pointer;
    padding: 15px;
    border-radius: 5px;
    font-size: 18px;
  }
</style>