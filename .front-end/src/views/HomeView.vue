<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
        <meta name="viewport"
            content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login</title>
    <div class="topnav">
        <a href="#menu" class="material-icons">menu</a>
        <b>Login</b>
    </div>
    <div class="main3">
        <form class="login-form">
            <div class="form-group">
                <label for="email">Email address:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button id = "submit-button" type="submit">Login</button>
            <!-- <a href="./register_account.html"><button type="submit">Login</button></a> -->
            <label for="dontHaveAccount">Don't have an account?</label>
            <button id = "register-button" type="submit" formaction="register">Register</button>
        </form>
    </div>

    <div class="main2">
        <div class="event-card">
            <h3>Study Groups</h3>
            <p class="description">Join different study groups based on your course or academic interests and
                collaborate with peers to learn
            </p>
        </div>
        <div class="event-card">
            <h3>Resource</h3>
            <p class="description">Access and share a wealth of academic resources, such as study notes, textbooks,
                videos, and other materials.
            </p>
        </div>
        <div class="event-card">
            <h3>Discussion board</h3>
            <p class="description">Engage in discussions and debates with fellow students on a wide range of academic
                and campus life topics.
            </p>
        </div>
    </div>
</template>

<style>
@import url('./../assets/HomeView.css');
</style>

<script>
export default {
    name: 'HomeView',
};
</script>


<!-- axios -->

