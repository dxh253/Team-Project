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
            <a :href="post.get_image" target="_blank"
              ><img
                :src="post.get_image"
                :style="{ filter: blur ? 'blur(10px)' : 'none' }"
                @click="enlargeImage"
            /></a>
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
          <span class="icon is-small"
            ><i
              class="fas fa-arrow-up"
              @click="upvote"
              :style="{ color: upColor }"
            ></i
          ></span>
          <span>{{ totalScore }}</span>
          <span class="icon is-small"
            ><i
              class="fas fa-arrow-down"
              @click="downvote"
              :style="{ color: downColor }"
            ></i
          ></span>
        </div>
        <div v-if="post.get_image" class="column">
          <span class="icon is-small">
            <i class="fas fa-eye" @click="toggleBlur"></i>
          </span>
        </div>
      </div>
    </div>
    <div class="card-footer">
      <span class="card-footer-item">posted by {{ post.username }}</span>
      <span class="card-footer-item"
        ><i class="far fa-clock"></i> {{ post.time_since_post }}</span
      >
      <span class="card-footer-item"
        ><i class="fas fa-rss"></i> {{ post.category_name }}</span
      >
      <div class="card-footer-item">
        <router-link
          v-if="isPostCreator"
          :to="{ name: 'edit-post', params: { id: post.id } }"
        >
          <span class="icon"><i class="fas fa-edit"></i></span>
        </router-link>
        <span v-if="isPostCreator" class="icon" @click="deletePost"
          ><i class="fas fa-trash"></i
        ></span>
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "@/plugins/axios";
import { reactive } from "@vue/reactivity";
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
      vote: 0,
      userVote: null,
      isHidden: false,
      isDeleted: false,
      blur: this.post.isBlurred,
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
      return this.vote === 1 ? "orange" : "grey";
    },
    downColor() {
      return this.vote === -1 ? "blue" : "grey";
    },
    isPostCreator() {
      const token = localStorage.getItem("access");
      const decodedToken = jwt_decode(token);
      const userId = decodedToken.user_id;
      return this.post.owner === userId;
    },
  },
  created() {
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
    toggleBlur() {
      this.blur = !this.blur;
    },
    deletePost() {
      console.log("delete post");
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
    upvote() {
      if (this.userVote && this.userVote.vote === 1) {
        this.vote = 0;
        this.updateVote();
      } else {
        this.vote = 1;
        this.updateVote().then(() => {
          this.$emit("vote-updated", this.post.id, this.vote);
        });
      }
    },
    downvote() {
      if (this.userVote && this.userVote.vote === -1) {
        this.vote = 0;
        this.updateVote();
      } else {
        this.vote = -1;
        this.updateVote().then(() => {
          this.$emit("vote-updated", this.post.id, this.vote);
        });
      }
    },

    updateVote() {
      const token = localStorage.getItem("access");
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
          .put(
            `/api/v1/posts/${this.post.id}/votes/${this.userVote.id}/`,
            data,
            {
              headers: {
                Authorization: `Bearer ${token}`,
              },
            }
          )
          .then((response) => {
            this.userVote = reactive(response.data);
            this.$emit("vote-updated", this.totalScore);
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        getAPI
          .post(`/api/v1/posts/${this.post.id}/votes/`, data, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          })
          .then((response) => {
            this.userVote = reactive(response.data);
            this.$emit("vote-updated", this.totalScore);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>
