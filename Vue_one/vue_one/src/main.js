// import './assets/main.css'
// import './assets/base.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import piniaPersist from 'pinia-plugin-persist'
const pinia = createPinia()
pinia.use(piniaPersist) // 注册插件

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)
app.use(pinia)
app.mount('#app')
