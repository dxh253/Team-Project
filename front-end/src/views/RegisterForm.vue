<template>
    <link rel="stylesheet" href="./../assets/registration.css">
    <div>
        <h1>Account Registration</h1>
        <form @submit.prevent = "RegisterForm" method="post">
            <!-- {% csrf_token %}
        {% if error_message %}
        <p class="error">{{ error_message }}</p>
        {% endif %}
        {% if success_message %}
        <p class="success">{{ success_message }}</p>
        {% endif %} -->
            <label for="username">First name:</label>
            <input type="text" name="first name" id="first-name" v-model = "firstName" required>
            <label for="username">Surname:</label>
            <input type="text" name="surname" id="surname" v-model = "secondName" required>
            <label for="username">Username:</label>
            <input type="text" name="username" id="username" v-model = "username" required>
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" v-model = "email" required>
            <label for="password1">Password:</label>
            <input type="password" name="password1" id="password1" v-model = "password1" required>
            <label for="password2">Confirm Password:</label>
            <input type="password" name="password2" id="password2" v-model = "password2" required>
            <button id="register-button" type="submit">Register</button>
        </form>
    </div>
</template>

<style>
@import url('./../assets/registration.css');
</style>

<script>
// import axios from 'axios';
export default {
    name: 'RegisterForm',
    /*data(){
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        RegisterForm(e){
            e.preventDefault();
            const formData = {
                username: this.username,
                password: this.password,
            }

            axios 
                .post('/api/v1/users/', formData)
                .then(response => {
                    this.$router.push('')
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }*/
};
</script>


<!-- <template>
    <div>
        <h1>Account Registration</h1>
        <form @submit.prevent="register">
            <label for="first-name">First name:</label>
            <input type="text" name="first_name" v-model="firstName" required>
            <label for="surname">Surname:</label>
            <input type="text" name="surname" v-model="surname" required>
            <label for="username">Username:</label>
            <input type="text" name="username" v-model="username" required>
            <label for="email">Email:</label>
            <input type="email" name="email" v-model="email" required>
            <label for="password1">Password:</label>
            <input type="password" name="password1" v-model="password1" required>
            <label for="password2">Confirm Password:</label>
            <input type="password" name="password2" v-model="password2" required>
            <button type="submit">Register</button>
        </form>
    </div>
</template> -->

<!-- <script>
export default {
    name: 'RegisterForm',
    data() {
    return {
        firstName: '',
        surname: '',
        username: '',
        email: '',
        password1: '',
        password2: '',
    };
    },
    methods: {
        submitForm() {
            // Send formData to backend server for processing
            console.log(this.formData);
        }, -->
    // register() {
    //   // Send the data to the backend using axios or any other HTTP library
    //     const formData = {
    //     first_name: this.firstName,
    //     surname: this.surname,
    //     username: this.username,
    //     email: this.email,
    //     password1: this.password1,
    //     password2: this.password2,
    //     };
    //   // send the formData object to the backend using axios or any other HTTP library
    // },
    },
};
<!-- </script> -->

<!-- <style>
@import url('./../assets/registration.css');
</style> -->
