import { onMounted } from 'vue';
import { createApp } from '@vue/runtime-dom';
import Accessibility from '@/components/AccessibilityPage.vue';

export default function accessibilityPlugin(Vue) {
    const app = createApp(Accessibility);
    const vm = app.mount(document.createElement('div'));

    onMounted(() => {
    const el = document.createElement('div');
    el.setAttribute('role', 'status');
    el.setAttribute('aria-live', 'polite');
    document.body.appendChild(el);
    vm.$parent = Vue.prototype;
    el.appendChild(vm.$el);
    });

    Vue.prototype.$accessibility = vm.$accessibility;
}
