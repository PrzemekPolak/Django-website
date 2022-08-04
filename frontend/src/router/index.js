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
    {
    name: "UserWallet",
    path: "/userwallet",
    component: () => import("@/views/UserWallet")
    },
    {
        name: "UserTransactions",
        path: "/usertransactions",
        component: () => import("@/views/UserTransactions")
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router