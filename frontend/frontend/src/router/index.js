import Vue from "vue";
import VueRouter from "vue-router";
import LoginPoint from "../components/LoginPoint.vue";
import DashBoard from "../components/DashBoard.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "login",
    component: LoginPoint,
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: DashBoard,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
