<template>
    <div>
        <input v-model="searchTerm" placeholder="Search posts" />
    </div>
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
        <div v-if="filteredPosts.length > 0">
            <div v-for="post in filteredPosts" :key="post.id">
                <post-box :post="post" @postDeleted="removePostFromList" />
            </div>
        </div>
    </div>
    <button @click="scrollToTop" class="myBtn">Scroll to top</button>
</template>

<script>
import { getAPI } from '@/plugins/axios';
import PostBox from '../components/PostBox.vue';
// import { mapState } from 'vuex';

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
        // mapState(['APIData']),
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
@import url('./../assets/PostList.css');
</style>
