<!-- <template lang="html">
    <div class="vote">
      <svg @click="upVote" :class="{ active: votedUp }" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
        <path d="M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z"/>
        <path d="M0 0h24v24H0z" fill="none"/>
      </svg>
      <p>{{ voting }}</p>
      <svg @click="downVote" :class="{ active: votedDown }" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
        <path d="M7.41 7.84L12 12.42l4.59-4.58L18 9.25l-6 6-6-6z"/>
        <path d="M0-.75h24v24H0z" fill="none"/>
      </svg>
    </div>
  </template>
  
  <script>
//   import store from '@/store/index'
  import { getAPI } from '@/plugins/axios';
  import { post_id } from '@/plugins/axios';

  export default {
      name: 'vote-vote',
  
      props: ['upvotes', 'downvotes', 'post_id'],
  
      methods: {
          upVote() {
                getAPI.post('posts/' + post_id + '/upvote')
                  .then(response => {
                    this.$emit('update:upvotes', response.data.upvotes)
                    this.$emit('update:downvotes', response.data.downvotes)
                  })
                  .catch(e => {
                      this.$emit('error', e.response.data.error)
                  })
          },
  
          downVote() {
                getAPI.post('posts/' + post_id + '/downvote')
                  .then(response => {
                    this.$emit('update:upvotes', response.data.upvotes)
                    this.$emit('update:downvotes', response.data.downvotes)
                  })
                  .catch(e => {
                    this.$emit('error', e.response.data.error)
                  })
          }
      },
  
      computed: {
          voting() {
              return this.upvotes.length - this.downvotes.length
          },
  
          votedUp() {
            //   if (!store.state.isUserLoggedIn) {
            //       return false
            //   }
  
              for (var i in this.upvotes) {
                //   if (this.upvotes[i].username == store.state.user.username) {
                      return true
                //   }
              }
              return false
          },
  
          votedDown() {
            //   if (!store.state.isUserLoggedIn) {
            //       return false
            //   }
  
              for (var i in this.downvotes) {
                //   if (this.downvotes[i].username == store.state.user.username) {
                      return true
                //   }
              }
              return false
          }
      },
  }
  </script>
  
  <style lang="css">
  .vote {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 20px;
  }
  
  .vote p {
      margin: 10px 0;
  }
  
  .vote svg.active {
      fill: red;
  }
  
  .vote svg:hover {
      fill: rgb(27, 122, 249);
      cursor: pointer;
  }
  </style> -->

  <template>
    <div>
      <button @click="upvote">Upvote</button>
      <span>{{ score }}</span>
      <button @click="downvote">Downvote</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PostVote',
    props: {
      postId: {
        type: Number,
        required: true
      },
      initialScore: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        score: this.initialScore
      }
    },
    methods: {
      upvote() {
        this.score++
        this.updateScore()
      },
      downvote() {
        this.score--
        this.updateScore()
      },
      updateScore() {
        // make an API call to update the post's score
        // using the postId and the new score value
      }
    }
  }
  </script>
  
  <style>
  button {
    cursor: pointer;
  }
  </style>
  