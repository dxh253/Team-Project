<!-- <template>
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
            <label for="password1">Password:</label>
            <input type="password" name="password1" id="password1" v-model="password1" required>
            <div class="field">
                <div class="control">
                    <label class="checkbox">
                        <input type="checkbox" name="privacy_policy" v-model="privacyPolicy" required>
                        I agree to the <a href="/privacy_policy">privacy policy</a>.
                    </label>
                </div>
            </div>
            <button id="register-button" type="submit">Register</button>
        </form>
    </div>
</template>

<style>
@import url('./../assets/registration.css');
</style>

<script>
// import axios from 'axios';
import { getAPI } from '@/plugins/axios'

export default {
    name: 'RegisterForm',
    data() {
        return {
            firstName: '',
            surname: '',
            username: '',
            email: '',
            password1: '',
        };
    },
    methods: {
        registerUser() {
            getAPI.post('api/v1/register/', {
                first_name: this.firstName,
                last_name: this.surname,
                username: this.username,
                email: this.email,
                password: this.password1,
            })
                .then(response => {
                    console.log(response.data);
                    this.$router.push({ name: 'EventsView' });
                })
                .catch(error => {
                    const data = error.response.data;
                    // Terrible way to do it, but oh well.
                    if (
                        data.username &&
                        data.username[0] === "A user with that username already exists."
                    ) {
                        alert("Username taken");
                    }
                    if (data[0] === "This email is already in use.") {
                        alert("Email taken");
                    }
                    this.incorrectAuth = true;
                });
        },
    },
};
</script> -->

<template>
    <div>
        <h1>Account Registration</h1>
        <p v-if="weakPassword" class="session-expired" style="text-align: center;">Password needs to be at least 8
            characters long.</p>
        <form @submit.prevent="registerUser" method="post">
            <label for="first-name">First name:</label>
            <input type="text" name="first_name" id="first-name" v-model="firstName" required>
            <label for="surname">Surname:</label>
            <input type="text" name="surname" id="surname" v-model="surname" required>
            <label for="username">Username:</label>
            <input type="text" name="username" id="username" v-model="username" required>
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" v-model="email" required>
            <label for="password1">Password:</label>
            <input type="password" name="password1" id="password1" v-model="password1" required>
            <div class="field">
                <div class="control">
                    <label class="checkbox">
                        <input type="checkbox" name="privacy_policy" v-model="privacyPolicy" required>
                        I agree to the <a href="/privacy_policy">privacy policy</a>.
                    </label>
                </div>
            </div>
            <button id="register-button" type="submit">Register</button>
        </form>
    </div>
</template>

<style>
@import url('./../assets/registration.css');
</style>

<script>
import { getAPI } from '@/plugins/axios'

export default {
    name: 'RegisterForm',
    data() {
        return {
            firstName: '',
            surname: '',
            username: '',
            email: '',
            password1: '',
            privacyPolicy: false,
        };
    },
    computed: {
        weakPassword() {
            return this.password1.length < 8;
        },
    },
    methods: {
        registerUser() {
            if (this.password1.length < 8) {
                this.weakPassword = true;
                console.log("Password too short");
                return;
            }

            getAPI.post('api/v1/register/', {
                first_name: this.firstName,
                last_name: this.surname,
                username: this.username,
                email: this.email,
                password: this.password1,
            })
                .then(response => {
                    console.log(response.data);
                    this.$router.push({ name: 'Dashboard' });
                })
                .catch(error => {
                    const data = error.response.data;
                    // Terrible way to do it, but oh well.
                    if (
                        data.username &&
                        data.username[0] === "A user with that username already exists."
                    ) {
                        alert("Username taken");
                    }
                    if (data[0] === "This email is already in use.") {
                        alert("Email taken");
                    }
                    this.incorrectAuth = true;
                });
        },

    },
};
</script>