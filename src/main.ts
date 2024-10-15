import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import PrimeVue from 'primevue/config';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import 'primevue/resources/themes/aura-light-green/theme.css'
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
import ToastService from 'primevue/toastservice';
import Toast from 'primevue/toast';
import Tooltip from 'primevue/tooltip';
const app = createApp(App);
// Primevue pluggin
app.component('Accordion', Accordion);
app.component('AccordionTab', AccordionTab);
app.component('Toast', Toast);

app.use(router)
   .use(VueAxios, axios)
   .use(PrimeVue)
   .use(ToastService)
   .use(createPinia().use(piniaPluginPersistedstate)) // Create Pinia instance
   .mount('#app');
app.directive('tooltip', Tooltip);