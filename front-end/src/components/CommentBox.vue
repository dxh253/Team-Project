<template>
    <div class="comment-container">
        <div class="comments">
            <div v-if="comments.length === 0">No comments yet.</div>
            <div v-else>
                <div v-for="comment in comments" :key="comment.id" class="comment">
                    <div class="comment-header">
                        <h3 class="comment-owner">{{ comment.owner }}</h3>
                    </div>
                    <div class="comment-body">
                        <p>{{ comment.text }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<style lang="scss">
.comment-container {
    margin-top: 1.5rem;
}

.comment {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 1rem;
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
}

.comment-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.5rem;
}

.comment-owner {
    font-size: 1.125rem;
    font-weight: bold;
    margin-right: 0.5rem;
}

.comment-body {
    font-size: 1rem;
    line-height: 1.5;
    color: #555;
}
</style>
  
<script>
export default {
    name: "CommentBox",
    props: {
        comments: {
            type: Array,
            default: () => [],
        },
    },
};
</script>
