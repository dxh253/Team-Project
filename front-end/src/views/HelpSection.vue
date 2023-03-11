<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <!-- references to the other pages yet to be added -->
    <!-- logo and site name yet to be added -->

    <div class="htopnav">
        <a class="material-icons" onclick="openNav()">menu</a>
        <b>Help Section</b>
    </div>

    <!-- search needs to search title in database -->
    <div class="hheader">
        <a>How can we help?</a>
        <input type="text" placeholder="Search your problem here" id="keywordProblem">
        <c>Here are some useful articles</c>
    </div>

    <!-- buttons need appriate functions -->
    <div class="hmain1">
        <button type="button" class="button" onclick="button1()">Testing</button>
        <button type="button" class="button" onclick="button2()">Testing2</button>
        <button type="button" class="button" onclick="button3()">Testing3</button>
    </div>

    <!-- user needs to be updated according to each user -->
    <!-- submit function needs to be properly implemented -->
    <div class="hmain2">
        <a>Or you can submit your problem here</a>
        <div class="hmain21">
            <i class="material-icons">person</i>
            <a>User 1</a>
        </div>
        <form class="hmain22">
            <input type="text" id="title" placeholder="Enter Title" class="title">
            <textarea type="text" id="problem" placeholder="Describe your problem here" class="problem"></textarea>
            <button type="button" class="button" onclick="submit()">Submit</button>
        </form>
    </div>
</template>

<style>
@import url('../assets/HelpSectionView.css');
</style>

<script>
export default {
    name: 'HelpSection',
};
</script>