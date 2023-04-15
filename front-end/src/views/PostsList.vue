<template>
    <div class="left">
        <div class="sidebar">
            <p>hello</p>
        </div>
        <router-link to="/create">
            <div class="create">
                New Post
            </div>
        </router-link>
    </div>
    <div class="post-background">
        <h2 style="color: black; margin-bottom: 10px;">Posts</h2>
        <div v-for="post in allposts" :key="post.id">
            <!-- <post-box :post="post" /> -->
            <vote :post-id="post.id" :initial-score="post.score"></vote>
            <post-box :post="post" @postDeleted="removePostFromList" />
        </div>
    </div>
    <button @click="scrollToTop" class="myBtn">Scroll to top</button>
</template>

<script>
import { getAPI } from '@/plugins/axios';
import PostBox from '../components/PostBox.vue';
import { mapState } from 'vuex';

export default {
    name: 'PostsList',
    components: {
        'post-box': PostBox,
    },
    data() {
        return {
            allposts: [],
        }
    },
    computed: mapState(['APIData']),
    methods: {
      scrollToTop() {
        // Scroll to top with smooth behavior
        window.scrollTo({ top: 0, behavior: 'instant' });
      },
      removePostFromList(postId) {
        this.allposts = this.allposts.filter((post) => post.Id !== postId);
      },
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

<style>
.myBtn {
  position: fixed;
  bottom: 20px;
  right: 30px;
  z-index: 99;
  border: none;
  outline: none;
  background-color: #7B57AA;
  color: white;
  cursor: pointer;
  padding: 15px;
  border-radius: 10px;
  font-size: 18px;
}
.post-background {
  background-color: #c5aaf0;
  padding: 20px;
  border-radius: 25px;
  float: left;
  width:45%;
}


  .sidebar {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 375px;
    background-color: #7B57AA;
    border-radius: 25px;
    margin-bottom: 25px;
    color: black;
  }

  .create {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    background-color: #5D3095;
    border-radius: 25px;
    padding: 25px;
    color: white;
  }

  .left{
    width: 15%;
    float: left;
    padding-right: 25px;
    margin-left: 280px;
  }

</style>
