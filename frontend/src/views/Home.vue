<template>
  <div>
      <TopMenu        
            :el1= pp.el1
            :el2= pp.el2
            :el3= pp.el3
            :el4= pp.el4
             />
  </div>
</template>

<script>
import TopMenu from "@/components/TopMenu";

export default {
  name: "HomePage",
  components: {
      TopMenu
  },
      data() {
        return {
            pp: {
            el1: 'Menu',
            el2: '20.05.2022',
            el3: '17:30:15',
            el4: 'User1',
        }}
    },
  mounted() {

  },
  computed: {

  }
};
</script>

<style>
body {
    font-size: 24;
    color: white;
    background: rgb(79, 70, 70); 
}
</style>