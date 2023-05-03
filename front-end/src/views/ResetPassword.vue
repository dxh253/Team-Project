<!-- <template>
    <div>
        <h2>Reset Password</h2>
        <form @submit.prevent="submitForm">
            <label>New Password:</label>
            <input type="password" v-model="password">
            <label>Confirm Password:</label>
            <input type="password" v-model="confirmPassword">
            <button type="submit">Reset Password</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            password: '',
            confirmPassword: '',
            resetToken: '' // The reset token will be passed as a prop from the URL
        }
    },
    methods: {
        async submitForm() {
            if (this.password !== this.confirmPassword) {
                alert('Passwords do not match')
                return
            }

            const response = await fetch(`/api/reset-password/${this.resetToken}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    password: this.password
                })
            })

            if (response.ok) {
                alert('Password reset successfully')
                // Redirect the user to the login page or home page
            } else {
                alert('Failed to reset password')
            }
        }
    }
}
</script> -->

<!-- <template>
    <div>
        <h2>Reset Password</h2>
        <form @submit.prevent="submitForm">
            <label>New Password:</label>
            <input type="password" v-model="password">
            <label>Confirm Password:</label>
            <input type="password" v-model="confirmPassword">
            <button type="submit">Reset Password</button>
        </form>
    </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';

export default {
    computed: {
        resetToken() {
            return this.$route.params.token
        }
    },
    data() {
        return {
            password: '',
            confirmPassword: '',
        }
    },
    methods: {
        async submitForm() {
            if (this.password !== this.confirmPassword) {
                alert('Passwords do not match');
                return;
            }

            try {
                const response = await getAPI.post(`/api/v1/reset-password/${this.$route.params.token}/`, {
                    password: this.password,
                });

                if (response.status === 200) {
                    alert('Password reset successfully');
                    // Redirect the user to the login page or home page
                } else {
                    alert('Failed to reset password');
                }
            } catch (error) {
                console.error('Error resetting password', error);
                alert('Failed to reset password');
            }
        },
    }
}
</script> -->

<template>
    <div>
        <h2>Reset Password</h2>
        <form @submit.prevent="submitForm">
            <label>New Password:</label>
            <input type="password" v-model="password">
            <label>Confirm Password:</label>
            <!-- <input type="password" v-model="confirmPassword"> -->
            <button type="submit">Reset Password</button>
        </form>
    </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';

export default {
    computed: {
        resetToken() {
            return this.$route.params.token
        }
    },
    data() {
        return {
            password: '',
            confirmPassword: '',
        }
    },
    methods: {
        async submitForm() {
            console.log('Password:', this.password);
            // console.log('Confirm Password:', this.confirmPassword);

            // if (this.password !== this.confirmPassword) {
            //     alert('Passwords do not match');
            //     return;
            // }

            try {
                const response = await getAPI.post(`/api/v1/reset-password/${this.$route.params.token}/`, {
                    password: this.password,
                });

                if (response.status === 200) {
                    alert('Password reset successfully');
                    this.$router.push({ name: 'Login' });
                } else {
                    alert('Failed to reset password');
                }
            } catch (error) {
                console.error('Error resetting password', error);
                alert('Failed to reset password');
            }
        },
    }
}
</script>