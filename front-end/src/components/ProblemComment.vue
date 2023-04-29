<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <div class="columns">
        <form class="box" style="margin: 1% 10%; min-width: 70%; max-width: 70%;">
            <p style="color:gray;">{{ comment.date }} by {{ comment.username }}</p>
            <p style="margin:0% 3%; overflow-wrap: break-word;">{{ comment.text }}</p>
        </form>
        <i v-show="owned" class="column is-1 material-icons deleting is-clickable" @click="deleteComment">delete</i>
    </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';
import jwtDecode from "jwt-decode";

export default {
    name: "ProblemComment",
    props: ["comment"],
    data() {
        return {
            owned: false,
        }
    },
    methods: {
        deleteComment() {
            const problem_id = this.$route.params.problem_id

            getAPI
                .delete(`api/v1/help/${problem_id}/comments/${this.comment.id}/`,
                    { headers: { "Authorization": `Bearer ${this.$store.state.accessToken}` } })
                .then(() => {
                    window.location.reload();
                })
                .catch((error) => {
                    if (error.response.status === 403) {
                        alert("You are not authorized to delete this problem.");
                    }
                    else {
                        console.log(error);
                    }
                })
        },
    },
    mounted() {
        const token = this.$store.state.accessToken;
        const decodedToken = jwtDecode(token);
        const userId = decodedToken.user_id;

        if(this.comment.author === userId){
            this.owned = true;
        }
    }
}
</script>

<style scoped>
.deleting:hover {
    color: darkred;
    cursor: pointer;
}
</style>