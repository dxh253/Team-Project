<template>
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
</style>
  