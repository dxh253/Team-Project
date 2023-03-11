<template>
    <div class="studyGroups">
        <h1>Study groups</h1>
    </div>
    <li v-for="item in d">{{ item.title }} : {{ item.content }}</li>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            d: "",
        };
    },

    mounted() {
        axios.get("/api/study_groups/").then((response) => {
            console.log(response);
            this.d = response.data;
        });
    },
};
</script>
