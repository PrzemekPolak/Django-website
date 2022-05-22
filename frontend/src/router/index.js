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
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router