import { createApp } from "vue";
import "./assets/css/base.scss";
import App from "./App.vue";
import { routes } from "./routers/routers";
import { createRouter, createWebHashHistory } from "vue-router";

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

const app = createApp(App);
app.use(router);
app.mount("#app");
