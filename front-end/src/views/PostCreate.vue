<template>
    <div>
      <h1>Create a Post</h1>
      <form @submit.prevent="handleSubmit">
        <label for="title">Title:</label>
        <input id="title" v-model="title" type="text" required>
        <br>
        <label for="link">Link:</label>
        <input id="link" v-model="link" type="url">
        <br>
        <label for="description">Description:</label>
        <textarea id="description" v-model="description" rows="5"></textarea>
        <br>
        <label for="category">Category:</label>
        <select id="category" v-model="category" required>
          <option value="" disabled>Select a category</option>
          <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
        </select>
        <br>
        <button type="submit">Create Post</button>
      </form>
    </div>
  </template>
  
  <script>
  import { getAPI } from '@/plugins/axios';
  
  export default {
    data() {
      return {
        title: '',
        link: '',
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
          link: this.link,
          description: this.description,
          category: this.category,
          owner: 1,
        };
        getAPI
        .post('/posts/', payload).then(() => {
          alert('Post created successfully!');
          this.$router.push('/'); // Redirect to homepage or wherever you want
        }).catch((error) => {
          alert(`Error creating post: ${error.response.data}`);
        });
      },
      
    },
  };
  </script>
  