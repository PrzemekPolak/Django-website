<template>

<div class="container">

<form v-on:submit.prevent="submitForm">
    <div>  
        <div class="single_row">
            <div class="first_column">Posiadana ilośc:</div>
            <div>{{owned_coins}}</div>
        </div>
        <div class="single_row">
            <div class="first_column">Obecna cena:</div>
            <div>{{coin_price}} €</div>
        </div>
        <div class="single_row">
            <div class="first_column">Ilość:</div>
            <input type="text" v-model="form_amount">
            <div style="margin-left:10px;">{{coin_id}}</div>
        </div>
        <div class="single_row">
            <div class="first_column">Dostępne środki:</div>
            <div>{{parseFloat(owned_cash).toFixed(4)}} €</div>
        </div>
        <div class="single_row">
            <div class="first_column">Całkowita wartość:</div>
            <div>{{total}} €</div>
        </div>
    </div>
    <div v-if="show_buy_form" class="button_div">
        <button type="submit">Kup</button>
    </div>
    <div v-else class="button_div">
        <button type="submit">Sprzedaj</button>
    </div>
</form>


</div>

</template>

<script>
import axios from 'axios';

export default {
    name: "CoinBuySellForm",
    props: {
        coin_price: Number,
        user_id: String,
        show_buy_form: Boolean,
        cash: [Number, String],
    },
      data() {
        return {
            coin_id: '',
            form_amount: 0,
            owned_coins: 0,
            owned_cash: 0,
    }},
    methods: {
        submitForm(){
            var fetch_url = 'http://127.0.0.1:8000/api/'
            if (this.show_buy_form) {
                fetch_url += 'coin_buy/'
            }
            else {
                fetch_url += 'coin_sell/'
            }
            axios.post(fetch_url, {
                coin_id: this.coin_id,
                form_amount: this.form_amount,
                user_id: this.user_id})
                .then((res) => {
                    console.log(res.data)
                    this.owned_coins = res.data['amount']
                    this.owned_cash = res.data['cash']
                    document.cookie = "cash=" + res.data['cash']
                })
                .catch((error) => {
                    console.log(error)
            })
        },
        getUserCoins() {
            axios.get('http://127.0.0.1:8000/api/get_user_assets/'+this.user_id+'/'+this.coin_id+'/')
                .then((res) => {
                    if (res.data.length > 0) {
                        this.owned_coins = res.data[0]['amount']
                    }
                })
                .catch((error) => {
                    console.log(error)
            })           
        }
    },
    created() {
        this.coin_id = this.$route.params.id
        this.getUserCoins()
        this.owned_cash = this.cash
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
.container {
    width: 400px;
    background-color: rgb(41, 37, 26);
    padding: 10px;
}

.container button {
    background-color: rgb(79, 70, 70);
}

.container input {
    font-size: 18px;
    width: 100px;
}

.first_column {
    width: 50%;
}

.button_div {
    margin-left: auto;
    margin-right: auto;
    width: fit-content;
}

.single_row {
    display: flex;
    margin-bottom: 5px;
}
</style>