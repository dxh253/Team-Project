<template>
    <div class="post">
        <h1>Create a Post</h1>
        <form @submit.prevent="handleSubmit">
            <input class="input" id="title" v-model="title" type="text" required placeholder="Title">
            <br>
            <textarea class="description" id="description" v-model="description" placeholder="Description"
                rows="10"></textarea>
            <br>
            <div class="bottom">
                <!-- <button type="submit">Create Post</button> -->
                <br>
                <select class="category" id="category" v-model="category" required style="margin-left: auto;">
                    <option value="" disabled>Category</option>
                    <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}
                    </option>
                </select>                                                                                               
                <!-- <label class="image-selector" tabindex="0" @keydown.enter="onFileSelected"> -->
                    <!-- <i class="fa-solid fa-image fa-xl"></i> -->
                    <input type="file" @change="onFileSelected"/>
                <!-- </label> -->
                <div style="margin-left: auto; display: flex; align-items: center;">
                    <p>Sensitive Content ?</p>
                    <label class="switch" tabindex="0" @keydown.enter="toggleBlur">
                    <input type="checkbox" id="isBlurred" v-model="isBlurred" @keydown.enter="toggleBlur">
                    <span class="slider round"></span>
                    </label>
                </div>
                <button type="submit">Create Post</button>
            </div>
        </form>
    </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';
import jwt_decode from "jwt-decode";

export default {
    data() {
        return {
            title: '',
            description: '',
            owner: '',
            category: '',
            categories: [],
            image: null,
            isBlurred: false,
        };
    },
    mounted() {
        this.fetchCategories();
    },
    methods: {
        fetchCategories() {
            getAPI.get('/api/v1/categories/')
                .then(response => {
                    this.categories = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        toggleBlur(event) {
  if (event.type === 'click' || (event.type === 'keydown' && event.key === 'Enter')) {
    this.isBlurred = !this.isBlurred;
  }
},
        handleSubmit() {
            // Decode the JWT token to get the user ID
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

            getAPI
                .post("/api/v1/posts/", payload, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                        'Content-Type': 'multipart/form-data',
                    },
                })
                .then(() => {
                    alert("Post created successfully!");
                    this.$router.push("/posts"); // Redirect to homepage or wherever you want
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
</script>

<style>
@import url('./../assets/PostCreate.css');
</style>
