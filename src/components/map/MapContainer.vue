<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { onMounted, ref } from "vue";
import { useMapStore } from "../../store/mapStore";
import { useDialogStore } from "../../store/dialogStore";
import { useContentStore } from "../../store/contentStore";
import { dates } from "../../assets/configs/apexcharts/aqiDates";
import MobileLayers from "../dialogs/MobileLayers.vue";

const mapStore = useMapStore();
const dialogStore = useDialogStore();
const contentStore = useContentStore();

const newSavedLocation = ref("");
const sliderValue = ref(50);

function handleSubmitNewLocation() {
	mapStore.addNewSavedLocation(newSavedLocation.value);
	newSavedLocation.value = "";
}

function handleSliderChange(e) {
	console.log("in again");
	// console.log(e.target.value);
	const date_idx = parseInt(parseFloat(e.target.value, 10) - 1);
	console.log(date_idx);
	filterBy(date_idx);
}
function filterBy(date_idx) {
	console.log(dates[date_idx]);
	const filters = ["==", "日期", dates[date_idx]];
	mapStore.map.setFilter("Taipei_Environment_new-circle", filters);
	mapStore.map.setFilter("Taipei_Environment_new-symbol", filters);

	document.getElementById("date").textContent = dates[date_idx];
}

onMounted(() => {
	mapStore.initializeMapBox();
});
</script>

<template>
	<div id="mapcontainer" class="mapcontainer">
		<div
			v-if="
				mapStore.currentLayers.includes('Taipei_Environment_new-circle')
			"
			class="map-overlay"
		>
			<div class="map-overlay-inner">
				<h2>Taipei Environment data</h2>
				<label id="date">{{ dates[0] }}</label>
				<input
					id="slider"
					type="range"
					name="range"
					min="1"
					max="90"
					step="1"
					v-model="sliderValue"
					@input="handleSliderChange"
				/>
				<!-- <br />
				<input v-model="sliderValue" type="number" /> -->
			</div>
			<div class="map-overlay-inner">
				<div id="legend" class="legend">
					<div>AQI Safety Index</div>
					<div class="bar"></div>
				</div>
			</div>
		</div>

		<div id="mapboxBox">
			<div
				class="mapcontainer-loading"
				v-if="mapStore.loadingLayers.length > 0"
			>
				<div></div>
			</div>
			<button
				class="mapcontainer-layers show-if-mobile"
				@click="dialogStore.showDialog('mobileLayers')"
			>
				<span>layers</span>
			</button>
			<!-- The key prop informs vue that the component should be updated when switching dashboards -->
			<MobileLayers :key="contentStore.currentDashboard.index" />
		</div>
		<div class="mapcontainer-controls hide-if-mobile">
			<button
				@click="
					mapStore.easeToLocation([
						[121.536609, 25.044808],
						12.5,
						0,
						0,
					])
				"
			>
				返回預設
			</button>
			<div
				v-for="(item, index) in mapStore.savedLocations"
				:key="`${item[4]}-${index}`"
			>
				<button @click="mapStore.easeToLocation(item)">
					{{ item[4] }}
				</button>
				<div
					class="mapcontainer-controls-delete"
					@click="mapStore.removeSavedLocation(index)"
				>
					<span>delete</span>
				</div>
			</div>
			<input
				v-if="mapStore.savedLocations.length < 10"
				type="text"
				placeholder="新增後按Enter"
				v-model="newSavedLocation"
				maxlength="6"
				@focusout="newSavedLocation = ''"
				@keypress.enter="handleSubmitNewLocation"
			/>
		</div>
	</div>
</template>

<style scoped lang="scss">
.map-overlay {
	font: 12px/20px "Helvetica Neue", Arial, Helvetica, sans-serif;
	width: 25%;
	top: 0;
	left: 0;
	padding: 10px;
	&-inner {
		background-color: black;
		box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
		border-radius: 3px;
		padding: 7px;
		margin-bottom: 10px;
		h2 {
			line-height: 24px;
			display: block;
			margin: 0 0 10px;
			color: white;
		}
		label {
			color: white;
		}

		input {
			padding: 0;
			background-color: black;
			display: inline-flex;
			width: 100%;
			border: 0;
			position: relative;
			margin: 0;
			margin-right: 15px;
			cursor: pointer;
		}
		#slider {
			font-family: "Avenir", Helvetica, Arial, sans-serif;
			-webkit-font-smoothing: antialiased;
			-moz-osx-font-smoothing: grayscale;
			text-align: center;
			color: #2c3e50;
		}
		.legend {
			.bar {
				height: 10px;
				width: 100%;
				background: linear-gradient(to right, #61d09c, #7f3121);
			}
		}
	}
}
.mapcontainer {
	position: relative;
	width: 100%;
	height: calc(100%);
	flex: 1;

	select {
		width: 200px;
		background: none;
		height: 30px;
		margin: 0;
		border: 3px solid #fff;
		border-radius: 10px;
	}

	select::after {
		display: block;
		font-size: 16px;
		top: 7px;
		color: #fff;
	}

	&-loading {
		position: absolute;
		top: 110px;
		right: 10px;
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 20;

		@media (max-width: 1000px) {
			top: 145px;
		}

		div {
			width: 1.3rem;
			height: 1.3rem;
			border-radius: 50%;
			border: solid 4px var(--color-border);
			border-top: solid 4px var(--color-highlight);
			animation: spin 0.7s ease-in-out infinite;
		}
	}

	&-controls {
		display: flex;
		margin-top: 8px;
		overflow: visible;

		button {
			height: 1.5rem;
			width: fit-content;
			margin-right: 6px;
			padding: 4px;
			border-radius: 5px;
			background-color: var(--color-component-background);
			color: var(--color-complement-text);

			&:focus {
				animation-name: colorfade;
				animation-duration: 4s;
			}
		}

		div {
			position: relative;
			overflow: visible;

			div {
				width: 1.2rem;
				height: 1.2rem;
				position: absolute;
				display: flex;
				align-items: center;
				justify-content: center;
				top: -0.5rem;
				right: -0.3rem;
				border-radius: 50%;
				opacity: 0;
				background-color: var(--color-border);
				box-shadow: 0 0 3px black;
				transition: opacity 0.2s;
				z-index: 10;
				pointer-events: none;
				cursor: pointer;

				span {
					color: rgb(185, 185, 185);
					font-family: var(--font-icon);
					font-size: 0.8rem;
					transition: color 0.2s;
				}

				&:hover span {
					color: rgb(255, 65, 44);
				}
			}

			&:hover div {
				opacity: 1;
				pointer-events: all;
			}
		}

		input {
			height: calc(1.5rem - 4px);
			width: 1.7rem;
			margin-right: 6px;
			padding: 2px 4px;
			border-radius: 5px;
			border: none;
			background-color: rgb(30, 30, 30);
			color: var(--color-complement-text);
			font-size: 0.82rem;

			&:focus {
				width: 5.4rem;
			}
		}
	}

	&-layers {
		width: 1.75rem;
		height: 1.75rem;
		display: flex;
		align-items: center;
		justify-content: center;
		position: absolute;
		right: 10px;
		top: 108px;
		border-radius: 50%;
		background-color: white;
		z-index: 1;

		span {
			color: var(--color-component-background);
			font-size: 1.2rem;
			font-family: var(--font-icon);
		}
	}
}

#mapboxBox {
	width: 100%;
	height: calc(100% - 32px);
	border-radius: 5px;

	@media (max-width: 1000px) {
		height: 100%;
	}
}

@keyframes colorfade {
	0% {
		color: var(--color-highlight);
	}

	75% {
		color: var(--color-highlight);
	}

	100% {
		color: var(--color-complement-text);
	}
}

@keyframes spin {
	to {
		transform: rotate(360deg);
	}
}
</style>
