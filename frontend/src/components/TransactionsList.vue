<template>
    <table>
        <tr>
            <th>Czas transakcji</th>
            <th>Typ transakcji</th>
            <th>Kryptowaluta</th>
            <th>Ilość</th>
            <th>Wartość transakcji</th>
        </tr>
        <tr v-for="transaction in transactions_data" v-bind:key="transaction">
            <td>{{ format_date(transaction.date_time) }}</td>
            <td>{{ translate_types(transaction.transaction_type) }}</td>
            <td>{{ name_data[transaction.coins] }} [{{transaction.coins}}]</td>
            <td>{{ parseFloat(transaction.coins_amount.toFixed(4)) }}</td>
            <td>{{ parseFloat(transaction.total_value.toFixed(4)) }} €</td>
        </tr>
    </table>
</template>

<script>
export default {
    name: "TransactionsList",
    props: {
        transactions_data: Object,
        name_data: Object,
    },
    methods: {
        translate_types(transaction_type) {
            if (transaction_type == 1) {
                return 'Kupno'
            }
            else {
                return 'Sprzedaż'
            }
        },
        format_date(date_time) {
            return Intl.DateTimeFormat(navigator.language, {
                day: '2-digit',
                month: '2-digit',
                year: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                timeZone: 'UTC'
            }).format(new Date(date_time))        
        },
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