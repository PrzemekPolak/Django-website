<template>
  <div>
      <TopMenu        
            :el1= pp.el1
            :el2= pp.el2
            :el3= pp.el3
            :el4= pp.el4
             />
  
  <div>
      detale {{ $route.params.id }}
  </div>
  
  </div>  
</template>


<script>
import TopMenu from "@/components/TopMenu";

export default {
  name: "CoinDetail",
  components: {
      TopMenu
  },
      data() {
        return {
            pp: {
        }}
    },
  mounted() {

  },
  computed: {

  }
};
</script>

<style>

</style>