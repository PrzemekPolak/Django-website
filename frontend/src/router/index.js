// import Vue from "vue";
// import Router from "vue-router";

// Vue.use(Router);

// export default new Router({
//   routes: [
//     {
//       name: "HomePage",
//       path: "",
//       component: () => import("@/views/Home")
//     },
//   ]
// });

import { createWebHistory, createRouter } from "vue-router"

const routes = [
    {
        name: "HomePage",
        path: "",
        component: () => import("@/views/Home")
    },
    {
        name: "CoinDetail",
        path: "/coindetail/:id",
        component: () => import("@/views/CoinDetail")
    },
    {
    name: "UserLogin",
        path: "/userlogin",
        component: () => import("@/views/UserLogin")
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router