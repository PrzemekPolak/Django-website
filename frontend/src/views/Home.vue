<template>
  <div>
      <TopMenu        
            :el4 = pp.el4
             />
  </div>

  <div v-if="coins && current_price">
    <CoinListElement
       :coins = coins
       :current_price = current_price   
    />
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
         coins: [
                {
                    coin_id: 'BTC',
                    coin_name: 'Bitcoin'
                }, 
                {
                    coin_id: 'ETH',
                    coin_name: 'Ethereum'
                }, 
            ],
            current_price: [
                1111.22,
                2222.33
            ]
      }
    },
  mounted() {
    // this.loadData()
  },
  methods: {
    loadData() {
      console.log('bede pobierał')
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