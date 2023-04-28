<template>
  <div>
    <h1>Account Registration</h1>
    <form @submit.prevent="registerUser" method="post">
      <label for="first-name">First name:</label>
      <input
        type="text"
        name="first_name"
        id="first-name"
        v-model="firstName"
        required
      />
      <label for="surname">Surname:</label>
      <input
        type="text"
        name="surname"
        id="surname"
        v-model="surname"
        required
      />
      <label for="username">Username:</label>
      <input
        type="text"
        name="username"
        id="username"
        v-model="username"
        required
      />
      <label for="email">Email:</label>
      <input type="email" name="email" id="email" v-model="email" required />
      <label for="password1">Password:</label>
      <input
        type="password"
        name="password1"
        id="password1"
        v-model="password1"
        required
      />
      <label for="password2">Confirm Password:</label>
      <input
        type="password"
        name="password2"
        id="password2"
        v-model="password2"
        required
      />
      <div class="field">
        <div class="control">
          <label class="checkbox">
            <input
              type="checkbox"
              name="privacy_policy"
              v-model="privacyPolicy"
              required
            />
            I agree to the <a href="/privacy_policy">privacy policy</a>.
          </label>
        </div>
      </div>
      <button id="register-button" type="submit">Register</button>
    </form>
  </div>
</template>

<style>
@import url("./../assets/registration.css");
</style>

<script>
// import axios from 'axios';
import { getAPI } from "@/plugins/axios";

export default {
  name: "RegisterForm",
  data() {
    return {
      firstName: "asdf",
      surname: "asdf",
      username: "asdf",
      email: "asdf@asdf.com",
      password1: "asdf",
      password2: "asdf",
    };
  },
  methods: {
    registerUser() {
      getAPI
        .post("api/v1/register/", {
          first_name: this.firstName,
          last_name: this.surname,
          username: this.username,
          email: this.email,
          password: this.password1,
        })
        .then((response) => {
          console.log(response.data);
          this.$router.push({ name: "EventsView" });
        })
        .catch((error) => {
          console.log(error.response.data);
          this.incorrectAuth = true;
        });
    },
  },
};
</script>
