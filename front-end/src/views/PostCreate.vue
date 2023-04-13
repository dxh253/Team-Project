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
                <button type="submit">Create Post</button>
                <br>
                <select class="category" id="category" v-model="category" required>
                    <option value="" disabled>Category</option>
                    <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}
                    </option>
                </select>
                <input type="file" @change="onFileSelected"/>
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
        onFileSelected(event) {
            this.get_image = event.target.files[0];
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
            };

            getAPI
                .post("/posts/", payload, {
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
