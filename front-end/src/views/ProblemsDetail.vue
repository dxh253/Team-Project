<template>
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-10">
          <div class="box">
            <div class="columns is-mobile is-centered">
              <div class="column is-10">
                <h1 class="title is-size-2 has-text-weight-bold">{{ problems.title }}</h1>
              </div>
              <div v-if="owned" class="column is-2 has-text-right">
                <button class="button is-danger is-small" @click="deleteProblem">Delete</button>
              </div>
            </div>
            <p class="subtitle is-size-6 has-text-grey">{{ problems.date_added }} by {{ problems.author }}</p>
            <hr>
            <div class="content">
              <p style="white-space: pre-wrap; overflow-wrap: break-word;">{{ problems.description }}</p>
            </div>
          </div>
          <div class="box">
            <div class="is-flex is-justify-content-space-between is-align-items-center">
                <h2 class="title is-size-4 has-text-weight-bold">{{ allComments.length }} Responses</h2>
                <button class="button is-info" @click="showForm = !showForm">{{ showForm ? 'Hide' : 'Add' }} Response</button>
            </div>
            <form v-if="showForm" @submit.prevent="submitComment">
                <div class="field">
                <div class="control">
                    <textarea class="textarea" v-model="commentInfo.text" placeholder="Type your response here"></textarea>
                </div>
                </div>
                <div class="field has-text-right">
                <button class="button is-info" type="submit">Submit</button>
                </div>
            </form>
            <hr>
            <div class="content">
                <ProblemComment v-for="comment in allComments" :comment="comment" :key="comment.id" />
            </div>
            </div>
        </div>
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
            },
            showForm: false,
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

            if (confirm("Are you sure you want to delete this post? \n\nAll comments will be deleted as well.")) {
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
        },

        getComments() {
            console.log("trying to get comments")
            const problem_id = this.$route.params.problem_id

            getAPI
                .get(`/api/v1/help/${problem_id}/comments/`, {
                    headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
                })
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
            formData.append('problem', problem_id)
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
