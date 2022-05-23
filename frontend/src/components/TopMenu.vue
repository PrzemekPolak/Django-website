<template>
<div class="menu_container">
    <router-link to="/" class="router_style">
        <div class="menu_el">Menu</div>
    </router-link>
    <div id="calendar" class="menu_el calendar">20.05.2022</div>
    <div id="clock" class="menu_el">17:30:15</div>
    <div class="menu_el">{{ el4 }}</div>
</div>
</template>

<script>
export default {
    name: "TopMenu",
    props: {
        el4: String,
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

.menu_el.login_el,
.menu_el.calendar {
    margin-left: auto;
}

.menu_el:hover,
.menu_el.login_el:hover,
.menu_el.mainpage_el:hover {
    opacity: 0.8;
    cursor: pointer;
}

.router_style {
    all: unset;
}
</style>