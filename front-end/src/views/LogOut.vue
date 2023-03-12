<template>
    <div class="log">
    </div>
</template>

<script>
    export default {
        created(){
            this.$store.dispatch('userLogout')
            .then(() => {{
                this.$state.accessToken = null
                this.$router.push({name: 'Home'})
            }})
        }
    }
</script>