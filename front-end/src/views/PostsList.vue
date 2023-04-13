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
            <post-box :post="post" />
            <vote :post-id="post.id" :initial-score="post.score"></vote>
        </div>
    </div>
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
    created() {
        const token = localStorage.getItem("access");

        getAPI
            .get("/allposts/", {
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
.post-background {
    background-color: #c5aaf0;
    padding: 20px;
    border-radius: 25px;
    float: left;
    width: 85%;
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

.left {
    width: 15%;
    float: left;
    padding-right: 25px;
}
</style>
