<template>
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-two-thirds-mobile is-half-tablet is-one-third-desktop">
          <h1 class="title has-text-centered">Account Registration</h1>
          <form @submit.prevent="registerUser" method="post">
            <div class="field">
              <label class="label" for="first-name">First name:</label>
              <div class="control">
                <input class="input" type="text" name="first_name" id="first-name" v-model="firstName" required>
              </div>
            </div>
            <div class="field">
              <label class="label" for="surname">Surname:</label>
              <div class="control">
                <input class="input" type="text" name="surname" id="surname" v-model="surname" required>
              </div>
            </div>
            <div class="field">
              <label class="label" for="username">Username:</label>
              <div class="control">
                <input class="input" type="text" name="username" id="username" v-model="username" required>
              </div>
            </div>
            <div class="field">
              <label class="label" for="email">Email:</label>
              <div class="control">
                <input class="input" type="email" name="email" id="email" v-model="email" required>
              </div>
            </div>
            <div class="field">
              <label class="label" for="password1">Password:</label>
              <div class="control">
                <input class="input" type="password" name="password1" id="password1" v-model="password1" required>
              </div>
            </div>
            <div class="field">
              <label class="label" for="password2">Confirm Password:</label>
              <div class="control">
                <input class="input" type="password" name="password2" id="password2" v-model="password2" required>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <label class="checkbox">
                  <input type="checkbox" name="privacy_policy" v-model="privacyPolicy" required>
                  I agree to the <a href="/privacy_policy">privacy policy</a>.
                </label>
              </div>
            </div>
            <div class="field">
              <div class="control has-text-centered">
                <button class="button is-primary" type="submit">Register</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  @media screen and (max-width: 768px) {
    .column.is-two-thirds-mobile {
      width: 100%;
    }
  }
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
            password2: '',
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
</script>

