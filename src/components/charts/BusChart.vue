<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { onMounted, ref } from "vue";
import { busNames } from "../../assets/configs/apexcharts/electricBusNames";
const props = defineProps(["chart_config", "activeChart", "series"]);

const color = ref("#c6c5c5");
const pinkColor = ref("#eea5a5");
const busIndex = ref(0);
const sortedBusNames = ref([...busNames]);
function shiftBusNames() {
	sortedBusNames.value.push(sortedBusNames.value.shift());
}
onMounted(() => {
	setInterval(() => {
		if (busIndex.value === props.series.length - 1) {
			busIndex.value = 0;
		} else {
			busIndex.value++;
		}
		shiftBusNames();
	}, 20000);
});
</script>

<template>
	<div v-if="activeChart === 'BusChart'" class="buschart">
		<TransitionGroup
			class="buschart-busNames"
			name="list"
			tag="ul"
			:style="{ flex: 3 }"
		>
			<li
				v-for="(sortedBusName, index) in sortedBusNames"
				:key="sortedBusName + '-' + index"
			>
				<div v-if="index === 0" class="buschart-busNames-0">
					{{ sortedBusName }}
				</div>
				<div v-else class="buschart-busNames-others">
					{{ sortedBusName }}
				</div>
			</li>
		</TransitionGroup>
		<div :style="{ display: 'flex', alignItems: 'center' }">
			<div>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					width="45px"
					height="45px"
					viewBox="0 0 200 200"
					version="1.1"
				>
					<g id="surface1">
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(27.058824%, 35.294118%, 39.215686%);
								fill-opacity: 1;
							"
							d="M 66.667969 150 C 66.667969 147.699219 64.800781 145.832031 62.5 145.832031 L 45.832031 145.832031 C 43.53125 145.832031 41.667969 147.699219 41.667969 150 L 41.667969 175 C 41.667969 177.300781 43.53125 179.167969 45.832031 179.167969 L 62.5 179.167969 C 64.800781 179.167969 66.667969 177.300781 66.667969 175 Z M 158.332031 150 C 158.332031 147.699219 156.46875 145.832031 154.167969 145.832031 L 137.5 145.832031 C 135.199219 145.832031 133.332031 147.699219 133.332031 150 L 133.332031 175 C 133.332031 177.300781 135.199219 179.167969 137.5 179.167969 L 154.167969 179.167969 C 156.46875 179.167969 158.332031 177.300781 158.332031 175 Z M 158.332031 150 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(100%, 75.686275%, 2.745098%);
								fill-opacity: 1;
							"
							d="M 156.25 16.667969 L 43.75 16.667969 C 37.996094 16.667969 33.332031 21.332031 33.332031 27.082031 L 33.332031 154.167969 C 33.332031 154.167969 33.332031 162.5 41.667969 162.5 L 158.332031 162.5 C 166.667969 162.5 166.667969 154.167969 166.667969 154.167969 L 166.667969 27.082031 C 166.667969 21.332031 162.003906 16.667969 156.25 16.667969 Z M 156.25 16.667969 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(100%, 75.686275%, 2.745098%);
								fill-opacity: 1;
							"
							d="M 41.667969 93.746094 C 41.667969 97.199219 38.867188 99.996094 35.417969 99.996094 L 31.25 99.996094 C 27.796875 99.996094 25 97.199219 25 93.746094 L 25 81.25 C 25 77.796875 27.796875 75 31.25 75 L 35.417969 75 C 38.867188 75 41.667969 77.796875 41.667969 81.25 Z M 175 93.746094 C 175 97.199219 172.203125 99.996094 168.75 99.996094 L 164.582031 99.996094 C 161.132812 99.996094 158.332031 97.199219 158.332031 93.746094 L 158.332031 81.25 C 158.332031 77.796875 161.132812 75 164.582031 75 L 168.75 75 C 172.203125 75 175 77.796875 175 81.25 Z M 175 93.746094 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(100%, 97.254902%, 88.235294%);
								fill-opacity: 1;
							"
							d="M 45.832031 135.417969 C 45.832031 141.167969 50.496094 145.832031 56.25 145.832031 C 62.003906 145.832031 66.667969 141.167969 66.667969 135.417969 C 66.667969 129.664062 62.003906 125 56.25 125 C 50.496094 125 45.832031 129.664062 45.832031 135.417969 Z M 45.832031 135.417969 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(100%, 97.254902%, 88.235294%);
								fill-opacity: 1;
							"
							d="M 133.332031 135.417969 C 133.332031 141.167969 137.996094 145.832031 143.75 145.832031 C 149.503906 145.832031 154.167969 141.167969 154.167969 135.417969 C 154.167969 129.664062 149.503906 125 143.75 125 C 137.996094 125 133.332031 129.664062 133.332031 135.417969 Z M 133.332031 135.417969 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(62.352941%, 65.882353%, 85.490196%);
								fill-opacity: 1;
							"
							d="M 152.082031 25 L 47.917969 25 C 44.464844 25 41.667969 27.796875 41.667969 31.25 L 41.667969 97.917969 C 41.667969 103.667969 46.332031 108.332031 52.082031 108.332031 L 147.917969 108.332031 C 153.667969 108.332031 158.332031 103.667969 158.332031 97.917969 L 158.332031 31.25 C 158.332031 27.796875 155.535156 25 152.082031 25 Z M 152.082031 25 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(14.901961%, 19.607843%, 21.960784%);
								fill-opacity: 1;
							"
							d="M 158.332031 50 L 41.667969 50 L 41.667969 31.25 C 41.667969 27.796875 44.464844 25 47.917969 25 L 152.082031 25 C 155.535156 25 158.332031 27.796875 158.332031 31.25 Z M 158.332031 50 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(39.215686%, 86.666667%, 9.019608%);
								fill-opacity: 1;
							"
							d="M 50 33.332031 L 95.832031 33.332031 L 95.832031 41.667969 L 50 41.667969 Z M 104.167969 33.332031 L 120.832031 33.332031 L 120.832031 41.667969 L 104.167969 41.667969 Z M 104.167969 33.332031 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(47.45098%, 52.54902%, 79.607843%);
								fill-opacity: 1;
							"
							d="M 87.5 108.332031 L 54.167969 108.332031 L 54.167969 77.082031 C 54.167969 73.632812 56.964844 70.832031 60.417969 70.832031 L 81.25 70.832031 C 84.703125 70.832031 87.5 73.632812 87.5 77.082031 Z M 145.832031 108.332031 L 112.5 108.332031 L 112.5 77.082031 C 112.5 73.632812 115.296875 70.832031 118.75 70.832031 L 139.582031 70.832031 C 143.035156 70.832031 145.832031 73.632812 145.832031 77.082031 Z M 145.832031 108.332031 "
						/>
						<path
							style="
								stroke: none;
								fill-rule: nonzero;
								fill: rgb(22.352941%, 28.627451%, 67.058824%);
								fill-opacity: 1;
							"
							d="M 118.457031 108.332031 C 117.351562 107.097656 116.667969 105.679688 116.667969 104.167969 C 116.667969 99.648438 122.390625 95.832031 129.167969 95.832031 C 135.941406 95.832031 141.667969 99.648438 141.667969 104.167969 C 141.667969 105.679688 140.984375 107.097656 139.875 108.332031 L 149.257812 108.332031 C 149.695312 106.996094 150 105.617188 150 104.167969 C 150 94.976562 140.652344 87.5 129.167969 87.5 C 117.679688 87.5 108.332031 94.976562 108.332031 104.167969 C 108.332031 105.617188 108.636719 106.996094 109.074219 108.332031 Z M 118.457031 108.332031 "
						/>
					</g>
				</svg>
			</div>
		</div>
		<div :style="{ flex: 4 }">
			<div class="buschart-data scroll-parent">
				<div class="scroll-element">
					<div
						v-for="(item, index) in props.series[busIndex]['data']"
						:class="`initial-animation-${index}`"
						:key="`${props.series[busIndex]['name']}-${index}`"
					>
						<div class="buschart-data-block">
							<div
								class="buschart-data-block-tag"
								:style="{
									backgroundColor:
										item['y'] !== 0 ? color : pinkColor,
									borderColor: 'black',
								}"
							>
								<div
									class="buschart-data-block-tag-outer"
									:style="{ flex: 1 }"
								>
									<div class="buschart-data-block-tag-inner">
										<div
											class="buschart-data-block-tag-inner-inner"
										></div>
									</div>
								</div>
								<div
									:style="{ flex: 3 }"
									class="buschart-data-block-tag-name"
								>
									{{ item["x"] }}
									<!-- <div class="buschart-data-block-tag-hollow"></div> -->
								</div>
								<!-- <p v-if="item['y']!==0" :style="{ color: (index === props.series[busIndex]['data'].length - 1 || index === 0) ? 'white' : 'black' }"> 
									{{ item["y"] }} min(s)
								</p>
								<p v-else :style="{ color: 'red' }"> 
									進站中 
								</p> -->
							</div>
							<div class="buschart-data-block-timeOuter">
								<div
									v-if="item['y'] === 0"
									class="buschart-data-block-time"
								>
									<h5>進站中</h5>
								</div>
								<div v-else class="buschart-data-block-time">
									<h5>{{ item["y"] }} min</h5>
								</div>
							</div>
						</div>
						<div class="buschart-data-block">
							<div
								class="buschart-data-block-line"
								:style="{
									backgroundColor:
										index ===
										props.series[busIndex]['data'].length -
											1
											? 'transparent'
											: color,
								}"
							></div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
.buschart {
	display: flex;
	flex-direction: row;
	// align-items: center;
	justify-content: space-between;
	width: 100%;
	height: 100%;

	&-busNames {
		overflow: scroll;
		// width: 25%;
		// height: 100%;
		// font-size: 1.5rem;
		font-weight: 400;
		// display: flex;
		// align-items: center;
		// margin-bottom: 0.5rem;

		&-0 {
			position: 5vh;
			font-size: 1.5rem;
			font-weight: 800;
			margin-bottom: 0.5rem;
			overflow: hidden;
		}

		&-others {
			position: 5vh;
			font-size: 1.2rem;
			font-weight: 400;
			margin-bottom: 0.5rem;
			opacity: 0.25;
			overflow: hidden;
		}
	}

	&-icon {
		position: absolute;
		top: 10%;
		left: 40%;
		width: 15%;
		// 	font-size: 1.5rem;
		// 	font-weight: 500;
		// 	// margin-bottom: 0.5rem;
	}

	&-data {
		// align-items: center;
		// justify-content: center;
		// width: 70%;

		&-block {
			display: grid;
			grid-template-columns: 8rem 15rem;

			&-icon {
				color: "red";
			}

			&-timeOuter {
				height: 2rem;
			}

			&-time {
				height: 100%;
				display: flex;
				flex-direction: row;
				align-items: center;
				justify-content: start;

				h5 {
					margin-left: 0.4rem;
					font-size: 0.7rem;
					font-weight: 500;
					pointer-events: none;
					user-select: none;
					color: #e0e0e0;
				}
			}

			&-tag {
				min-width: 2rem;
				min-height: 2rem;
				display: flex;
				flex-direction: row;
				align-items: center;
				justify-content: start;
				border-width: 2px;
				border-style: solid;
				border-top-left-radius: 1rem;
				border-bottom-left-radius: 1rem;
				background-color: white;

				&-name {
					font-size: 0.7rem;
					font-weight: 500;
					pointer-events: none;
					user-select: none;
					color: black;
					display: flex;
					flex-direction: row;
					align-items: center;
					justify-content: center;
					margin-left: 0.5rem;
				}

				&-outer {
					display: flex;
					flex-direction: row;
					align-items: center;
					justify-content: center;
					width: 1.5rem;
					height: 1.5rem;
					border-radius: 50%;
				}

				&-inner {
					width: 1.3rem;
					height: 1.3rem;
					border-radius: 50%;
					border: solid 1.5px black;
					display: flex;
					flex-direction: row;
					align-items: center;
					justify-content: center;

					&-inner {
						width: 1rem;
						height: 1rem;
						border-radius: 50%;
						border: solid 1.5px black;
						background: white;
					}
				}
			}

			&-line {
				width: 0.3rem;
				height: 1rem;
				margin: 0px 0.85rem;
				color: #c6c5c5;
			}
		}
	}
}

.scroll-parent {
	overflow: hidden;
	max-height: 100%;
}

.scroll-element {
	position: absolute;
	animation: primary 20s linear infinite;
	animation-delay: 1.5s;
	overflow: hidden;
}

.slide-leave-active,
.slide-enter-active {
	transition: all 1s ease;
}

.slide-enter-from {
	transform: translateY(-100%);
}

.slide-leave-to {
	transform: translateY(100%);
}

@keyframes primary {
	from {
		top: 0%;
	}
	to {
		top: -300%;
	}
}

@keyframes ease-in {
	0% {
		opacity: 1;
	}

	50% {
		opacity: 0;
	}

	100% {
		opacity: 1;
	}
}

@for $i from 1 through 40 {
	.initial-animation-#{$i} {
		animation-name: ease-in;
		animation-duration: 1s;
		animation-delay: 0.025s * ($i);
		animation-timing-function: linear;
		animation-fill-mode: forwards;
		opacity: 0;
	}
}
</style>
