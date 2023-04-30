<!-- <template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <div class="main3">
        <p v-if="sessionExpired" class="session-expired">Your session has expired, please log in again.</p>
        <p v-if="incorrectAuth"> Incorrect username and/or password entered. Please try again.</p>
        <form @submit.prevent="login" class="login-form">
            <div class="form-group">
                <label for="email">Username:</label>
                <input type="text" id="email" name="username" v-model="username" required>
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
            <br>
            <RouterLink to="/forgot-password">
                Forgot Password?
            </RouterLink>
        </form>
    </div>

</template>

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
</script> -->


  
<template>
    <div class="container">
        <div class="box">
        <div class="columns">
          <div class="column is-half">
            <div class="description">
              <h1 class="title">Welcome to BrumConnect</h1>
            </div>
            <hr>
            <div class="columns">
              <div class="column is-half-desktop">
                <div class="box">
                  <p class="subtitle">Discussions</p>
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.</p>
                </div>
              </div>
              <div class="column is-half-desktop">
                <div class="box">
                  <p class="subtitle">Events</p>
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.</p>
                </div>
              </div>
            </div>
            <div class="columns">
              <div class="column is-half-desktop">
                <div class="box">
                  <p class="subtitle">Study Resources</p>
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.</p>
                </div>
              </div>
              <div class="column is-half-desktop">
                <div class="box">
                  <p class="subtitle">Study Groups</p>
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="column">
            <h1 class="title has-text-centered">Login</h1>
            <div class="login-form is-flex is-flex-wrap-wrap">
              <form @submit.prevent="login" class="box">
                <div class="field">
                  <label for="email" class="label">Username</label>
                  <input type="text" id="email" name="username" v-model="username" class="input" required>
                </div>
                <div class="field">
                  <label for="password" class="label">Password</label>
                  <input type="password" id="password" name="password" v-model="password" class="input" required>
                </div>
                <div class="field">
                  <button id="submit-button" type="submit" class="button is-success is-fullwidth">Login</button>
                </div>
                <div class="field">
                  <RouterLink to="/forgot-password">Forgot Password?</RouterLink>
                </div>
                <div class="field">
                  <span>Don't have an account?</span>
                  <RouterLink to="/register" class="button is-link is-outlined is-small ml-2">Register</RouterLink>
                </div>
                <p v-if="sessionExpired" class="help is-danger">Your session has expired, please log in again.</p>
                <p v-if="incorrectAuth" class="help is-danger">Incorrect username and/or password entered. Please try again.</p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  

  <script>
  export default {
    name: 'HomeView',
    data() {
      return {
        username: '',
        password: '',
        incorrectAuth: false,
        sessionExpired: false,
      };
    },
    mounted() {
      if (this.$route.query.sessionExpired) {
        this.sessionExpired = true;
      }
    },
    methods: {
      login() {
        this.$store.dispatch('userLogin', {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: 'Dashboard' });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
      },
    },
  };
  </script>

  
<style scoped>
    form {
        width: 500px;
        margin: 19px auto;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
        padding: 40px;
    }
</style>