<template>
  <MenuTop        
    :user_name = user_name
    :logged_in_user = logged_in_user
  /> 
  <div class="page_title">{{ coin_name }} [{{ coin_id }}] (w euro)</div>
    <div class="chart_buttons_container">
      <div class="chart-container">
        <CoinChart
            :coinData = coin_data
            :coin_id = coin_id
        />
    </div>
    <div class="buttons_container">
      <div v-for="elem in button_list" v-bind:key="elem">
        <GetCoinDataButton @clicked="onClickCoinButton"
            :buttonName = elem[0]
            :timeRange = elem[1]
            :dataIsOld = elem[2]
            :coinId = coin_id
        />
      </div>
    </div>
  </div>
  <div v-if="logged_in_user" class="buy_sell_form">
    <button @click="show_buy_form = true" type="button">Zakup</button>
    <button @click="show_buy_form = false" type="button">Sprzedaż</button>
    <CoinBuySellForm 
      :coin_price = coin_buy
      :user_id = user_id
      :show_buy_form = show_buy_form
      :cash = cash
    />
  </div>
</template>

<script>
import MenuTop from "@/components/MenuTop";
import CoinChart from "@/components/CoinChart";
import GetCoinDataButton from "@/components/GetCoinDataButton";
import CoinBuySellForm from "@/components/CoinBuySellForm";

export default {
  name: "CoinDetail",
  components: {
    MenuTop,
    CoinChart,
    GetCoinDataButton,
    CoinBuySellForm,
},
      data() {
        return {
            logged_in_user: false,
            user_name: null,
            user_id: null,
            cash: null,
            time_range: 24,
            coin_data: {},
            coin_id: '',
            coin_name: '',
            button_list: [
              ['Ostatnie 4 godziny', 4, false],
              ['Ostatnie 8 godziny', 8, false],
              ['Ostatnie 12 godziny', 12, false],
              ['Ostatnie 24 godziny', 24, false],
              ['Ostatni tydzień', 7, true],
              ['Ostatni miesiąc', 30, true],
              ['Ostatnie 3 miesiące', 90, true],
              ['Ostatnie 6 miesięcy', 180, true],
            ],
            show_buy_form: true,

    }},
  mounted() {
  },
  methods: {
    onClickCoinButton (value) {
        this.coin_data = value
    },
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

          fetch('http://127.0.0.1:8000/api/get_coin_name/'+this.coin_id+'/')
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    this.coin_name = data[0]['coin_name']
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
    this.coin_id = this.$route.params.id
    this.loadData()
    this.getCookies()
  },

  computed: {
    coin_buy: function() {
      try {
        return this.coin_data.data.at(-1)
      }
      catch {
        return 0
      }
    }
  }
};
</script>

<style>
body {
    font-size: 24px;
    color: white;
    background: rgb(79, 70, 70); 
}

.chart_buttons_container {
    display: flex;
}

.buttons_container {
    display: block;
}

.chart-container {
    width: 100%;
    margin-right: auto;
    margin-left: auto;  
}

.buy_sell_form {
    margin-top: 10px;
    margin-left: 10px;
}

.page_title {
    font-size: 32px;
    text-align: center;
    margin-bottom: 20px;
}
</style>