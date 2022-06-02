<template>

    <MenuTop        
        :user_name = user_name
        :logged_in_user = logged_in_user
    />

    <div class="wallet_header">Historia Transakcji</div>

    <TransactionsList
        :transactions_data = transactions_data
        :name_data = name_data
    />

</template>

<script>
import MenuTop from "@/components/MenuTop";
import TransactionsList from "@/components/TransactionsList";

export default {
  name: "UserTransactions",
  components: {
    MenuTop,
    TransactionsList,
},
      data() {
        return {
            logged_in_user: false,
            user_name: null,
            user_id: null,
            cash: null,
            transactions_data: {},
            name_data: {}
    }},
  mounted() {
  },
  methods: {
    loadData() {
        fetch('http://127.0.0.1:8000/api/get_user_transactions/'+this.user_id+'/')
            .then(response => {
                return response.json()
            })
            .then(data => {
                this.transactions_data = data
            })
            .catch(err => {
                console.log(err)
            })

        fetch('http://127.0.0.1:8000/api/coin_list/')
            .then(response => {
                return response.json()
            })
            .then(data => {
                for (var i = 0; i < data.length; i++) {
                    this.name_data[data[i].coin_id] = data[i].coin_name
                }
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
    this.getCookies()
    this.loadData()
  },
};
</script>

<style>
body {
    font-size: 24px;
    color: white;
    background: rgb(79, 70, 70); 
}

.wallet_header {
    text-align: center;
    margin: 20px;
    font-weight: bold;
    font-size: 32px;
}
</style>