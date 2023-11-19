<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { ref } from "vue";

const props = defineProps(["chart_config", "activeChart", "series"]);

var max = 0;
var ymax = [];
for (var i = 0; i < props.series.length; i++) {
	max = 0;
	for (var j = 0; j < props.series[i]["data"].length; j++) {
		// console.log(props.series[i]['data'][j]);
		if (props.series[i]["data"][j].y > max) {
			max = props.series[i]["data"][j].y;
		}
	}
	console.log(max);
	ymax.push(max);
}
console.log(ymax);
const chartOptions = ref({
	chart: {
		id: "realtime",
		toolbar: {
			show: false,
			tools: {
				zoom: false,
			},
		},
		animations: {
			enabled: true,
			easing: "linear",
			speed: 800,
			animateGradually: {
				enabled: true,
				delay: 150,
			},
			dynamicAnimation: {
				enabled: true,
				speed: 350,
			},
		},
	},

	fill: {
		type: "gradient",
		gradient: {
			type: "vertical",
			colorStops: [
				{
					offset: 0,
					color: "#ED2939",
				},
				{
					offset: 100 / 6,
					color: "#6F2DA8",
				},
				{
					offset: 200 / 6,
					color: "#FFF700",
				},
				{
					offset: 300 / 6,
					color: "#FFBF00",
				},
				{
					offset: 400 / 6,
					color: "#FFF700",
				},
				{
					offset: 500 / 6,
					color: "#3CB043",
				},
			],
		},
	},
	dataLabels: {
		enabled: false,
	},
	grid: {
		show: true,
		borderColor: "#90A4AE",
	},
	legend: {
		show: props.series.length > 1 ? true : false,
	},
	markers: 0,
	stroke: {
		colors: props.chart_config.color,
		curve: "smooth",
		show: true,
		width: 2,
	},
	tooltip: {
		custom: function ({ series, seriesIndex, dataPointIndex, w }) {
			// The class "chart-tooltip" could be edited in /assets/styles/chartStyles.css
			return (
				'<div class="chart-tooltip">' +
				"<h6>" +
				`${parseTime(
					w.config.series[seriesIndex].data[dataPointIndex].x
				)}` +
				` - ${w.globals.seriesNames[seriesIndex]}` +
				"</h6>" +
				"<span>" +
				series[seriesIndex][dataPointIndex] +
				` ${props.chart_config.unit}` +
				"</span>" +
				"</div>"
			);
		},
	},
	xaxis: {
		axisBorder: {
			color: "#555",
			height: "0.8",
		},
		axisTicks: {
			show: false,
		},
		crosshairs: {
			show: false,
		},
		tooltip: {
			enabled: false,
		},
		type: "datetime",
	},
	yaxis: {
		labels: {
			formatter: function (val) {
				return val.toFixed(0);
			},
		},
	},
});

function parseTime(time) {
	return time.replace("T", " ").replace("+08:00", " ");
}
</script>

<template>
	<div v-if="activeChart === 'TimelineColorChart'">
		<!-- <li v-for="(data, index) in props.series" :key="data['name']">
			{{ data['name'] }}
		</li> -->
		<apexchart
			width="100%"
			height="260px"
			type="line"
			:options="chartOptions"
			:series="series"
		></apexchart>
		<!-- <TransitionGroup name="list">
			<li v-for="(data, index) in props.series" :key="data['name']">
				<apexchart
					width="100%"
					height="260px"
					type="line"
					:options="chartOptions"
					:series="data"
				></apexchart>
			</li> -->
		<!-- </TransitionGroup> -->
	</div>
</template>

<style lang="scss">
.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}

.slide-leave-active,
.slide-enter-active {
  transition: all .2s ease;
}

.slide-enter-from {
  transform: translateX(-100%);
}

.slide-leave-to {
  transform: translateX(100%);
}

</style>