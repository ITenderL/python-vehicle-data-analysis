<template>
  <div>
    <!--    <Chart :cdata="cdata"/>-->
    <div ref="chart" style="width: 100%; height: 470px" v-bind:key="this.cdata.lineData"
         @mouseleave="this.onLeave" @mouseenter="onHover"></div>
  </div>
</template>

<script>
// import Chart from './chart.vue'
export default {
  data() {
    return {
      isHovered: true,
      cdata: {
        category: [],
        lineData: [],
        barData: [],
        rateData: []
      }
    };
  },
  components: {
    // Chart,
  },
  async mounted() {
    const res = await this.$http.get("/myApp/bottomLeft");
    this.$set(this.cdata, "category", res.data.brandList);
    this.$set(this.cdata, "lineData", res.data.priceList);
    this.$set(this.cdata, "barData", res.data.volumeList);
  },
  updated() {
    this.initChart();
    this.startUpdateDataInterval();
  },
  methods: {
    // 鼠标悬浮事件
    onHover() {
      this.isHovered = false;
    },
    // 鼠标离开事件
    onLeave() {
      this.isHovered = true;
    },
    // 根据自己的业务情况修改
    initChart() {
      this.myChart = this.$echarts.init(this.$refs.chart);
      const option = {
        tooltip: {
          trigger: "axis",
          backgroundColor: "rgba(255,255,255,0.1)",
          axisPointer: {
            type: "shadow",
            label: {
              show: true,
              backgroundColor: "#7B7DDC"
            }
          }
        },
        dataZoom: [
          {
            type: "slider",
            show: false,
            start: 0,
            end: 95
          }
        ],
        legend: {
          data: ["已贯通", "计划贯通", "贯通率"],
          textStyle: {
            color: "#B4B4B4"
          },
          top: "0%"
        },
        grid: {
          x: "8%",
          width: "88%",
          y: "4%"
        },
        xAxis: {
          data: this.cdata.category,
          axisLine: {
            lineStyle: {
              color: "#B4B4B4"
            }
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            show: true,
            interval: 0
          }
        },
        yAxis: [
          {
            splitLine: {show: false},
            axisLine: {
              lineStyle: {
                color: "#B4B4B4"
              }
            },

            axisLabel: {
              formatter: "{value} "
            }
          },
          {
            splitLine: {show: false},
            axisLine: {
              lineStyle: {
                color: "#B4B4B4"
              }
            },
            axisLabel: {
              formatter: "{value} "
            }
          }
        ],
        series: [
          {
            name: "价格",
            type: "line",
            smooth: true,
            showAllSymbol: true,
            symbol: "emptyCircle",
            symbolSize: 8,
            yAxisIndex: 1,
            itemStyle: {
              normal: {
                color: "#F02FC2"
              }
            },
            data: this.cdata.lineData
          },
          {
            name: "销量",
            type: "bar",
            barWidth: 10,
            itemStyle: {
              normal: {
                barBorderRadius: 5,
                color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {offset: 0, color: "#956FD4"},
                  {offset: 1, color: "#3EACE5"}
                ])
              }
            },
            data: this.cdata.barData
          }
        ]
      };
      this.myChart.setOption(option);
    },
    // 修改柱状图数据
    changeData(x) {
      const st = x[0];
      for (let i = 0; i < x.length - 1; i++) {
        x[i] = x[i + 1]
      }
      x[x.length - 1] = st
    },
    // 更新柱状图数据
    updateBarChat() {
      if (this.isHovered) {
        this.changeData(this.cdata.category)
        this.changeData(this.cdata.barData)
        this.changeData(this.cdata.lineData)
        this.myChart.setOption({
          xAxis: {
            data: this.cdata.category,
          },
          series: [
            {
              data: this.cdata.barData,
            },
            {
              data: this.cdata.lineData,
            }
          ]
        })
      } else {
        clearInterval(this.timer)
      }
    },
    startUpdateDataInterval() {
      if (this.isHovered) {
        const interval = 3000;
        clearInterval(this.timer)
        setInterval(this.updateBarChat, interval);
      }
    }
  }
};
</script>

<style lang="scss" scoped>
</style>