<template>
<div class="menu_container">
    <router-link to="/" class="router_style">
        <div class="menu_el mainpage_el">Strona Główna</div>
    </router-link>
    <div v-if="logged_in_user" style="display:flex">
        <router-link to="/userwallet" class="router_style">
            <div class="menu_el mainpage_el">Portfel</div>
        </router-link>
    </div>
    <div class="menu_el calendar">
        <MenuDate />
    </div>
    <div class="menu_el clock">
        <MenuClock />
    </div>

<div v-if="!logged_in_user" style="display:flex">
    <router-link to="/userlogin" class="router_style">
        <div class="menu_el login_el">Zaloguj się</div>
    </router-link>
    <div class="menu_el">Gość</div>
</div>
<div v-else style="display:flex">
    <div class="menu_el login_el" @click="logout()">Wyloguj się</div>
    <div class="menu_el">{{ user_name }}</div>
</div>

</div>
</template>

<script>
import MenuClock from "@/components/MenuClock";
import MenuDate from "@/components/MenuDate";

import axios from 'axios';

export default {
    name: "MenuTop",
    components: {
        MenuClock,
        MenuDate,
    },
    props: {
        user_name: String,
        logged_in_user: [Boolean, String],
    },
    methods: {
        logout(){
            axios.post('http://127.0.0.1:8000/api/user_logout/')
                .then((res) => {
                    if (res.data['success']) {
                        document.cookie.split(";").forEach(function(c) { document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); });
                        this.$parent.logged_in_user = false
                        this.$parent.cash = null
                    }
                })
                .catch((error) => {
                    console.log(error)
                })
        },
  },
    computed: {
    }
};
</script>

<style scoped>
.menu_container {
    display: flex;
    background: black;
    margin-bottom: 30px;
}

.menu_el {
    padding: 30px;
    font-size: 28px;
}

.menu_el.clock {
    margin-right: auto;
}

.menu_el.login_el,
.menu_el.calendar {
    margin-left: auto;
}

.menu_el.login_el:hover,
.menu_el.mainpage_el:hover {
    opacity: 0.8;
    cursor: pointer;
}

.router_style {
    all: unset;
}
</style>