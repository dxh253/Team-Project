<template>
    <div>
        <router-link :to="{ name: 'ProblemsDetail', params: { problem_id: problem.id } }"
         class="box column is-three-fifths is-clickable"
         style="display: inline-table; margin-bottom: 1%; ">
            <div>   
                <p class="is-size-3">{{ problem.title }}</p> 
                <p class="is-size-7">{{ problem.date_added }} {{ problem.author }}</p>
            </div>
            <p class="is-size-5" style="overflow: hidden; text-overflow: ellipsis; margin-right:10% ;"> {{ problem.description }}</p>
        </router-link>
    </div>
</template>

<script>


export default {
    name: "ProblemCard",
    props: ["problem"],
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
</style>