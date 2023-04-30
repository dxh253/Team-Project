<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <router-link :to="{ name: 'ProblemsDetail', params: { problem_id: problem.id } }">
      <div class="card box column is-three-fifths is-clickable" @click="viewProblem">
        <div class="card-content">
          <p class="title is-3 is-size-4-mobile">{{ problem.title }}</p>
          <p class="subtitle is-7 is-size-8-mobile">{{ problem.date_added }} by {{ problem.author }}</p>
          <div class="content">
            <p class="is-size-5 is-size-6-mobile">{{ problem.description }}</p>
          </div>
        </div>
      </div>
    </router-link>
  </template>
  <script>
  import { getAPI } from '@/plugins/axios';
  
  export default {
    name: "ProblemCard",
    props: ["problem"],
    methods: {
      viewProblem() {
        console.log("You pressed on card");
      },
      deleteProblem() {
        if (this.$parent.problemInfo.isOwner == true) {
          getAPI.delete("api/v1/help/", { headers: { "Authorization": `Bearer ${this.$store.state.accessToken}` } })
            .then(() => {
              window.location.reload();
            })
            .catch((error) => {
              if (error.response.status === 403) {
                alert("You are not authorized to delete this event.");
              } else {
                console.log(error);
              }
            });
        } else {
          alert("You are not the owner");
        }
      },
    },
  };
  </script>
  <style lang="scss" scoped>
  .card {
    margin: 1rem auto;
    max-width: 900px;
    border: none;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease-in-out;
  
    &:hover {
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }
  
    .card-content {
      padding: 1rem;
  
      .subtitle {
        margin-bottom: 0.5rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
  
      .content {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }
  }
  </style>
