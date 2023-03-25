<template>
  <h1>Charts TODO!</h1>
  <div ref="chart" class="chart shadow"></div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from "vue";
import * as echarts from "echarts/core";
import { GridComponent } from "echarts/components";
import { LineChart } from "echarts/charts";
import { UniversalTransition } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";

const chart = ref<HTMLDivElement | null>(null);

onMounted(() => {
  echarts.use([GridComponent, LineChart, CanvasRenderer, UniversalTransition]);

  let myChart = echarts.init(chart.value!);
  let option;

  option = {
    xAxis: {
      type: "category",
      data: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: [150, 230, 224, 218, 135, 147, 260, 50, 70, 110, 130, 230, 224, 218, 135, 147, 260, 50, 70, 110, 130, 230, 224, 218, 135, 147, 260, 50, 70, 110, 130],
        type: "line",
      },
    ],
  };

  option && myChart.setOption(option);
});
</script>

<style lang="scss" scoped>
@import "../assets/css/vars.scss";
.chart {
  margin: 10px 20px;
  background-color: $white;
  width: 600px;
  height: 300px;
}

.shadow {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
}
</style>
