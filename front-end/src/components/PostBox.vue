<template>
    <div>
        <div class="post-box" v-show="!isHidden && !isDeleted">
            <div class="post-box-header">
                <h3 class="post-box-title"><router-link :to="{ name: 'post-detail', params: { slug: post.slug } }">{{
                    post.title }}</router-link>
                </h3>
                <span>&nbsp;// posted by {{ post.username }} </span>
                <div class="post-box-edit">
                <div class="flex-item">
                    <router-link v-if="isPostCreator" :to="{ name: 'edit-post', params: { id: post.id } }"> 
                    <i class="fa-sharp fa-solid fa-pen-to-square fa-xl"></i>
                    </router-link>
                </div>
                </div>
                <div class= "flex-item"><i class="fa-solid fa-trash-can fa-xl" v-if="isPostCreator" @click="deletePost" v-on:click="isDeleted = !isDeleted"></i></div> 
            </div>
            <p class="post-box-description">{{ post.description }}</p>
            <div>
                <figure>
                    <img :src="post.get_image" v-if="!post.isBlurred" />
                    <img :src="post.get_image" v-else :style="{ filter: 'blur(10px)' }" />
                </figure>
            </div>
            <div class="post-box-details">
                <div class="post-box-category">
                    <i class="fas fa-rss"></i>
                    <span class="post-box-category-name">{{ post.category_name }}</span>
                </div>

                <div class="post-box-time">
                    <i class="far fa-clock"></i>
                    <span class="post-box-time-since">{{ post.time_since_post }}</span>
                </div>
            </div>
            <div class="post-box-interactions">
                <div class="flex-item"><i class="fas fa-arrow-up post-box-upvote fa-xl" @click="upvote" :style="{ color: upColor }"></i>
                <span>{{ post.score }}</span>
                <i class="fas fa-arrow-down post-box-downvote fa-xl" @click="downvote" :style="{ color: downColor }"></i>
                </div>
                <div class ="flex-item"><span><i class="fa-sharp fa-solid fa-comments fa-xl"></i><router-link
                        :to="{ name: 'post-detail', params: { slug: post.slug } }">&nbsp;{{ post.number_of_comments
                        }}Comments</router-link></span></div>
                <div class="flex-item"><i class="fa-sharp fa-solid fa-eye-slash fa-xl" v-on:click="isHidden = !isHidden"></i></div>
            </div>

        </div>
        <!-- <div v-show="isDeleted">
            <div class="post-box">
                <div style="justify-content: center; display: flex;">
                    <i class="fa-solid fa-trash-can fa-xl" v-on:click="isDeleted = !isDeleted"></i>
                </div>
            </div>
        </div> -->
        <div v-show="isHidden">
            <div class="post-box">
                <div style="justify-content: center; display: flex;">
                    <i class="fa-solid fa-eye fa-xl" v-on:click="isHidden = !isHidden"></i>
                </div>
            </div>
        </div> 
        
    </div>
</template>


<script>
import { getAPI } from '@/plugins/axios';
import { reactive } from '@vue/reactivity';
import jwt_decode from 'jwt-decode';

export default {
    props: {
        post: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            vote: 0,
            userVote: null,
            isHidden: false,
            isDeleted: false,
        };
    },
    computed: {
        totalScore() {
            let score = this.post.score;
            if (this.userVote) {
                score -= this.userVote.vote;
            }
            score += this.vote;
            return score;
        },
        upColor() {
            return this.vote === 1 ? 'orange' : 'grey';
        },
        downColor() {
            return this.vote === -1 ? 'blue' : 'grey';
        },
        isPostCreator() {
            const token = localStorage.getItem("access");
            const decodedToken = jwt_decode(token);
            const userId = decodedToken.user_id;
            return this.post.owner === userId;
        },
    },
    created() {
        const token = localStorage.getItem('access');
        const decodedToken = jwt_decode(token);
        const userId = decodedToken.user_id;

        getAPI
            .get(`/posts/${this.post.id}/votes/?user_id=${userId}`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            })
            .then((response) => {
                const existingVote = response.data.find(
                    (vote) => vote.post_id === this.post.id && vote.user_id === userId
                );

                if (existingVote) {
                    this.userVote = reactive(existingVote);
                    this.vote = existingVote.vote;
                }
            })
            .catch((error) => {
                console.log(error);
            });
    },
    methods: {
        deletePost() {
            console.log('delete post');
            const token = localStorage.getItem('access');
            const config = {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            };

            getAPI.delete(`/posts/${this.post.id}/`, config)
                .then(() => {
                    // Emit a custom event to notify the parent component that a post was deleted
                    this.$emit('post-deleted', this.post.id);
                })
                .catch(error => {
                    console.log(error);
                });
        },
        upvote() {
            // If the user has already upvoted, remove their vote.
            if (this.userVote && this.userVote.vote === 1) {
                this.vote = 0;
                this.updateVote();
            }
            // If the user has already downvoted or hasn't voted yet, upvote the post.
            else {
                this.vote = 1;
                this.updateVote();
            }
        },
        downvote() {
            // If the user has already downvoted, remove their vote.
            if (this.userVote && this.userVote.vote === -1) {
                this.vote = 0;
                this.updateVote();
            }
            // If the user has already upvoted or hasn't voted yet, downvote the post.
            else {
                this.vote = -1;
                this.updateVote();
            }
        },

        updateVote() {
            const token = localStorage.getItem('access');
            const decodedToken = jwt_decode(token);
            const userId = decodedToken.user_id;

            const data = {
                post_id: this.post.id,
                user_id: userId,
                vote: this.vote,
                id: this.userVote ? this.userVote.id : null,
            };

            if (data.id) {
                getAPI
                    .put(`/posts/${this.post.id}/votes/${this.userVote.id}/`, data, {
                        headers: {
                            Authorization: `Bearer ${token}`,
                        },
                    })
                    .then((response) => {
                        this.userVote = reactive(response.data);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            } else {
                getAPI
                    .post(`/posts/${this.post.id}/votes/`, data, {
                        headers: {
                            Authorization: `Bearer ${token}`,
                        },
                    })
                    .then((response) => {
                        this.userVote = reactive(response.data);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
    },
};
</script>

<style>
@import url('./../assets/PostBox.css');
</style>
