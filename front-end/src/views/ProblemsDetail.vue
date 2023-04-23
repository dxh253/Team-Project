<template>
    <div>
        <div class="box" style="margin:0 5%">
            <p class="is-size-1" style="text-indent: 5%;">{{ problems.title }}</p>
            <p class="is-size-6" style="text-indent: 5%;">{{ problems.description }}</p>
        </div>
    </div>
</template>

<script>
import { getAPI } from '@/plugins/axios';

export default {
    name: 'ProblemsDetail',
    data() {
        return {
            problems: {},
        }
    },
    mounted() {
        this.getProblems()
    },
    methods: {
        getProblems() {
            const problem_id = this.$route.params.problem_id

            getAPI
                .get(`api/v1/help/${problem_id}`,
                    { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                .then(response => {
                    this.problems = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>