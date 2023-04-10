<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <div class="main3">
        <p v-if="sessionExpired" class="session-expired">Your session has expired, please log in again.</p>
        <p v-if="incorrectAuth"> Incorrect username and/or password entered. Please try again.</p>
        <form @submit.prevent="login" class="login-form">
            <div class="form-group">
                <label for="email">Email address:</label>
                <input type="text" id="email" name="email" v-model="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" v-model="password" required>
            </div>
            <button id="submit-button" type="submit" to="/events">Login</button>
            <label for="dontHaveAccount">Don't have an account?</label>
            <RouterLink to="/register">
                <button id="register-button" type="submit" formaction="register">Register</button>
            </RouterLink>

        </form>
    </div>

    <div class="main2">
        <div class="event-card">
            <h3>Study Groups</h3>
            <p class="description">Join different study groups based on your course or academic interests and collaborate
                with peers to learn
            </p>
        </div>
        <div class="event-card">
            <h3>Resource</h3>
            <p class="description">Access and share a wealth of academic resources, such as study notes, textbooks, videos,
                and other materials.
            </p>
        </div>
        <div class="event-card">
            <h3>Discussion board</h3>
            <p class="description">Engage in discussions and debates with fellow students on a wide range of academic and
                campus life topics.
            </p>
        </div>
    </div>
</template>

<style>@import url('./../assets/HomeView.css');</style>


<script>
// import axios from 'axios';

export default {
    name: 'HomeView',
    data(){
        return{
            username: '',
            password: '',
            incorrectAuth: false,
            sessionExpired: false,
        }
    },
    mounted(){
        if (this.$route.query.sessionExpired) {
            this.sessionExpired = true;
  }
    },
    // Add the props section in your script
    methods:{
        login(){
            this.$store.dispatch('userLogin', {
                username: this.username,
                password: this.password
            })
            .then(() => {
                this.$router.push({name: 'Dashboard'})
            })
            .catch((err) => {
                console.log(err)
                this.incorrectAuth = true;
            })
        }
    }
}   
</script>