<template>
  <div>
      <TopMenu        
        :el4 = pp.el4
      />
  
  <div>
      detale {{ $route.params.id }}
  </div>
  
  <div class="chart-container">
        <CoinChart
            :coinData = coin_data
            :coin_id = coin_id
        />
    </div>
<button @click="testupdate()" type="button">test</button>
  </div>  
</template>

<script>
import TopMenu from "@/components/TopMenu";
import CoinChart from "@/components/CoinChart";

export default {
  name: "CoinDetail",
  components: {
      TopMenu,
      CoinChart,
  },
      data() {
        return {
            time_range: 12,
            coin_data: {},
            coin_id: '',

            pp: {
              el4: 'User',
            },

    }},
  mounted() {
  },
  methods: {
    loadData() {
        const fetch_url = 'http://127.0.0.1:8000/api/coin_get_price/'+this.coin_id+'/'+this.time_range
                fetch(fetch_url)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    this.coin_data = data
                })
                .catch(err => {
                    console.log(err)
                })
    },
    testupdate() {
        const fetch_url = 'http://127.0.0.1:8000/api/coin_get_price/'+this.coin_id+'/'+6
                fetch(fetch_url)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    this.coin_data = data
                })
                .catch(err => {
                    console.log(err)
                })      
    }
  },
  created() {
    this.coin_id = this.$route.params.id
    this.loadData()
  },

  computed: {

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