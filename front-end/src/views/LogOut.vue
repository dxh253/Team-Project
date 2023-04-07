<template>
    <div class="log">
    </div>
</template>

<!-- <script>
    export default {
        created(){
            this.$store.dispatch('userLogout')
            .then(() => {{
                this.$state.accessToken = updateStorage('accessToken', null)
                this.$router.push({name: 'Login'})
            }})
        }
    }
</script> -->

<script>
    export default {
        created () {
        this.$store.dispatch('userLogout')
            .then(() => {
            this.$router.push({ name: 'Login' })
            })
        }
    }
</script>