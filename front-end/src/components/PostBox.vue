<template>
  <div>
    <div class="post-box" v-show="!isHidden">
        <h3 class="post-box-title"><router-link :to="{ name: 'post-detail', params: { slug: post.slug } }">{{ post.title }}</router-link>
        </h3>
            <p class="post-box-description">{{ post.description }}</p>
      <div class="post-box-details">
        <div class="post-box-subreddit">
          <i class="fas fa-rss"></i>
          <span class="post-box-subreddit-name">{{ post.category_name }}</span>
        </div>
        <div class="post-box-score">
          
          
        </div>
        <div class="post-box-time">
          <i class="far fa-clock"></i>
          <span class="post-box-time-since">{{ post.time_since_post }}</span>
        </div>
      </div>
      <div>
      <div class="post-box-interactions">
        <i class="fas fa-arrow-up post-box-upvote fa-xl" @click="upvote" :style="{ color: upColor }"></i>
        <span>{{ post.score }}</span>
        <i class="fas fa-arrow-down post-box-downvote fa-xl" @click="downvote" :style="{ color: downColor }"></i>
        <span style="margin-left: 10px;"><i class="fa-sharp fa-solid fa-comments fa-xl"></i><router-link :to="{ name: 'post-detail', params: { slug: post.slug } }">&nbsp;{{ post.number_of_comments }}Comments</router-link></span>
        <i class="fa-sharp fa-solid fa-eye-slash fa-xl" v-on:click="isHidden = !isHidden" style="margin-left: 10px;"></i>
      </div>
      </div>
    </div>
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
    };
  },
  computed: {
    totalScore() {
      // Calculate the total score based on the current vote and the existing votes from the API response.
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
  },
  created() {
    // Send a GET request to retrieve the user's existing vote for the post.
    getAPI.get(`/posts/${this.post.id}/votes/?user_id=1`)
      .then(response => {
        // If the user has already voted, extract the existing vote from the response data.
        const existingVote = response.data.find(vote => vote.post_id === this.post.id && vote.user_id === 1);

        if (existingVote) {
          this.userVote =  reactive(existingVote);

          // Set the vote to the user's existing vote.
          this.vote = existingVote.vote;
        }
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    upvote() {
      // If the user has already upvoted, remove their vote.
      if (this.userVote && this.userVote.vote === 1) {
        this.vote = 0;
      } else {
        // If the user has already downvoted, switch their vote.
        if (this.userVote && this.userVote.vote === -1) {
          this.vote = 1;
        } else {
          // If the user hasn't voted yet or has removed their vote, upvote.
          this.vote = 1;
        }
      }

      this.updateVote();
    },
    downvote() {
      // If the user has already downvoted, remove their vote.
      if (this.userVote && this.userVote.vote === -1) {
        this.vote = 0;
      } else {
        // If the user has already upvoted, switch their vote.
        if (this.userVote && this.userVote.vote === 1) {
          this.vote = -1;
        } else {
          // If the user hasn't voted yet or has removed their vote, downvote.
          this.vote = -1;
        }
      }

      this.updateVote();
    },
    updateVote() {
      const data = {
        post_id: this.post.id,
        user_id: 1,
        vote: this.vote,
        id: this.userVote ? this.userVote.id : null,
      };

      if (data.id) {
        // If the user has already voted, make a PUT request to update the existing vote.
        getAPI.put(`/posts/${this.post.id}/votes/${this.userVote.id}/`, data)
          .then(response => {
            console.log(response.data);
            this.userVote = reactive(response.data);
          })
          .catch(error => {
            console.log(error);
          });
      } else {
        // If the user hasn't voted yet, make a POST request to create a new vote.
        getAPI.post(`/posts/${this.post.id}/votes/`, data)
          .then(response => {
            console.log(response.data);
            this.userVote = reactive(response.data);
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
  },
};

</script>


  <style>
  .post-box {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 25px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
  }
  
  .post-box-title {
    margin-top: 0;
    display: flex;
  }
  
  .post-box-description {
    color: #666;
    font-size: 16px;
    line-height: 1.5;
  }
  
  .post-box-details {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 10px;
  }

  .post-box-interactions{
    display: flex;
    align-items: center;
    margin-top: 10px;
  }
  
  .post-box-subreddit {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: #999;
  }
  
  .post-box-subreddit-name {
  }
  
  .post-box-score {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: #999;
  }
  
  .post-box-upvote,
  .post-box-downvote {
    cursor: pointer;
    margin: 0 5px;
  }
  
  .post-box-score-value {
    margin: 0 10px;
  }
  
  .post-box-time {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: #999;
  }
  
  .post-box-time-since {
    margin-left: 5px;
  }

  </style>
  
  