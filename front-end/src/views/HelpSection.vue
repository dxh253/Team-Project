<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <div class="home">
    <section class="hero is-small is-dark mb-6">
          <div class="hero-body has-text-centered mt-6">
            <h1 class="title" style="font-size: 50px;">
               How can we help?
            </h1>
            <input 
            class="input" 
            type="text" 
            placeholder="Search your problem here..." 
            style="width: 675px; border-radius: 20px; text-indent: 3%;"
            >
          </div>
          <div class="hero-footer has-text-centered mb-5">
            <p>
                Here are some useful articles
            </p>
          </div>
        
    </section>
    </div>
    
    <div class="columns is-mobile is-centered is-multiline has-text-centered" style="margin-bottom: 2%;">
        <div class="column">
            <button class="button is-large is-link is-light is-outlined" style="width: 250px; height: 125px; margin: 3px 25px;">
                Testing
            </button>
            <button class="button is-large is-link is-light is-outlined" style="width: 250px; height: 125px; margin: 3px 25px;">
                Testing
            </button>
            <button class="button is-large is-link is-light is-outlined" style="width: 250px; height: 125px; margin: 3px 25px;">
                Testing232
            </button>
        </div>
    </div>
    
    <div class="hero" style="margin-bottom: 3%; margin-left: 5%;">
        <p class="title is-4">Or you can submit your problem here</p>
        <div class="columns" style="align-items: center;">
            <i class="column is-1 material-icons" style="font-size: 40px;">person</i>
        </div>

        <div class="event-card" style="margin: 0%; width: 1000px;">
            <div class="field">
                <label>Title of your problem</label>
                <input 
                class="input"
                ows="1"
                type="text"
                placeholder="Enter Title"
                style="width: 400px; 
                border:1px solid grey;
                background-color: white;"
                v-model.trim="problemInfo.title"
                >
            </div>
            <div class="field">
                <label>Describe your problem</label>
                <textarea 
                    class="textarea" 
                    type="text" 
                    placeholder="Describe your problem here" 
                    style="border:1px solid grey;"
                    v-model.trim="problemInfo.description">
                </textarea>
                <div style="text-align: right;">
                <button class="button is-info" type="button" style="margin-top: 5px;" @click="submitProblem">Submit</button>
                </div>
            </div>
        </div>
    </div>

    <h2 class="title is-3">Here is a list of problems submitted by other users</h2>
    <div class="box" @click.right="viewProblem" style="max-width: 1000px; margin-left: 5%;">
        <h3 class="is-size-4"> static problem card 1 </h3>
        <p class="is-size-6" style=""> description display 1</p>
    </div>
    <div class="box" @click.right="viewProblem" style="max-width: 1000px; margin-left: 5%;">
        <h3 class="is-size-4"> Static problem card 2 </h3>
        <p class="is-size-6" style=""> description display 2</p>
    </div>

    <ProblemCard
        v-for="problem in allProblems"
        v-bind:key="problem.id"
        v-bind:problem="problem"
      />

</template>


<script>
import ProblemCard from '@/components/ProblemCard';
import { getAPI } from '@/plugins/axios'

export default {
    name: 'HelpSection',
    data() {
        return {
            allProblems: [],
            problemInfo: {
                title: '',
                description: '',
                user: 'null',
            }
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
            const formData = new FormData();
            formData.append('title', this.problemInfo.title);
            formData.append('description', this.problemInfo.description);
            getAPI
                .post('/api/v1/help', formData, {
                method: 'POST'
                })
                .then((response) => {
                console.log('API response data:', response.data);
                this.allProblems = response.data;
                this.$store.state.APIData = response.data;
                })
                .catch((error) => {
                console.log(error.response.data);
                alert('Something went wrong. Please try again.')
                })
        }
    },
    async created() {
        console.log('created method is executed');
            if (!this.$store.getters.loggedIn) {
            //User is not logged in
            return;
        }

        getAPI
            .get('/api/v1/help/', {
                   headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
               })
            .then((response) => {
               console.log('API response data:', response.data);
               this.allProblems = response.data;
               this.$store.state.APIData = response.data;
            })
            .catch((error) => {
                console.log('API error:', error);
            });
        },
    };

</script>