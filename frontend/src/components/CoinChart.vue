<template>

  <Line
    :chart-options="chartOptions"
    :chart-data="chartData"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
  />

</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, LinearScale, CategoryScale, PointElement} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, LinearScale, CategoryScale, PointElement)

export default {
  name: "CoinChart",
  props: {
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    },
      coinData: Object,
      coin_id: String,
  },
  components: {
      Line,
  },
      data() {
        return {
            chartOptions: {
                responsive: true,
                maintainAspectRatio: false,
                color: "white",
                scales: {
                  yAxes: {
                      ticks: {
                          color: "white",
                          font: {
                              size: 16,
                          },
                      }
                  },
                  xAxes: {
                      ticks: {
                          color: "white",
                          font: {
                              size: 16,
                          },
                      }
                  },
                },
            },
    }},
  computed: {
    chartData() { 
        return {
            labels: this.coinData.labels,
            datasets: [
                {
                    label: this.coin_id + ' (w euro)',
                    data: this.coinData.data,
                    backgroundColor: 'rgb(235, 233, 230)',
                    borderColor: 'red',
                    borderWidth: 2,
                }
            ]
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
</style>