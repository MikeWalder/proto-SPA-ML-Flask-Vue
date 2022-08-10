import Vue from "vue";
import VueRouter from "vue-router";
import LoginPoint from "../components/LoginPoint.vue";
import LogOut from "../components/LogOut.vue";
import DashBoard from "../components/DashBoard.vue";
import ProjetOne from "../components/ProjetOne.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "login",
    component: LoginPoint,
  },
  {
    path: "/logout",
    name: "logout",
    component: LogOut,
  },
  {
    path: "/projet1",
    name: "projet1",
    component: ProjetOne,
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
