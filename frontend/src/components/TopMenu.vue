<template>
<div class="menu_container">
    <div class="menu_el">{{ el1 }}</div>
    <div id="calendar" class="menu_el calendar">{{ el2 }}</div>
    <div id="clock" class="menu_el">{{ el3 }}</div>
    <div class="menu_el">{{ el4 }}</div>
</div>
</template>

<script>
export default {
    name: "TopMenu",
    props: {
        el1: String,
        el2: String,
        el3: String,
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
    margin-bottom: 20;
}

.menu_el {
    padding: 30;
    font-size: 28;
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
</style>