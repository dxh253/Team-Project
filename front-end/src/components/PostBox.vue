<!-- <template>
    <div class="post-box">
      <router-link :to="{ name: 'post-detail', params: { slug: post.slug } }">
        <h3>{{ post.title }}</h3>
      </router-link>
      <p>{{ post.description }}</p>
      <p>Subreddit: {{ post.subreddit_name }}</p>
      <p>Score: {{ post.score }}</p>
      <p>Posted {{ post.time_since_post }}</p>
    </div>
</template>
  
<script>
  export default {
    props: {
      post: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style>
  .post-box {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 10px;
  }
</style> -->

<template>
    <div class="post-box">
      <router-link :to="{ name: 'post-detail', params: { slug: post.slug } }">
        <h3 class="post-box-title">{{ post.title }}</h3>
      </router-link>
      <p class="post-box-description">{{ post.description }}</p>
      <div class="post-box-details">
        <div class="post-box-subreddit">
          <i class="fas fa-rss"></i>
          <span class="post-box-subreddit-name">{{ post.subreddit_name }}</span>
        </div>
        <div class="post-box-score">
          <i class="fas fa-arrow-up post-box-upvote" @click="upvote"></i>
          <span class="post-box-score-value">{{ post.score }}</span>
          <i class="fas fa-arrow-down post-box-downvote" @click="downvote"></i>
        </div>
        <div class="post-box-time">
          <i class="far fa-clock"></i>
          <span class="post-box-time-since">{{ post.time_since_post }}</span>
        </div>
      </div>
      <div>
        <button @click="upvote">Upvote</button>
        <span>{{ post.score }}</span>
        <button @click="downvote">Downvote</button>
      </div>
    </div>
  </template>
  
  <script>
  import { getAPI } from '@/plugins/axios';


  export default {
    props: {
      post: {
        type: Object,
        required: true,
      },
    },
    data(){
      return{
        vote: 0,
      }
    },
    methods: {
      upvote() {
        this.vote = 1;
        this.updateVote();  
      },
      downvote() {
        this.vote = -1;
        this.updateVote();
      },
      updateVote() { //TODO: update the vote on the server
      const data = {
        post_id: this.post.id,
        user_id: 3,
        vote: this.vote,
        id: 5,
      };
      // axios.post('/posts/' + this.post.id + '/votes', data)
      //   .then(response => {
      //     console.log(response.data);
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   });
      getAPI.post('/posts/' + this.post.id + '/votes', data)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    },
  };
  </script>
  
  <style>
  .post-box {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
  }
  
  .post-box-title {
    margin-top: 0;
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
  
  .post-box-subreddit {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: #999;
  }
  
  .post-box-subreddit-name {
    margin-left: 5px;
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
  
  