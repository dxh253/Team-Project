<template>
    <form class="box" style="margin: 1% 10%; min-width: 70%; max-width: 70%;">
        <p style="color:gray;">{{ comment.date }} by {{ comment.username }}</p>
        <p style="margin:0% 3%; overflow-wrap: break-word;">{{ comment.text }}</p>
    </form>
</template>

<script>
export default {
    name: "ProblemComment",
    props: ["comment"],
}
</script>