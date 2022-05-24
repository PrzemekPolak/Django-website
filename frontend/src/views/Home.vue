<template>
  <div>
      <TopMenu        
            :el4 = pp.el4
             />
  </div>

  <div v-if="list_data[0]">
    <div v-for="data in list_data" v-bind:key="data">
      <CoinListElement
        :coin_id = data.coin_id
        :coin_name = data.coin_name
        :current_price = data.current_price
      />
    </div>
  </div>
  <p v-else>Coins or prices are unavailable.</p>


</template>

<script>
import TopMenu from "@/components/TopMenu";
import CoinListElement from "@/components/CoinListElement";

export default {
   name: "HomePage",
   components: {
      TopMenu,
      CoinListElement
   },
   data() {
      return {
         pp: {
            el4: 'User1',
         },
         list_data: [],
      }
    },
  mounted() {
    // this.loadData()
  },
  methods: {
    loadData() {
      console.log('bede pobierał')
                fetch('http://127.0.0.1:8000/api/coin_list/')
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    this.list_data = data
                })
                .catch(err => {
                    console.log(err)
                })
    }
  },
  created() {
    this.loadData()
  }
};
</script>

<style>
body {
    font-size: 24px;
    color: white;
    background: rgb(79, 70, 70); 
}
</style>