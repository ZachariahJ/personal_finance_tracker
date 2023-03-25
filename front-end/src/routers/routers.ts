import MyWallet from "../pages/MyWallet.vue";
import Calender from "../pages/Calender.vue";
import Charts from "../pages/Charts.vue";
import AutoBilling from "../pages/AutoBilling.vue";
import { RouteRecordRaw } from "vue-router";

export const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    redirect: "/my-wallet",
  },
  {
    path: "/my-wallet",
    name: "MyWallet",
    component: MyWallet,
  },
  {
    path: "/calender",
    name: "Calender",
    component: Calender,
  },
  {
    path: "/charts",
    name: "Charts",
    component: Charts,
  },
  {
    path: "/auto-billing",
    name: "AutoBilling",
    component: AutoBilling,
  },
];
