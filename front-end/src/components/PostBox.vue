<template>
  <div class="card">
    <div class="card-header">
      <p class="card-header-title">
        <router-link :to="{ name: 'PostDetails', params: { id: post.id } }">
          {{ post.title }}
        </router-link>
      </p>
      <div class="card-header-icon">
        <span class="icon">
          <i class="fas fa-angle-down"></i>
        </span>
      </div>
    </div>
    <div class="card-content">
      <div class="content">
        <p>{{ post.description }}</p>
        <div v-if="post.get_image" class="has-text-centered">
          <figure class="image is-16by9">
            <a :href="post.get_image" target="_blank"><img :src="post.get_image"
                :style="{ filter: blur ? 'blur(100px)' : 'none' }" @click="enlargeImage" /></a>
          </figure>
        </div>
      </div>
      <div class="columns is-mobile is-gapless">
        <div class="column">
          <router-link :to="{ name: 'PostDetails', params: { id: post.id } }">
            <span class="icon is-small"><i class="fas fa-comment"></i></span>
            <span>Comments</span>
          </router-link>
        </div>
        <div class="column">
          <span class="icon is-small"><i class="fas fa-arrow-up" @click="upvote" tabindex="0" role="button" @keydown.enter="upvote"

              :style="{ color: this.userVote === 1 ? 'orange' : 'grey' }"></i></span>
          <span>{{ currentScore }}</span>
          <span class="icon is-small"><i class="fas fa-arrow-down" @click="downvote" tabindex="0" role="button" @keydown.enter="downvote"
              :style="{ color: this.userVote === -1 ? 'blue' : 'grey' }"></i></span>
        </div>
        <div v-if="post.get_image" class="column">
          <span class="icon is-small" >
            <i class="fas fa-eye" @click="toggleBlur" @keydown.enter="toggleBlur" tabindex="0"></i>
          </span>
        </div>
      </div>
    </div>
    <div class="card-footer">
      <span class="card-footer-item">posted by {{ post.username }}</span>
      <span class="card-footer-item"><i class="far fa-clock"></i> {{ post.time_since_post }}</span>
      <span class="card-footer-item"><i class="fas fa-rss"></i> {{ post.category_name }}</span>
      <div class="card-footer-item">
        <!-- <router-link v-if="isPostCreator" :to="{ name: 'edit-post', params: { id: post.id } }"> -->
        <router-link v-if="isPostCreator" :to="{ name: 'edit-post', params: { id: post.id } }">
          <span class="icon"><i class="fas fa-edit"></i></span>
        </router-link>
        <span v-if="isPostCreator" class="icon" @click="deletePost" tabindex="0" role="button" @keydown.enter="deletePost"><i class="fas fa-trash"></i></span>
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "@/plugins/axios";
import jwt_decode from "jwt-decode";

export default {
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      // Current score, including votes for this post from other users.
      currentScore: 0,
      // The current user's vote for this post. Either -1, 0, or 1.
      userVote: 0,
      // The user id (id field in the forum_postvotes table).
      userId: null,
      isHidden: false,
      isDeleted: false,
      blur: this.post.isBlurred,
    };
  },
  computed: {
    isPostCreator() {
      const token = localStorage.getItem("access");
      const decodedToken = jwt_decode(token);
      const userId = decodedToken.user_id;
      return this.post.owner === userId;
    },
  },
  created() {
    this.refreshVotes();
  },
  methods: {
    toggleBlur() {
      this.blur = !this.blur;
    },
    refreshVotes() {
      const token = localStorage.getItem("access");
      const decodedToken = jwt_decode(token);
      const userId = decodedToken.user_id;

      getAPI
        .get(`/api/v1/posts/${this.post.id}/votes/?user_id=${userId}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          const existingVote = response.data.find(
            (vote) => vote.post_id === this.post.id && vote.user_id === userId
          );

          // The total votes for the post, including votes from other users.
          this.currentScore = response.data.reduce(
            (acc, cur) => acc + cur.vote,
            0
          );

          if (existingVote) {
            this.userVote = existingVote.vote;
            this.userId = existingVote.id;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    changePostVotesBy(n) {
      const token = localStorage.getItem("access");
      const decodedToken = jwt_decode(token);
      const userId = decodedToken.user_id;
      let data = {
        id: this.userId,
        // Either -1, 0, or 1 to represent downvotes/no vote/upvote.
        vote: n,
        // The id field in the forum_post table.
        post_id: this.post.id,
        // The id field in the auth_user table.
        user_id: userId,
      };

      // Always send a post request, it's scuffed anyway.
      getAPI
        .post(`/api/v1/posts/${data.post_id}/votes/`, data, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then(() => this.refreshVotes());
    },
    upvote() {
      // If the user has previously upvoted the post, then undo the upvote.
      let n = this.userVote == 1 ? 0 : 1;
      this.changePostVotesBy(n);
    },
    downvote() {
      // If the user has previously downvoted the post, then undo the downvote.
      let n = this.userVote == -1 ? 0 : -1;
      this.changePostVotesBy(n);
    },
    deletePost() {
      const token = localStorage.getItem("access");
      const config = {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      };

      getAPI
        .delete(`/api/v1/posts/${this.post.id}/`, config)
        .then(() => {
          this.$emit("post-deleted", this.post.id);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

