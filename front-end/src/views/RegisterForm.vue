<template>
    <div>
        <h1>Account Registration</h1>
        <form @submit.prevent="registerUser" method="post">
            <label for="first-name">First name:</label>
            <input type="text" name="first_name" id="first-name" v-model="firstName" required>
            <label for="surname">Surname:</label>
            <input type="text" name="surname" id="surname" v-model="surname" required>
            <label for="username">Username:</label>
            <input type="text" name="username" id="username" v-model="username" required>
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" v-model="email" required>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password" v-model="password" required>
            <!-- <label for="password2">Confirm Password:</label>
            <input type="password" name="password2" id="password2" v-model="password2" required> -->
            <button id="register-button" type="submit">Register</button>
        </form>
    </div>
</template>

<style>
@import url('./../assets/registration.css');
</style>

<script>
import axios from 'axios';
const BASE_URL = 'https://team22-22.bham.team/api/v1/';
// const BASE_URL = process.env.VUE_APP_BASE_URL;
export default {
    name: 'RegisterForm',
    data() {
        return {
            firstName: 'asdf',
            surname: 'asdf',
            username: 'asdf',
            email: 'asdf@asdf.com',
            password: 'asdf',
            // password2: 'asdf',
        };
    },
    // methods: {
    //     registerUser() {
    //         axios.post('http://127.0.0.1:8000/api/v1/register/', {
    //             withCredentials: true,
    //             first_name: this.firstName,
    //             last_name: this.surname,
    //             username: this.username,
    //             email: this.email,
    //             password: this.password1,
    //         },
    //         {
    //             headers:{
    //                 'Access-Control-Allow-Origin': '*',
    //                 'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    //                 'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token',
    //             }
    //         })
    //             .then(response => {
    //                 console.log(response.data);
    //                 this.$router.push({name: 'EventsView'});
    //             })
    //             .catch(error => {
    //                 console.log(error.response.data);
    //                 this.incorrectAuth = true;
    //             });
    //     },
    // },
    methods: {
        async registerUser() {
            try {
                // const token = "Bearer " + localStorage.getItem("token");
                const response = await axios.post(`${BASE_URL}register/`, {
                    
                    first_name: this.firstName,
                    surname: this.surname,
                    username: this.username,
                    email: this.email,
                    password: this.password,
                    // password2: this.password2,
                },
                {
                    headers:{
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                        'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token, Authorization', 
                    }
                });
                console.log(response.data);
            } catch (error) {
                console.error(error);
            }
        },
    },
};
</script>