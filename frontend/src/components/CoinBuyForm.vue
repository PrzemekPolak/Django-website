<template>

<div>

<form v-on:submit.prevent="submitForm">
    <div>
        <div>{{coin_id}}</div>
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
    },
      data() {
        return {
            coin_id: '',
            form_amount: 0,
            user_id: 'Przemek',
    }},
    methods: {
        submitForm(){
            axios.post('http://127.0.0.1:8000/api/coin_buy/', {
                coin_id: this.coin_id,
                form_amount: this.form_amount,
                user_id: this.user_id})
                .then((res) => {
                    console.log(res)
                })
                .catch((error) => {
                    console.log(error)
            })
        }
    },
    created() {
        this.coin_id = this.$route.params.id
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