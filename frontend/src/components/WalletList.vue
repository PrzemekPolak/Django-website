<template>
    <table>
        <tr>
            <th>Kryptowaluta</th>
            <th>Ilość</th>
            <th>Średnia cena zakupu</th>
            <th>Aktualna cena</th>
            <th>Różnica</th>
        </tr>
        <tr v-for="asset in assets_data" v-bind:key="asset">
            <td>{{ name_data[asset.coins] }} [{{asset.coins}}]</td>
            <td>{{ parseFloat(asset.amount.toFixed(4)) }}</td>
            <td>{{ parseFloat(asset.average_price.toFixed(4)) }} €</td>
            <td>{{ price_data[asset.coins] }} €</td>
            <td>{{ compute_change(asset.average_price, asset.coins) }}</td>
        </tr>
    </table>
</template>

<script>
export default {
    name: "WalletList",
    props: {
        assets_data: Array,
        price_data: Object,
        name_data: Object,
    },
    methods: {
        compute_change(average_price, coin_id) {
            const change = parseFloat((this.price_data[coin_id] - average_price).toFixed(4))
            const percent_change = parseFloat((change * 100 / average_price).toFixed(2))
            if (isNaN(change) || isNaN(percent_change)) {
                return 'Brak danych'
            }
            if (percent_change > 0) {
                return change + ' € (+' + percent_change + '%)'
            }
            return change + ' € (' + percent_change + '%)'
        }
    },
};
</script>

<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
}

td, th {
  border: 2px solid #dddddd;
  text-align: center;
  padding: 10px;
  width: 250px;
}

tr:nth-child(even) {
  background-color: #2e2929;
}
</style>