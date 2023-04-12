<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <div class="home">
    <section class="hero is-small is-dark mb-6">
          <div class="hero-body has-text-centered mt-6">
            <h1 class="title" style="font-size: 50px;">
               How can we help?
            </h1>
            <input class="input" type="text" placeholder="Search your problem here..." style="width: 675px; border-radius: 20px; text-indent: 3%;">
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
                <input class="input" rows="1" type="text" id="title" placeholder="Enter Title" style="width: 400px; border:1px solid grey; background-color: white;">
            </div>
            <div class="field">
                <label>Describe your problem</label>
                <textarea class="textarea" type="text" id="problem" placeholder="Describe your problem here" style="border:1px solid grey;"></textarea>
                <div style="text-align: right;">
                <button class="button is-info" type="button" onclick="submit()" style="margin-top: 5px;">Submit</button>
                </div>
            </div>
        </div>
    </div>

    <h2 class="title is-3">Here is a list of problems submitted by other users</h2>

</template>


<script>
export default {
    name: 'HelpSection',
};
</script>