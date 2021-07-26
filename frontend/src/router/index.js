import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Preprocess from "../views/Preprocess.vue";
import Algorithms from "../views/Algorithms.vue";
import Log from "../views/Log.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/preprocessing",
    name: "Preprocess",
    component: Preprocess,
  },
  {
    path: "/algorithms",
    name: "Algorithms",
    component: Algorithms,
  },
  {
    path: "/log",
    name: "Log",
    component: Log,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
