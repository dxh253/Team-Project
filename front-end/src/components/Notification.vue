<!-- Notification.vue -->
<template>
    <transition name="slide-fade">
        <div v-if="show" class="notification" :class="type">
            {{ message }}
        </div>
    </transition>
</template>

<script>
    export default {
        name: 'Notification',
        props: ['message', 'type', 'duration'],
        data() {
            return {
                show: false,
            };
        },
        methods: {
            showNotification() {
                this.show = true;
                setTimeout(() => {
                    this.show = false;
                }, this.duration);
            },
        },
        watch: {
            message() {
                this.showNotification();
            },
        },
    };
</script>

<style scoped>
.notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    padding: 1rem;
    border-radius: 5px;
    z-index: 1000;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
    transition: all 0.3s ease;
}

.slide-fade-enter,
.slide-fade-leave-to {
    transform: translateY(50px);
    opacity: 0;
}
</style>
