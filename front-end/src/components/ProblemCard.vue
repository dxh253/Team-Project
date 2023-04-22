<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <div>
        <div class="box column is-three-fifths" @click="viewProblem" style="display: inline-table; ">
            <div>
                <p class="is-size-3">{{ problem.title }}</p>
                <p class="is-size-7">{{ problem.date_added }}</p>
            </div>
            <p class="is-size-5" style="overflow: hidden; text-overflow: ellipsis; margin-right:10% ;"> {{
                problem.description }}</p>
        </div>
        <i class="column is-1 material-icons deleting" style="font-size: 35px;" @click="deleteProblem">delete</i>
    </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';



export default {
    name: 'ProblemCard',
    props: ['problem'],
    methods: {
        viewProblem() {
            console.log("You pressed on card")
        },

        deleteProblem() {

            if (this.$parent.problemInfo.isOwner == true) {
                getAPI
                    .delete('api/v1/help',
                        { headers: { 'Authorization': `Bearer ${this.$store.state.accessToken}` } },
                    )
                    .then(() => {
                        window.location.reload();
                    })
                    .catch((error) => {
                        if (error.response.status === 403) {
                            alert('You are not authorized to delete this event.');
                        } else {
                            console.log(error);
                        }
                    });
            }
            else alert("You are not the owner")
        }
    }
};

</script>

<style scoped>
.box {
    margin-left: 4.3%;
    text-indent: 1%;
}

.box:hover {
    font-weight: bold;
}

.test:hover {
    font-weight: bold;
}

.deleting:hover {
    color: darkred;
    cursor: pointer;
}
</style>
