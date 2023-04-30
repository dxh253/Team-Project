<template>
    <div class="container">

      <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <h1 class="title">
              How can we help?
        </h1>
        <p class="subtitle">Have an issue? Look no further...</p>
      </div>
    </section>
  
      <div class="section">
        <div class="columns is-centered is-multiline">
          <div class="column is-one-third">
            <RouterLink to="/help_features/" tabindex="-1" class="button is-large is-link is-light is-outlined is-fullwidth">
              Features
            </RouterLink>
          </div>
          <div class="column is-one-third">
            <RouterLink to="/help_accessibility/" tabindex="-1" class="button is-large is-link is-light is-outlined is-fullwidth">
              Accessibility
            </RouterLink>
          </div>
          <div class="column is-one-third">
            <RouterLink to="/privacy_policy/" tabindex="-1" class="button is-large is-link is-light is-outlined is-fullwidth">
              Privacy Policy
            </RouterLink>
          </div>
        </div>
        <hr>
  
 
        <div class="columns">
            <div class="column is-3">
                <h2 class="title is-3">{{ listTitle }}</h2>
            </div>
            <div class="field column is-5">
                <div class="control">
                    <input class="input" type="text" placeholder="Search your problem here..." v-model="searchValue">
                </div>
            </div>
            <div class="column is-2">
                <button class="button is-link is-outlined" @click="filterProblems">My problems</button>
            </div>
            <div class="column is-2">
                <button class="button is-link" @click="showForm = !showForm">{{ showForm ? 'Hide form' : 'Submit a problem' }}</button>
            </div>
            
            </div>
            <div v-show= "showForm" class="columns">
          <div class="column is-half is-offset-one-quarter">
            <div class="box">
              <h2 class="title is-4">Or you can submit your problem here</h2>
              <form @submit.prevent="submitProblem">
                <div class="field">
                  <label class="label">Title of your problem</label>
                  <div class="control">
                    <input class="input" type="text" placeholder="Enter Title" v-model.trim="problemInfo.title" required>
                  </div>
                </div>
                <div class="field">
                  <label class="label">Describe your problem</label>
                  <div class="control">
                    <textarea class="textarea" placeholder="Describe your problem here" v-model.trim="problemInfo.description" required></textarea>
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-link" type="submit">Submit</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>

            <div>
                <ProblemCard v-for="problem in displayedProblems" v-bind:key="problem.id" v-bind:problem="problem" />
            </div>
        </div>

        <div v-show="!showing">
            <div class="columns">
                <div class="column is-10">
                    <h2 class="title is-3">You searched for problems containing "{{ searchValue }}"</h2>
                </div>
                <div class="column is-2 is-offset">
                    <button type="button" class="button is-underlined is-link is-light" @click="filterProblems"> My problems
                    </button>
                </div>
                <p v-show="noproblem">You haven't submitted any problems.</p>
            </div>

            <button class="button" @click="clearSearch" style="margin-top: 2px; margin-bottom: 50px;">Clear search</button>
            <!-- roundabout way but works -->
            <ProblemCard v-for="problem in searchProblems" v-bind:key="problem.id" v-bind:problem="problem" />
        </div>
    </div>
</template>


<script>
import ProblemCard from '@/components/ProblemCard';
import { getAPI } from '@/plugins/axios'
import jwt_decode from "jwt-decode";

export default {
    name: 'HelpSection',
    data() {
        return {
            allProblems: [],
            displayedProblems: [],
            problemInfo: {
                title: '',
                description: '',
                filterByOwner: false,
            },
            renderComponent: true,
            searchValue: '',
            showing: true,
            listTitle: 'All Questions',
            introText: 'Here are some useful articles',
            noproblem: this.displayedProblems === [],
            notificationMessage: '',
            notificationType: '',
            showForm: false,
        }
    },
    components: {
        ProblemCard,
    },
    methods: {
        submitProblem() {
            console.log('submit problem method');
            if (!this.$store.getters.loggedIn) {
                //User is not logged in
                return;
            }

            console.log(this.problemInfo.title + " " + this.problemInfo.description)
            const token = localStorage.getItem("access");
            const decodedToken = jwt_decode(token);
            const ownerId = decodedToken.user_id;

            const formData = new FormData();
            if (this.problemInfo.title.length < 100) {
                formData.append('title', this.problemInfo.title);
                formData.append('description', this.problemInfo.description);
                formData.append('owner', parseInt(ownerId));
            }
            else {
                alert("Title exceeds 100 character limit.")
                return
            }
            getAPI
                .post('/api/v1/help/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        'Authorization': `Bearer ${this.$store.state.accessToken}`,
                    }
                })
                .then((response) => {
                    console.log('API response data:', response.data);
                    window.location.reload();
                })
                .catch((error) => {
                    console.log(error.response.data);
                    alert('Something went wrong. Please try again.')
                })
        },

        filterProblems() {
            if (this.filterByOwner) {
                // filterByOwner set false by default
                // starts at else part
                // when user clicks button again - filterByOwner is true is will run
                this.displayedProblems = this.allProblems;
                this.filterByOwner = false;
                this.listTitle = 'All Questions';
            } else {
                const userId = jwt_decode(this.$store.state.accessToken).user_id;
                const filteredProblems = this.allProblems.filter((problem) => {
                    return problem.owner === userId;
                });
                this.displayedProblems = filteredProblems;
                this.filterByOwner = true;
                this.listTitle = 'My Questions'
            }
        },

        clearSearch() {
            this.searchValue = '';
        }
    },
    computed: {
        searchProblems() {
            console.log("you searched for " + this.searchValue);
            if (!this.searchValue) {
                return this.allProblems.filter((problem) => {
                    this.showing = true;
                    this.introText = "Here are some useful articles";
                    return problem;
                });
            }

            return this.allProblems.filter((problem) => {
                this.showing = false;
                this.introText = "";

                // Checks that all characters in `this.searchValue` appear in the same
                // order in `this.problem.title` e.g. `prty` will match `party` but
                // not `piracy` or `try please`
                let charIndex = 0;
                let searchValue = this.searchValue.toLowerCase();
                for (const c of problem.title.toLowerCase()) {
                    if (c == searchValue[charIndex]) ++charIndex;
                }
                return charIndex == searchValue.length;
            });
        },
    },
    async created() {
        console.log('created method is executed');

        getAPI
            .get('/api/v1/help/', {
                headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
            })
            .then((response) => {
                console.log('API response data:', response.data);
                this.allProblems = response.data;
                this.displayedProblems = response.data;
                this.$store.state.APIData = response.data
            })
            .catch((error) => {
                console.log('API error:', error);
            });
    },
};

</script>
