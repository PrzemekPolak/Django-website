<template>

<div>

<form v-on:submit.prevent="submitForm">
    <div>
        <div>{{coin_id}}</div>
        <div>Posiadana ilośc: {{owned_coins}}</div>
        <div>DODAJ WALIDACJĘ !!!<br>Obecna cena: {{coin_price}}</div>
        <div>
            <div>Ilość:</div>
            <input type="text" v-model="form_amount">
        </div>
        <div>Suma: {{total}}</div>
    </div>
    <button type="submit">Kup</button>
</form>


</div>

</template>

<script>
import axios from 'axios';

export default {
    name: "CoinBuyForm",
    props: {
        coin_price: Number,
        user_id: String,
    },
      data() {
        return {
            coin_id: '',
            form_amount: 0,
            owned_coins: 0,
    }},
    methods: {
        submitForm(){
            axios.post('http://127.0.0.1:8000/api/coin_buy/', {
                coin_id: this.coin_id,
                form_amount: this.form_amount,
                user_id: this.user_id})
                .then((res) => {
                    console.log(res.data)
                    this.owned_coins = res.data['amount']
                })
                .catch((error) => {
                    console.log(error)
            })
        },
        getUserCoins() {
            axios.get('http://127.0.0.1:8000/api/get_user_assets/'+this.user_id+'/'+this.coin_id+'/')
                .then((res) => {
                    this.owned_coins = res.data[0]['ammount']
                })
                .catch((error) => {
                    console.log(error)
            })           
        }
    },
    created() {
        this.coin_id = this.$route.params.id
        this.getUserCoins()
    },

    computed: {
        total: function() {
            const cost = this.form_amount * this.coin_price
            return parseFloat(cost.toFixed(4))
        }
    }
};
</script>

<style>

</style>