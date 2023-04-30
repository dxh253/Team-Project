<!-- <template>
  <div class="container">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <h1 class="title">Looking For Answers?</h1>
        <p class="subtitle">Ask away!</p>
      </div>
    </section>
    <div class="columns is-custom-width">
      <div class="column">
        <h2 class="title is-4" style="margin-bottom: 1rem; display: flex; align-items: center;">
          <span style="flex-grow: 1;">Posts</span>
          <router-link to="/create">
            <button class="button is-primary">New Post</button>
          </router-link>
        </h2>
        <div class="searchbar">
          <input class="search" type="text" v-model="searchTerm" placeholder="Search posts">
        </div>
        <div v-if="filteredPosts.length > 0">
          <div v-for="post in filteredPosts" :key="post.id">
            <div class="box">
              <div class="columns is-vcentered">
                <div class="column">
                  <post-box :post="post" @postDeleted="removePostFromList" @vote-updated="updatePostVote" />
                </div>
              </div>
            </div>
          </div>
          <button @click="scrollToTop" class="button is-info is-hidden-desktop is-fullwidth">Scroll to top</button>
        </div>
      </div>
    </div>
    <button @click="scrollToTop" class="myBtn is-hidden-mobile">Scroll to top</button>
  </div>
</template>







<script>
import { getAPI } from '@/plugins/axios';
import PostBox from '../components/PostBox.vue';

export default {
    name: 'PostsList',
    components: {
        'post-box': PostBox,
    },
    data() {
        return {
            allposts: [],
            searchTerm: '',


        }
    },
    computed: {
        filteredPosts() {
            // if there is no search term, return all posts
            if (!this.searchTerm) {
                return this.allposts;
            }
            // if there are no posts, return an empty array
            if (this.allposts.length === 0) {
                return [];
            }
            // if there is a search term, filter posts that include the search term in the title
            return this.allposts.filter(post => {
                // filter posts that include the search term in the title
                return post.title.toLowerCase().includes(this.searchTerm.toLowerCase());
            });
        }
    },
    methods: {
        scrollToTop() {
            // Scroll to top with smooth behavior
            window.scrollTo({ top: 0, behavior: 'instant' });
        },
        removePostFromList(postId) {
            this.allposts = this.allposts.filter((post) => post.id !== postId);
        },
        updatePostVote(postId, vote) {
            const postToUpdate = this.allposts.find((post) => post.id === postId);
            if (postToUpdate) {
                postToUpdate.score += vote;
            }
        },
        updatePostScore(postId, updatedScore) {
            const postToUpdate = this.allposts.find((post) => post.id === postId);
            if (postToUpdate) {
                postToUpdate.score = updatedScore;
            }
        }
    },
    created() {
        const token = localStorage.getItem("access");

        getAPI
            .get("/api/v1/posts/", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            })
            .then((response) => {
                console.log("Post API has received data");
                this.allposts = response.data;
            })
            .catch((error) => {
                console.log(error);
            });
    },
}
</script>

<style lang="scss">
.box {
    margin-bottom: 1.5rem;
}

@media screen and (max-width: 1023px) {
    .column.is-one-quarter-desktop {
        display: none;
    }

    .button.is-hidden-desktop {
        display: block !important;
        margin-left: auto;
        margin-right: auto;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
}

.myBtn {
    position: fixed;
    bottom: 20px;
    right: 30px;
    z-index: 99;
    border: none;
    outline: none;
    background-color: hsl(171, 100%, 41%);
    color: white;
    cursor: pointer;
    padding: 15px;
    border-radius: 5px;
    font-size: 18px;
}
</style> -->

<template>
    <div class="container">
        <section class="hero is-medium is-dark mb-6">
            <div class="hero-body has-text-centered">
                <h1 class="title">Looking For Answers and Resources?</h1>
                <p class="subtitle">Ask away!</p>
            </div>
        </section>
        <div class="columns is-custom-width">
            <div class="column">
                <h2 class="title is-4" style="margin-bottom: 1rem; display: flex; align-items: center;">
                    <span style="flex-grow: 1;">Posts</span>
                    <router-link to="/create">
                        <button class="button is-primary" tabindex="-1">New Post</button>
                    </router-link>
                </h2>
                <div class="searchbar">
                    <input class="search" type="text" v-model="searchTerm" placeholder="Search posts or category">
                </div>
                <!-- <div class="select field column is-3">
                    <select v-model="choice">
                        <option value="0">Show all</option>
                        <option value="1">Study Resources only</option>
                    </select>
                </div> -->
                <div class="columns">
                    <div class="column">
                        <button @click="toggleView" class="button is-primary">
                        {{ viewMode ? 'Gallery View' : 'List View' }}
                        </button>
                    </div>
                    <div class="column is-3">
                        <div class="select">
                            <select v-model="choice">
                                <option value="0">Show all</option>
                                <option value="1">Study Resources only</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div v-if="filteredPosts.length > 0">
                    <!-- <div v-for="post in filteredPosts" :key="post.id"> -->
                    <div v-if="viewMode" class="columns is-multiline">
                        <div v-for="post in filteredPosts" :key="post.id" class="column is-one-third">
                            <post-box :post="post" @postDeleted="removePostFromList" @vote-updated="updatePostVote" />
                        </div>
                    </div>
                    <div v-else>
                        <div v-for="post in filteredPosts" :key="post.id">
                            <div class="box">
                                <div class="columns is-vcentered">
                                    <div class="column">
                                        <post-box :post="post" @postDeleted="removePostFromList"
                                            @vote-updated="updatePostVote" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                        <button @click="scrollToTop" class="button is-info is-hidden-desktop is-fullwidth">Scroll to top</button>
                </div>
            </div>
        </div>
        <button @click="scrollToTop" class="myBtn is-hidden-mobile">Scroll to top</button>
    </div>
</template>


<script>
import { getAPI } from '@/plugins/axios';
import PostBox from '../components/PostBox.vue';

export default {
    name: 'PostsList',
    components: {
        'post-box': PostBox,
    },
    data() {
        return {
            allposts: [],
            viewMode: false,
            choice: "0",
            searchTerm: '',


        }
    },
    computed: {
        filteredPosts() {
            let filteredPosts = this.allposts;
            if (this.choice == "1")
                filteredPosts = this.allposts.filter((post) => post.category_name.toLowerCase() === "resources");
            if (this.searchTerm) {
                filteredPosts = this.allposts.filter((post) => {
                    let searchTerm = this.searchTerm.toLowerCase();
                    let textToMatch = post.title.toLowerCase();
                    let categoryToMatch = post.category_name.toLowerCase();
                    let charIndex = 0;
                    for (const c of textToMatch) {
                        if (c == searchTerm[charIndex]) ++charIndex;
                    }
                    for (const c of categoryToMatch) {
                        if (c == searchTerm[charIndex]) ++charIndex;
                    }
                    return charIndex == searchTerm.length;
                });
            }
            return filteredPosts;

        },
    },
    methods: {
        toggleView() {
            this.viewMode = !this.viewMode;
        },
        scrollToTop() {
            // Scroll to top with smooth behavior
            window.scrollTo({ top: 0, behavior: 'instant' });
        },
        removePostFromList(postId) {
            this.allposts = this.allposts.filter((post) => post.id !== postId);
        },
        updatePostVote(postId, vote) {
            const postToUpdate = this.allposts.find((post) => post.id === postId);
            if (postToUpdate) {
                postToUpdate.score += vote;
            }
        },
        updatePostScore(postId, updatedScore) {
            const postToUpdate = this.allposts.find((post) => post.id === postId);
            if (postToUpdate) {
                postToUpdate.score = updatedScore;
            }
        }
    },
    created() {
        const token = localStorage.getItem("access");

        getAPI
            .get("/api/v1/posts/", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            })
            .then((response) => {
                console.log("Post API has received data");
                this.allposts = response.data;
            })
            .catch((error) => {
                console.log(error);
            });
    },
}
</script>

<style lang="scss">
.box {
    margin-bottom: 1.5rem;
}

@media screen and (max-width: 1023px) {
    .column.is-one-quarter-desktop {
        display: none;
    }

    .button.is-hidden-desktop {
        display: block !important;
        margin-left: auto;
        margin-right: auto;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
}

.myBtn {
    position: fixed;
    bottom: 20px;
    right: 30px;
    z-index: 99;
    border: none;
    background-color: hsl(171, 100%, 41%);
    color: white;
    cursor: pointer;
    padding: 15px;
    border-radius: 5px;
    font-size: 18px;
}
</style>
