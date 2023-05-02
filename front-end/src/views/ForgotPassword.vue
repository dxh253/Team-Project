<!-- <template>
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
</script> -->

<template>
    <div>
        <h2>Forgot Password</h2>
        <form @submit.prevent="submitForm">
            <label>Email Address:</label>
            <input type="email" v-model="email">
            <button type="submit">Reset Password</button>
        </form>
    </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';
export default {
    data() {
        return {
            email: '',
        };
    },
    methods: {
        submitForm() {
            // Send email to initiate password reset
            getAPI.post('/api/v1/forgot-password/', { email: this.email })
                .then(response => {
                    alert('Password reset email sent');
                    console.log(response.data);
                })
                .catch(error => {
                    console.log('Error sending password reset email');
                    console.log(error.response.data);
                });
        },
    },
};
</script>