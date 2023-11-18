<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { ref, computed } from 'vue';
import { useMapStore } from '../../store/mapStore';

const props = defineProps(['chart_config', 'activeChart', 'series', 'map_config']);

const mapStore = useMapStore();

const chartOptions = ref({
	chart: {
          height: 350,
          type: 'scatter',
          animations: {
            enabled: false,
          },
	zoom: {
            enabled: false,
          },
	toolbar: {
            show: false
          }
        },
	colors: ['#056BF6', '#D2376A'],
	xaxis: {
          tickAmount: 10,
          min: 0,
          max: 40
        },
	yaxis: {
          tickAmount: 7
        },
        markers: {
          size: 20
        },
	fill: {
          type: 'image',
          opacity: 1,
          image: {
            src: ['../../assets/images/ico-messenger.png', '../../assets/images/ico-instagram.png'],
            width: 40,
            height: 40
          }
        },
	legend: {
          labels: {
            useSeriesColors: true
          },
	markers: {
		customHTML: [
			function() {
			return ''
			}, function() {
			return ''
			}
		]
		}
	},
	tooltip: {
		custom: function ({ series, seriesIndex, dataPointIndex, w }) {
			return '<div class="chart-tooltip">' +
				'<h6>' + w.globals.labels[dataPointIndex] + '</h6>' +
				'<span>' + series[seriesIndex][dataPointIndex] + ` ${props.chart_config.unit}` + '</span>' +
				'</div>';
		},
		followCursor: true,
	},
});

const chartHeight = computed(() => {
	return `${40 + props.series[0].data.length * 24}`;
});

const selectedIndex = ref(null);

function handleDataSelection(e, chartContext, config) {
	if (!props.chart_config.map_filter) {
		return;
	}
	if (config.dataPointIndex !== selectedIndex.value) {
		mapStore.addLayerFilter(`${props.map_config[0].index}-${props.map_config[0].type}`, props.chart_config.map_filter[0], props.chart_config.map_filter[1][config.dataPointIndex]);
		selectedIndex.value = config.dataPointIndex;
	} else {
		mapStore.clearLayerFilter(`${props.map_config[0].index}-${props.map_config[0].type}`);
		selectedIndex.value = null;
	}
}

function printChartConfig(chartConfig) {
	console.log(chartConfig);
}

</script>

<template>
	<div v-if="activeChart === 'HexagonalBinning'">
		<apexchart width="100%" :height="chartHeight" type="scatter" :options="chartOptions" :series="series"
			@dataPointSelection="handleDataSelection" ></apexchart>
	</div>
</template>