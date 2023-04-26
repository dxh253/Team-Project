<template>
    <div class="box" style="margin: 1% 10%; max-width: 70%;">
        <p style="color:gray;">{{ comment.date }} by {{ comment.username }}</p>
        <p style="margin:0% 3%; overflow-wrap: break-word;">{{ comment.text }}</p>
    </div>
</template>

<script>
export default {
    name: "ProblemComment",
    props: ["comment"],
}
</script>