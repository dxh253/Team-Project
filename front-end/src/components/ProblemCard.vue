<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <div>
        <router-link 
        :to="{ name: 'ProblemsDetail', params: { problem_id: problem.id } }"
        class="box column is-three-fifths is-clickable" @click="viewProblem"
        style="display: inline-table; margin-bottom: 1%;">
            <div>
                <p class="is-size-3" style="margin-left: 1%;">{{ problem.title }}</p>
                <p class="is-size-7" style="margin-left: 1%;">{{ problem.date_added }} by {{ problem.author }}</p>
            </div>
            <p
            class="is-size-5" 
            style="overflow: hidden; text-overflow: ellipsis; margin-right:10%;margin-left: 1%; white-space: nowrap; max-width: 850px;"> 
                {{ problem.description }}
            </p>
        </router-link>
    </div>
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
                getAPI
                    .delete("api/v1/help/", { headers: { "Authorization": `Bearer ${this.$store.state.accessToken}` } })
                    .then(() => {
                        window.location.reload();
                    })
                    .catch((error) => {
                        if (error.response.status === 403) {
                            alert("You are not authorized to delete this event.");
                        }
                        else {
                            console.log(error);
                        }
                    });
            }
            else
                alert("You are not the owner");
        }
    },
};

</script>

<style scoped>
.box {
    margin-left: 4.3%;
    min-width: 900px;
}

.box:hover {
    font-weight: bold;
}
</style>