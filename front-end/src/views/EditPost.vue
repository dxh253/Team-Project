<template>
  <div class="post">
    <h1>Edit your Post</h1>
    <form @submit.prevent="handleSubmit">
      <input class="input" id="title" v-model="title" type="text" required placeholder="Title">
      <br>
      <textarea class="description" id="description" v-model="description" placeholder="Description" rows="10"></textarea>
      <br>
      <div class="bottom">
        <br>
        <select class="category" id="category" v-model="category" required>
          <option value="" disabled>Category</option>
          <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}
          </option>
        </select>
        <label class="image-selector">
          <i class="fa-solid fa-image fa-xl"></i>
          <input type="file" @change="onFileSelected" style="display:none" />
        </label>
        <div style="margin-left: auto; display: flex; align-items: center;">
          <p style="padding: 9px;">Sensitive Content ?</p>
          <label class="switch">
            <input type="checkbox" id="isBlurred" v-model="isBlurred">
            <span class="slider round"></span>
          </label>
        </div>
        <button type="submit" @click.prevent="editPost">Edit Post</button>
      </div>
    </form>
  </div>
</template>
  
  <script>
  import { getAPI } from '@/plugins/axios';
  import jwt_decode from "jwt-decode";

  export default {
    name: 'EditPost',
    data(){
      return{
        title: '',
        description: '',
        owner: '',
        category: '',
        categories: [],
        image: null,
        isBlurred: false,
      }
    },
    mounted(){
      this.fetchCategories();
    },
    // component logic goes here
    methods:{
      onFileSelected(event) {
        this.get_image = event.target.files[0];
      },
      fetchCategories() {
        getAPI.get('/api/v1/categories/')
          .then(response => {
            this.categories = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      },
      editPost() {
        const token = localStorage.getItem("access");
        const decodedToken = jwt_decode(token);
        const userId = decodedToken.user_id;

        const payload = {
          title: this.title,
          description: this.description,
          category: this.category,
          owner: userId,
          get_image: this.get_image,
          isBlurred: this.isBlurred,
        };
        getAPI.put(`/api/v1/posts/${this.$route.params.id}/`, payload, {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
            "Content-Type": "multipart/form-data",
          },
        })
          .then((response) => {
            this.title = response.data.title;
            this.description = response.data.description;
            this.category = response.data.category;
            this.get_image = response.data.get_image;
            this.isBlurred = response.data.isBlurred;
            this.$router.push("/posts");
          })
          .catch((error) => {
            alert("Something went wrong, please try again later.");
            console.log(error);
          });
      },
    },
  }
  </script>

<style>
@import url('./../assets/PostCreate.css');
</style>
  