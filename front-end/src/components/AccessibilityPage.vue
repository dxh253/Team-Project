<template>
    <div class="accessibility">
        <button class="accessibility__button" @click="toggleTextSize">
            <span class="sr-only">Toggle Text Size</span>
            <i class="fas fa-font"></i>
        </button>
        <button class="accessibility__button" @click="toggleContrast">
            <span class="sr-only">Toggle Contrast</span>
            <i class="fas fa-adjust"></i>
        </button>
    </div>
</template>


<script>
export default {
    data() {
        return {
            textSize: false,
            contrast: false,
            focus: false,
        };
    },
    methods: {
        toggleTextSize() {
            this.textSize = !this.textSize;
            document.body.classList.toggle('large-text');
        },
        toggleContrast() {
            this.contrast = !this.contrast;
            document.body.classList.toggle('high-contrast');
        },
    },
};
</script>

<style>
.accessibility {
    display: flex;
    gap: 10px;
    padding: 10px;

}

.accessibility__button {
    background-color: #fff;
    border: none;
    border-radius: 15px;
    color: #333;
    cursor: pointer;
    font-size: 1.5rem;
    height: 40px;
    width: 40px;
    align-items: center;
}

.accessibility__button:hover {
    background-color: #3ec487;
}

:focus-visible {
    outline: 3px solid red;
}

.button:focus-visible {
    outline: 3px solid red;
}

/* .input.input:focus-visible {
    outline: 3px solid red;
} */

.select:focus-visible {
    outline: 3px solid red;
}

.button.is-dark:focus-visible {
    outline: 3px solid red;
}

.button.is-light:focus-visible {
    outline: 3px solid red;
}

.button.is-info:focus-visible {
    outline: 3px solid red;
}

.button.is-link:focus-visible {
    outline: 3px solid red;
}

.button.is-success:focus-visible {
    outline: 3px solid red;
}

.button.is-primary:focus-visible {
    outline: 3px solid red;
}

.large-text {
    font-size: 1.2rem;
    font-weight: bold;
}

.large-text button {
    font-size: 1.2rem;
    font-weight: bold;

}

.high-contrast {
    background-color: #000;
    color: turquoise;
}

.high-contrast a {
    color: turquoise;
    text-decoration: underline;
}

.high-contrast div {
    color: white;
    background-color: black;
}

.high-contrast label,
.high-contrast p,
.high-contrast span {
    color: white !important;
    background-color: black;
}

.high-contrast form {
    background-color: black;
    color: white;
    border: solid 1px;
}

.high-contrast input {
    background-color: black;
    color: white;
    border: solid 1px;
    border-color: black;
}

.high-contrast button {
    background-color: black !important;
    color: white !important;
    border: solid 1px !important;
}

.high-contrast div.column {
    background-color: black;
    border: solid 1px;
}

.high-contrast h1 {
    color: white;
}

.high-contrast h2.title {
    /*specifically for help section*/
    color: white;
}

.high-contrast h2.subtitle {
    /*specifically for comment section*/
    color: white;
}

.high-contrast footer {
    background-color: black;
    color: white;
}

.high-contrast input::placeholder {
    color: black;
}

.high-contrast input.input::placeholder {
    color: white !important;
}

.high-contrast textarea::placeholder {
    color: white;
}

.high-contrast input.input {
    border: solid 1px !important;
    border-color: white !important;
    background-color: black !important;
    color: white !important;
}

.high-contrast textarea.description {
    border: solid 1px;
    border-color: white;
    background-color: black;
    color: white;
}

.high-contrast div.your-events,
.high-contrast div.your-studyg,
.high-contrast div.upcoming {
    border: solid 1px;
    background-color: black;
    color: white;
}

.high-contrast div.event-card {
    border: solid 1px;
    background-color: black !important;
    color: white;
}

.high-contrast i {
    color: white !important;
}
</style>
