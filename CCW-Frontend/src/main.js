/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'
import globalState from './globalState';

const app = createApp(App)
app.config.globalProperties.$globalState = globalState;
registerPlugins(app)


app.mount('#app')
