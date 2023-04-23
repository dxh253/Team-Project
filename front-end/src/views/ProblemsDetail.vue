<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <div>
        <div class="box" style="margin:0 5%">
            <div class="columns">
                <p class="is-size-1 column is-10" style="text-indent: 5%;">{{ problems.title }}</p>
                <i v-show="owned"
                class="column is-1 material-icons deleting" 
                style="font-size: 35px; display: grid; align-self: center; text-align: end;" @click="deleteProblem">delete</i>
            </div>
                <p class="is-size-6" style="text-indent: 5%;">{{ problems.date_added }}</p>
                <p class="is-size-6" style="text-indent: 5%;">{{ problems.description }}</p>
        </div>
        
    </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';
import jwt_decode from "jwt-decode";

export default {
    name: 'ProblemsDetail',
    data() {
        return {
            problems: {},
            owned: false,
        }
    },
    mounted() {
        this.getProblems()
    },
    methods: {
        getProblems() {
            const problem_id = this.$route.params.problem_id
            const token = this.$store.state.accessToken;
            const decodedToken = jwt_decode(token);
            const userId = decodedToken.user_id;

            getAPI
                .get(`api/v1/help/${problem_id}/`,
                { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                .then(response => {
                    this.problems = response.data
                    if (this.problems.owner === userId) {
                        this.owned = true;
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        },
        
        deleteProblem() {
            const problem_id = this.$route.params.problem_id

            getAPI
                .delete(`api/v1/help/${problem_id}/`, 
                { headers: { "Authorization": `Bearer ${this.$store.state.accessToken}` } })
                .then(() => {
                window.history.back();
                })
                .catch((error) => {
                if (error.response.status === 403) {
                    alert("You are not authorized to delete this problem.");
                }
                else {
                    console.log(error);
                }
                })
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