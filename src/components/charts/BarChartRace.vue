<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import SingleBar from "./SingleBar.vue";

const props = defineProps([
	"chart_config",
	"activeChart",
	"series",
	"map_config",
]);

// use transition-group to perform bar chart race animation
function getColor(index, name) {
	props.chart_config['fixed']
	if (props.chart_config['fixed']) {
		return this.colorMap[index];
	} else {
		return this.colorMap[name];
	}
}
const colorMap = {};
if (props.chart_config['fixed']) {
	for (let i = 0; i < props.chart_config.color.length; i++) {
		colorMap[i] =
		props.chart_config.color[i % props.chart_config.color.length];
	}
} else {
	for (let i = 0; i < props.series[0]['data'].length; i++) {
		colorMap[props.series[0]['data'][i]['x']] =
		props.chart_config.color[i % props.chart_config.color.length];
	}
}

const oneBarHeight = computed(() => {
	return `30px`;
});

const maxNumber = computed(() => {
	return props.series[historyDataIndex.value]['data'][0]['y'];
})

const historyDataIndex = ref(0);
let timer = null;
onMounted(() => {
	timer = setInterval(() => {
		if (historyDataIndex.value === props.series.length - 1) {
			historyDataIndex.value = 0;
		} else {
			historyDataIndex.value++;
		}
	}, 3000);
});

onUnmounted(() => {
	if (timer) clearInterval(timer);
});

</script>

<template>
	<div v-if="activeChart === 'BarChartRace'" class="BarChartRace">
		<transition name="slide" mode="out-in">
			<div class="BarChartRaceYear" :key="`${historyDataIndex}_${series[historyDataIndex]['name']}`">
				{{ series[historyDataIndex]['name'] }}
			</div>
		</transition>
		<TransitionGroup name="list" tag="ul">
			<li v-for="(data, index) in series[historyDataIndex]['data']" 
			:key="data['x']+'-'+data['x']">
				<SingleBar :title="data['x']" :number="data['y']" :height="oneBarHeight" 
				:index="index" :maxNumber="maxNumber" :color="getColor(index, data['x'])"/>
			</li>
		</TransitionGroup>
	</div>
</template>

<style lang="scss">
.BarChartRace {
	padding: 20px;
}
.BarChartRaceYear{
	// center
	text-align: center;
}
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