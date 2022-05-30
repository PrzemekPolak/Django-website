<template>
  <div>
      <MenuTop        
            :user_name = user_name
            :logged_in_user = logged_in_user
             />
  </div>

  <div class="home_list_title">
    <div class="home_list_title_names">Dostępne kryptowaluty:</div>
    <div class="home_list_title_prices">Obecne ceny:</div>
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
import MenuTop from "@/components/MenuTop";
import CoinListElement from "@/components/CoinListElement";

export default {
   name: "HomePage",
   components: {
      MenuTop,
      CoinListElement
   },
   data() {
      return {
         logged_in_user: false,
         user_name: null,
         user_id: null,
         cash: null,
         pp: {
            el4: 'User1',
         },
         list_data: [],
      }
    },
  methods: {
    loadData() {
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
    },
    getCookies() {
      const dict = {}
      document.cookie.split('; ').map(c => {
        const [ key, v ] = c.split('=');
        dict[key] = v
      });
      // set values here only when first cookie is not undefined
      if (dict['logged_in_user'] != undefined) {
        this.logged_in_user = dict['logged_in_user']
        this.user_name = dict['user_name']
        this.user_id = dict['user_id']
        this.cash = dict['cash']
      }
    },
  },
  created() {
    this.loadData()
    this.getCookies()
  }
};
</script>

<style>
body {
    font-size: 24px;
    color: white;
    background: rgb(79, 70, 70); 
}

.home_list_title {
    display: flex;
    font-size: 26px;
    font-style: italic;
    padding-left: 20px;
    font-weight: bold;
}

.home_list_title_names {
    width: 300px;
}

.home_list_title_prices {
    width: 200px;
}

</style>