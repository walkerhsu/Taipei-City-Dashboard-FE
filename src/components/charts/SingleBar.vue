<script setup>
import { computed } from 'vue'

const props = defineProps(['title', 'number', 'handleDataSelection', 'height', 'index', 'maxNumber', 'color']);
// const mapStore = useMapStore();
const yLabel = computed(() => {
	return props.title.length > 7 ? props.title.slice(0, 6) + "..." : props.title
});
const barWidth = computed(() => {

	return (props.number / props.maxNumber * 100) >= 25 ?
		(props.number / props.maxNumber * 100) - 25 : 1
});

</script>
<template>
    <div class="one-row" :style="{ 'height': props.height }">
		<h6 class="yLabel" :style="{'width': '25%'}">{{ yLabel }}</h6>
		<div v-on:click="handleDataSelection" class="bar" :style="{'width': `${barWidth}%`, 'backgroundColor': props.color}">
			<div v-if="barWidth >= 8" >{{ props.number }}</div>
		</div>
		<div v-if="barWidth < 8" class="outside_number">{{ props.number }}</div>
	</div>
</template>
<style lang="scss">
.one-row {
	display: flex;
	flex-direction: row;
	justify-content: flex-start;
	align-items: center;
	width: 100%;
	margin: 6px 0;
	
	.bar {
		width: 100%;
		height: 100%;
		// background-color: #277833;
		border-radius: 5px;
		transition: width 0.5s ease-in-out;
	}

	.outside_number {
		margin: 3px 0;
	}
}
</style>