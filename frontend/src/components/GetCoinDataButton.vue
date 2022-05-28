<template>
    <button @click="loadData()" type="button">{{buttonName}}</button>
</template>

<script>
export default {
    name: "GetCoinDataButton",
    props: {
        buttonName: String,
        timeRange: Number,
        dataIsOld: Boolean,
        coinId: String,
    },
  methods: {
    loadData() {
        var fetch_url = ''
        if (this.dataIsOld) {
            fetch_url = 'http://127.0.0.1:8000/api/coin_get_price/old/'+this.coinId+'/'+this.timeRange
        }
        else {  
            fetch_url = 'http://127.0.0.1:8000/api/coin_get_price/'+this.coinId+'/'+this.timeRange
        } 
            fetch(fetch_url)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    this.$emit('clicked', data)
                })
                .catch(err => {
                    console.log(err)
                })
    },
  },
};
</script>

<style>
button {
    width: 210px;
    padding: 10px;
    font-size: 20px;
    border: ridge;
    border-top-style: groove;
    border-right-style: groove;
    border-color: rgb(79, 70, 70);
    background: rgb(41, 37, 26);
    color: white;
}

button:hover {
    border-color: rgb(219, 215, 215);
    background: rgb(59, 57, 53);
    cursor: pointer;
}
</style>