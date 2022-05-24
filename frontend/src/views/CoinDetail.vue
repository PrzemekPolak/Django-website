<template>
  <div>
      <TopMenu        
        :el4 = pp.el4
      />
  
  <div>
      detale {{ $route.params.id }}
  </div>
  
  <div class="chart-container">
    <!-- <canvas id="myChart" style="background-color:#29251a;"></canvas> -->
        <LineChart
            :chart-data = chartData
        />
    </div>


  </div>  
</template>

<script>
import TopMenu from "@/components/TopMenu";
import LineChart from "@/components/LineChart";

export default {
  name: "CoinDetail",
  components: {
      TopMenu,
      LineChart,
  },
      data() {
        return {
            chart_conf: {},
            chart_time_data: ['11-11-2011', '12-11-2011'],
            chart_price_data: [1111.22, 2111.22],
            chart_id_data: 'BTC',
            pp: {
              el4: 'User',
            },
      chartData: {
        labels: ['11-11-2011', '12-11-2011'],
        datasets: [
          {
            label: 'BTC',
            backgroundColor: 'rgb(235, 233, 230)',
            data: [1111.22, 2111.22]
          }
        ]
      },
    }},
  mounted() {
  },
  methods: {
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