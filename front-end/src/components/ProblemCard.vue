<template>
    <div class="box" @click.right="viewProblem">
        <h3 class="is-size-5"> {{ problem.title }} </h3>
        <p class="is-size-6"> {{ problem.description }}</p>
    </div>
</template>

<script>
export default {
    name: 'ProblemCard',
    methods: {
        viewProblem() {
            
        }
    }
}

</script>