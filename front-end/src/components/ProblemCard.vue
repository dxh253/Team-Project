<template>
    <div class="box" @click.right="viewProblem" style="max-width: 1000px; margin-left: 5%;">    
        <h3 class="is-size-4"> {{ problem.title }} </h3>
        <p class="is-size-6"> {{ problem.description }}</p>
    </div>
</template>

<script>

export default {
    name: 'ProblemCard',
    props: ['problem'],
    methods: {
        viewProblem() {
            
        }
    }
};

</script>