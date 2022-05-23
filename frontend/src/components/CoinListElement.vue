<template>
<div class="lists_container">
    <div class="names_list">
    <li v-for="coin in coins" v-bind:key="coin" class="names_list_el">
    <router-link :to="/coindetail/ + coin.coin_id" class="router_style">[{{ coin.coin_id }}] {{ coin.coin_name }}</router-link>
    </li>
    </div>
    <div class="prices_list">
    <li v-for="cp in current_price" v-bind:key="cp" class="prices_list_el">{{ cp }}</li>
    </div>
</div>
</template>

<script>
export default {
    name: "CoinListElement",
    props: {
        coins: Array,
        current_price: Array
    },
    computed: {
    }
};
</script>

<style scoped>
.lists_container {
    display: flex;
}
.names_list {
    list-style-type:none;
    font-size: 26px;
    font-style: italic;
}
.names_list_el{
    margin: 15px;
    padding: 18px;
}
.names_list_el:hover {
    color: lightskyblue;
    cursor: pointer;
}
.prices_list {
    list-style-type:none;
     float:left;
}
.prices_list_el {
    margin: 15px;
    border: ridge;
    border-color: black;
    padding: 15px;
    background: floralwhite;
    color: black;
}
.router_style {
    all: unset;
    padding: inherit;
}
</style>