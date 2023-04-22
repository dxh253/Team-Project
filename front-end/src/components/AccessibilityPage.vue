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
        <button class="accessibility__button" @click="toggleFocus">
            <span class="sr-only">Toggle Focus</span>
            <i class="fas fa-crosshairs"></i>
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
            document.footer.classList.toggle('high-contrast');
        },
        toggleFocus() {
            this.focus = !this.focus;
            document.body.classList.toggle('no-focus');
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

.accessibility__button:hover,
.accessibility__button:focus {
    background-color: #eee;
    outline: none;
}

.large-text {
    font-size: 1.2rem;
}

.high-contrast{
    background-color: #000;
    color: turquoise;
}

.high-contrast a {
  color: #fff12ebb;
  text-decoration: underline;
}

.high-contrast div{
    color: white;
    background-color: black;
}

.high-contrast label,
.high-contrast p,
.high-contrast span{
    color: white !important;
}

.high-contrast form{
    background-color: black;
    color: white;
    border: solid 1px;
}

.high-contrast input{
    background-color: black;
    color: white;
    border: solid 1px;
}

.high-contrast button{
    background-color: black !important;
    color: white !important;
    border: solid 1px !important;
}

.high-contrast div.column{
    background-color: black;
    border: solid 1px;
}

.high-contrast h1, h2, title{
    color: white;
}

.high-contrast footer{
    background-color: black;
    color: white;
}

.high-contrast div.event-card{
    border: block 1px;
}



.no-focus {
    outline: none;
}
</style>
