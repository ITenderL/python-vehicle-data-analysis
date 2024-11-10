<template>
  <div id="centerRight1">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="chart-line" class="text-icon"></icon>
        </span>
        <div class="d-flex">
          <span class="text mx-2">油车电车对比</span>
          <a v-on:click="oil" href="#" class="text mx-2" style="color: #4394e4">油车</a>
          <a v-on:click="electric" href="#" class="text mx-2" style="color: #33cea0">电车</a>
        </div>
      </div>
      <div class="d-flex jc-center body-box">
        <dv-scroll-board class="dv-scr-board" :config="config" v-bind:key="this.config.data[0][1]"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      config: {
        header: ['车名', '销量/台', '能源'],
        data: [
          ['序号', 1, "<span  class='colorGrass'>↑75%</span>"],
        ],
        rowNum: 7, //表格行数
        headerHeight: 35,
        headerBGC: '#0f1325', //表头
        oddRowBGC: '#0f1325', //奇数行
        evenRowBGC: '#171c33', //偶数行
        index: true,
        columnWidth: [50],
        align: ['center']
      }
    }
  },
  methods: {
    async electric() {
      const res = await this.$http.get('/myApp/centerRightChange/2')
      this.$set(this.config, 'data', res.data.result)
    },
    async oil() {
      const res = await this.$http.get('/myApp/centerRightChange/1')
      this.$set(this.config, 'data', res.data.result)
    }
  },
  async mounted() {
    const res = await this.$http.get('/myApp/centerRightChange/1')
    this.$set(this.config, 'data', res.data.result)
  }
}
</script>

<style lang="scss" scoped>
$box-height: 410px;
$box-width: 300px;
#centerRight1 {
  padding: 16px;
  padding-top: 20px;
  height: $box-height;
  width: $box-width;
  border-radius: 5px;
  .bg-color-black {
    height: $box-height - 30px;
    border-radius: 10px;
  }
  .text {
    color: #c3cbde;
  }
  .body-box {
    border-radius: 10px;
    overflow: hidden;
    .dv-scr-board {
      width: 270px;
      height: 340px;
    }
  }
}
</style>
