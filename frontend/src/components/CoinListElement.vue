<template>
<div class="lists_container">
    <div class="names_list">
    <li class="names_list_el">
    <router-link :to="/coindetail/ + coin_id" class="router_style">[{{ coin_id }}] {{ coin_name }}</router-link>
    </li>
    </div>
    <div class="prices_list">
    <li class="prices_list_el">{{ current_price }} €</li>
    </div>
</div>
</template>

<script>
export default {
    name: "CoinListElement",
    props: {
        coin_id: String,
        coin_name: String,
        current_price: [Number, String],
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
    width: 300px;
    list-style-type:none;
    font-size: 26px;
    font-style: italic;
}
.names_list_el{
    width: 240px;
    margin: 15px;
    padding: 18px;
}
.names_list_el:hover {
    color: lightskyblue;
    cursor: pointer;
}
.prices_list {
    width: 200px;
    text-align: center;
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