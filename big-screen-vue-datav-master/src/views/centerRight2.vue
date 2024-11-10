<template>
  <div id="centerRight2">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="align-left" class="text-icon"></icon>
        </span>
        <span class="text mx-2">汽车销售价格分布</span>
      </div>
      <div class="d-flex ai-center flex-column body-box">
        <dv-capsule-chart class="dv-cap-chart" :config="config" v-bind:key="this.config.data[0].value" style="height: 170px"/>
        <dv-active-ring-chart :config="dynamicPieConfig" style="width:250px;height:250px" v-bind:key="this.dynamicPieConfig.data[0].value"/>
        <!--        <centerRight2Chart1/>-->
      </div>
    </div>
  </div>
</template>

<script>
// import centerRight2Chart1 from '@/components/echart/centerRight/centerRightChart'

export default {
  data() {
    return {
      dynamicPieConfig: {
        data: []
      },
      config: {
        data: []
      }
    }
  },
  components: {
    // centerRight2Chart1
  },
  async mounted() {
    const res = await this.$http.get('/myApp/centerRight')
    console.log("getCenterRightData:", res)
    this.$set(this.config, 'data', res.data.priceSortList)
    this.$set(this.dynamicPieConfig, 'data', res.data.priceSortList)
  }
  // methods: {}
}
</script>

<style lang="scss" scoped>
#centerRight2 {
  $box-height: 410px;
  $box-width: 340px;
  padding: 5px;
  height: $box-height;
  width: $box-width;
  border-radius: 5px;

  .bg-color-black {
    padding: 5px;
    height: $box-height;
    width: $box-width;
    border-radius: 10px;
  }

  .text {
    color: #c3cbde;
  }

  .body-box {
    border-radius: 10px;
    overflow: hidden;

    .dv-cap-chart {
      width: 100%;
      height: 160px;
    }
  }
}
</style>
