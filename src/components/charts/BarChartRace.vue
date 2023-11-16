<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useMapStore } from "../../store/mapStore";
import SingleBar from "./SingleBar.vue";

const props = defineProps([
	"chart_config",
	"activeChart",
	"series",
	"map_config",
]);
const mapStore = useMapStore();

// use transition-group to perform bar chart race animation

const NameToColor = computed(() => {
	const colorMap = {};
	for (let i = 0; i < props.series[0]['data'].length; i++) {
		colorMap[props.series[0]['data'][i]['x']] =
			props.chart_config.color[i % props.chart_config.color.length];
	}
	return colorMap;
});

const oneBarHeight = computed(() => {
	return `30px`;
});

const selectedIndex = ref(null);

const maxNumber = computed(() => {
	return props.series[historyDataIndex.value]['data'][0]['y'];
})

function handleDataSelection(e, chartContext, config) {
	if (!props.chart_config.map_filter) {
		return;
	}
	if (config.dataPointIndex !== selectedIndex.value) {
		mapStore.addLayerFilter(
			`${props.map_config[0].index}-${props.map_config[0].type}`,
			props.chart_config.map_filter[0],
			props.chart_config.map_filter[1][config.dataPointIndex]
		);
		selectedIndex.value = config.dataPointIndex;
	} else {
		mapStore.clearLayerFilter(
			`${props.map_config[0].index}-${props.map_config[0].type}`
		);
		selectedIndex.value = null;
	}
}
const historyDataIndex = ref(0);
let timer = null;
onMounted(() => {
	timer = setInterval(() => {
		if (historyDataIndex.value === props.series.length - 1) {
			historyDataIndex.value = 0;
		} else {
			historyDataIndex.value++;
		}
	}, 2000);
});

onUnmounted(() => {
	if (timer) clearInterval(timer);
});

</script>

<template>
	<div v-if="activeChart === 'BarChartRace'">
		<TransitionGroup name="list" tag="ul">
			<li v-for="(data, index) in series[historyDataIndex]['data']" 
			:key="data['x']+'-'+data['x']">
				<SingleBar :title="data['x']" :number="data['y']" :handleDataSelection="handleDataSelection" :height="oneBarHeight" :index="index" :maxNumber="maxNumber" :color="NameToColor[data['x']]"/>
			</li>
		</TransitionGroup>
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

</style>