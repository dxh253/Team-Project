<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <div>
        <div class="box" style="margin:0 5%">
            <div class="columns">
                <p class="is-size-1 column is-10" style="text-indent: 5%;">{{ problems.title }}</p>
                <i v-show="owned" class="column is-1 material-icons deleting"
                    style="font-size: 35px; display: grid; align-self: center; text-align: end;"
                    @click="deleteProblem">delete</i>
            </div>
            <p class="is-size-6" style="margin-left: 4%; margin-bottom: 1%;">{{ problems.date_added }} by {{ problems.author }}</p>
            <p class="is-size-6" 
            style="margin-left: 4%; margin-right: 20%; overflow-wrap: break-word;">{{ problems.description }}</p>
        </div>
        <form class="box" @submit.prevent="submitComment" style="margin:1% 10%; min-width: 70%; max-width: 70%;">
            <textarea class="textarea" v-model="commentInfo.text" placeholder="add response"></textarea>
            <div style="text-align: right; margin-top: 5px;">
            <button class="button is-info" type="submit"> Submit </button>
            </div>
        </form>
        <div>
            <ProblemComment v-for="comment in allComments" :comment="comment" :key="comment.id" />
        </div>
    </div>
</template>

<script>
import ProblemComment from '@/components/ProblemComment.vue';
import { getAPI } from '@/plugins/axios';
import jwt_decode from "jwt-decode";

export default {
    name: 'ProblemsDetail',
    data() {
        return {
            problems: {},
            owned: false,
            allComments: [],
            commentInfo: {
                text: '',
            }
        }
    },
    components: {
        ProblemComment,
    },
    mounted() {
        this.getProblems();
        this.getComments();
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
                    console.log(this.problems);
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
        },

        getComments() {
            console.log("trying to get comments")
            const problem_id = this.$route.params.problem_id

        getAPI
            .get(`/api/v1/help/${problem_id}/comments/`,{
            headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },})
            .then((response) => {
                console.log('API respinse data:', response.data);
                this.allComments = response.data;
                this.$store.state.APIData = response.data;
            })
            .catch((error) => {
                console.log('API error:', error);
            });
        },

        submitComment() {
            console.log("Submit comment");
            const problem_id = this.$route.params.problem_id
            const token = localStorage.getItem("access");
            const decodedToken = jwt_decode(token);
            const ownerId = decodedToken.user_id;

            if (!this.$store.getters.loggedIn) {
                //User is not logged in
                return;
            }

            console.log(this.commentInfo.text)

            const formData = new FormData();
            formData.append('problem',problem_id)
            formData.append('text', this.commentInfo.text)
            formData.append('author', ownerId)
            getAPI
                .post(`api/v1/help/${problem_id}/comments/`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        'Authorization': `Bearer ${this.$store.state.accessToken}`,
                    }
                })
                .then((response) => {
                    console.log('API response data:', response.data);
                    window.location.reload()
                })
                .catch((error) => {
                    console.log(error.response.data);
                    alert('Something went wrong. Please try again.')
                })
        }
    },
}
</script>

<style scoped>
.deleting:hover {
    color: darkred;
    cursor: pointer;
}
</style>