<template>
      <div class="post">
          <h1>Create a Post</h1>
            <form @submit.prevent="handleSubmit">
              <input class="input" id="title" v-model="title" type="text" required placeholder="Title">
              <br>
              <textarea class="description" id="description" v-model="description" placeholder="Description" rows="10"></textarea>
              <br>
              <div class="bottom">
                <button type="submit">Create Post</button>
                <br>
                <select class="category" id="category" v-model="category" required>
                <option value="" disabled>Category</option>
                <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                </select>
              </div>
            </form>
      </div>
</template>
  
  <script>
  import { getAPI } from '@/plugins/axios';
  
  export default {
    data() {
      return {
        title: '',
        description: '',
        owner: '',
        category: '',
        categories: [],
      };
    },
    mounted() {
        this.fetchCategories(); 
      },  
    methods: {
      fetchCategories() {
        getAPI.get('/categories/')
          .then(response => {
            this.categories = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      },  
      handleSubmit() {
        const payload = {
          title: this.title,
          description: this.description,
          category: this.category,
          owner: 1,
        };
        getAPI
        .post('/posts/', payload).then(() => {
          alert('Post created successfully!');
          this.$router.push('/'); // Redirect to homepage or wherever you want
        }).catch((error) => {
          console.log(error);
        });
      },
    },
  };
  </script>

  <style>
  @import url('./../assets/PostCreate.css');
  </style>
  