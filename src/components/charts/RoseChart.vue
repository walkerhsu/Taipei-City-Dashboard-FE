<template>
    <div v-if="activeChart === 'RoseChart'" :style="{width: '100%', height: '100%'}">
		<div :style="{width: '100%', height: '80%'}" class="initial_animation">
			<canvas id="myChart" ref="myChart" width="0" height="0"></canvas>
		</div>
		<div :style="{width: '100%', height: '20%', display: 'flex', justifyContent: 'center', alignItems: 'center'}">
			<div v-for="(color, index) in props.chart_config['color']" :key="`${index}-${color}`">
				<div :style="{width: '10px', height: '10px', backgroundColor: color, borderRadius: '50%'}"></div>
				<div :style="{marginLeft: '5px', fontSize: '1rem', fontWeight: '400'}">{{ props.series[index]['name'] }}</div>
			</div>
		</div>
    </div>
</template>

<script setup>
import { onMounted, onUpdated } from 'vue'
// import { useMapStore } from '../../store/mapStore';

const props = defineProps(['chart_config', 'activeChart', 'series', 'map_config']);
function drawRoseChart(canvasId) {
	const canvas = document.getElementById(canvasId);
	if (canvas == null) {
		return;
	}
	canvas.width = canvas.parentElement.clientWidth;
	canvas.height = canvas.parentElement.clientHeight;
	const context = canvas.getContext("2d");
	const centerX = canvas.width / 2;
	const centerY = canvas.height / 2;
	let maxRadius = Math.min(centerX, centerY) / (props.series.length-0.2);
	let numPetals = props.series[0]['data'].length;

	let maxValues = []
	let lastPoints = []
	let allRadius = []
	for (let i = 0; i < numPetals; i++) {
		lastPoints.push([centerX, centerY, centerX, centerY]);
		allRadius.push(0);
	}

	for (let i = 0; i < props.series.length; i++) {
		let maxValue = -100
		for (let j = 0; j < numPetals; j++) {
			if (maxValue < props.series[i]['data'][j]['y']) {
				maxValue = props.series[i]['data'][j]['y']
			}
		}
		maxValues.push(maxValue)
	}


	context.clearRect(0, 0, canvas.width, canvas.height);

	const angleIncrement = (2 * Math.PI) / numPetals;
	for (let i = 0; i < props.series.length; i++) {
		let color = props.chart_config['color'][i % props.chart_config['color'].length];
		for (let j = 0; j < numPetals; j++) {
			const angle = j * angleIncrement;
			const radius = maxRadius * (props.series[i]['data'][j]['y'] / maxValues[i]);
			const x = centerX + (allRadius[j] + radius) * Math.cos(angle);
			const y = centerY + (allRadius[j] + radius) * Math.sin(angle);
			const x2 = centerX + (allRadius[j] + radius) * Math.cos(angle + angleIncrement);
			const y2 = centerY + (allRadius[j] + radius) * Math.sin(angle + angleIncrement);
			
			context.fillStyle = color; // Set the fill color to red
			// context.strokeStyle = color;
			// context.beginPath();
			// context.moveTo(222.83333333333334, 121)
			// context.lineTo(217.42969128597235, 100.83333333333334);
			// context.stroke();
			let region = new Path2D();
			region.moveTo(lastPoints[j][0], lastPoints[j][1]);
			region.lineTo(x, y);
			region.arc(centerX, centerY, radius + allRadius[j], angle, angle+angleIncrement, false);
			if (i === 0) region.closePath();
			else {
				region.lineTo(lastPoints[j][2], lastPoints[j][3]);
				region.arc(centerX, centerY, allRadius[j], angle + angleIncrement, angle, true);
				// region.closePath();
			}
			lastPoints[j] = [x, y, x2, y2];
			allRadius[j] += radius;
			context.fill(region);
		}
	}
}
onMounted(() => {
	drawRoseChart('myChart');
})
onUpdated(() => {
	drawRoseChart('myChart');
})
</script>

<style lang="scss">

.initial_animation {
	animation: initial_animation 1s ease-in-out;
}

@keyframes initial_animation {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}

</style>