<template>
    <div class="comment-container">
        <div class="comments">
            <div v-if="comments.length === 0">No comments yet.</div>
            <div v-else>
                <div v-for="comment in parentComments" :key="comment.id" class="comment">
                    <div class="comment-header">
                        <h3 class="comment-owner">{{ comment.owner }}</h3>
                    </div>
                    <div class="comment-body">
                        <p>{{ comment.text }}</p>
                    </div>
                    <button @click="showReplyForm(comment.id)" class="button is-small is-light">
                        Reply
                    </button>
                    <button v-if="isOwner(comment)" @click="deleteComment(comment.id)" class="button is-small is-danger">
                    Delete
                    </button>
                    <div v-if="visibleReplyForm === comment.id" class="reply-form">
                        <textarea class="textarea" v-model="replyText[comment.id]"
                            placeholder="Write your reply here"></textarea>
                        <button @click="submitReply(comment.id)" class="button is-small is-primary">
                            Submit
                        </button>
                    </div>
                    <!-- This section shows the children comments only. -->
                    <div class="replies" v-if="comment.children && comment.children.length > 0">
                        <div v-for="reply in comment.children" :key="reply.id" class="reply">
                            <div class="reply-footer">
                                <span class="reply-owner">{{ reply.owner }}</span>
                            </div>
                            <div class="reply-body">
                                <span v-for="word in reply.text.split(' ')" :key="word">
                                    <span v-if="word[0] == '@'" style="color: #0000ee">{{ word }}&nbsp;
                                    </span>
                                    <span v-else>{{ word }}&nbsp;</span>
                                </span>
                                <span>&nbsp;</span>
                            </div>
                            <button @click="showReplyForm(reply.id)" class="button is-small is-light">
                                Reply
                            </button>
                            <button v-if="isOwner(reply)" @click="deleteReply(reply.id)" class="button is-small is-danger">
                            Delete
                            </button>
                            <div v-if="visibleReplyForm === reply.id" class="reply-form">
                                <textarea class="textarea" v-model="replyText[comment.id]"
                                    placeholder="Write your reply here"></textarea>
                                <button @click="submitReply(comment.id)" class="button is-small is-primary">
                                    Submit
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import jwtDecode from "jwt-decode";

export default {
  name: "CommentBox",
  props: {
    comments: {
      type: Array,
      default: () => [],
    },
    authToken: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      visibleReplyForm: null,
      replyText: {},
      currentUser: null,
    };
  },
  methods: {
    showReplyForm(commentId) {
      this.visibleReplyForm =
        this.visibleReplyForm === commentId ? null : commentId;
    },
    submitReply(commentId) {
      this.$emit("add-reply", {
        parentCommentId: commentId,
        text: this.replyText[commentId],
      });
      this.replyText[commentId] = "";
      this.visibleReplyForm = null;
    },
    childComments() {},
    deleteComment(commentId) {
      this.$emit("delete-comment", commentId);
    },
    deleteReply(replyId) {
      this.$emit("delete-reply", replyId);
    },
    isOwner(comment) {
        const token = this.$store.state.accessToken;
        const decodedToken = jwtDecode(token);
        const userId = decodedToken.user_id;
        console.log(comment.owner);
        console.log(comment.author_id)
        console.log(userId);

        if (comment.author_id === userId) {
            return true;
        } else {
            return false;
        }
    },
  },
  computed: {
    parentComments() {
      let parents = this.comments.filter(
        (comment) => comment.parent_comment == null
      );
      return parents;
    },
  },
  created() {
    if (this.authToken) {
      this.currentUser = jwtDecode(this.authToken);
    }
  },
};
</script>


<style lang="scss">
.comment-container {
    margin-top: 1.5rem;
}

.comment,
.reply {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 1rem;
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
}

.comment-header,
.reply-header {
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

.comment-body,
.reply-body {
    font-size: 1rem;
    line-height: 1.5;
    color: #555;
}

.reply {
    border-color: #eee;
    margin-left: 2rem;
    margin-top: 1rem;
}

.reply-body {
    margin-bottom: 0.5rem;
}

.reply-footer {
    display: flex;
    justify-content: space-between;
    margin-top: 0.5rem;
}

.reply-owner {
    font-size: 0.875rem;
    font-weight: bold;
    color: #555;
}

.reply-form {
    margin-top: 0.5rem;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}

.reply-form .textarea {
    min-height: 3rem;
}

.reply-form button {
    margin-top: 0.5rem;
}

.button.is-light {
    border-color: #ccc;
    color: #333;
}

.button.is-light:hover {
    background-color: #f5f5f5;
}

.button.is-primary {
    background-color: #4a4a4a;
}

.button.is-primary:hover {
    background-color: #363636;
}
</style>
