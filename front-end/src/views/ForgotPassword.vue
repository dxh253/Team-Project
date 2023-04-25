<template>
    <div>
        <h1>Forgot Password</h1>
        <form @submit.prevent="forgotPassword">
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" v-model="email" required>
            <button id="submit-button" type="submit">Submit</button>
        </form>
        <p>{{ message }}</p>
    </div>
</template>

<script>
    import { getAPI } from "@/plugins/axios";

    export default {
        name: 'ForgotPassword',
        data() {
            return {
                email: '',
                message: '',
            }
        },
        methods: {
            forgotPassword() {
                getAPI.post('/api/v1/forgot-password/', {
                    email: this.email,
                })
                    .then(response => {
                        console.log(response.data)
                        this.message = response.data.message
                    })
                    .catch(error => {
                        console.log(error.response.data)
                        this.message = error.response.data.message
                    })
            }
        }
    }
</script>
