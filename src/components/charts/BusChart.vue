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
		<TransitionGroup class="buschart-busNames" name="list" tag="ul" :style="{flex: 3}">
			<li v-for="(sortedBusName, index) in sortedBusNames" 
			:key="sortedBusName+'-'+index">
				<div v-if="index===0" class="buschart-busNames-0">
					{{sortedBusName}}
				</div>
				<div v-else class="buschart-busNames-others">
					{{sortedBusName}}
				</div>
			</li>
		</TransitionGroup>
		<div :style="{display: 'flex', alignItems: 'center'}">
			<div>
				<svg width="45px" height="45px" viewBox="0 0 1024 1024" class="icon"  version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M341.333333 768a21.333333 21.333333 0 0 0-21.333333-21.333333h-85.333333a21.333333 21.333333 0 0 0-21.333334 21.333333v128a21.333333 21.333333 0 0 0 21.333334 21.333333h85.333333a21.333333 21.333333 0 0 0 21.333333-21.333333v-128zM810.666667 768a21.333333 21.333333 0 0 0-21.333334-21.333333h-85.333333a21.333333 21.333333 0 0 0-21.333333 21.333333v128a21.333333 21.333333 0 0 0 21.333333 21.333333h85.333333a21.333333 21.333333 0 0 0 21.333334-21.333333v-128z" fill="#455A64" /><path d="M800 85.333333h-576A53.333333 53.333333 0 0 0 170.666667 138.666667V789.333333s0 42.666667 42.666666 42.666667h597.333334c42.666667 0 42.666667-42.666667 42.666666-42.666667V138.666667A53.333333 53.333333 0 0 0 800 85.333333z" fill="#FFC107" /><path d="M213.333333 479.978667a32 32 0 0 1-32 32h-21.333333a32 32 0 0 1-32-32V416A32 32 0 0 1 160 384h21.333333a32 32 0 0 1 32 32v63.978667zM896 479.978667a32 32 0 0 1-32 32h-21.333333a32 32 0 0 1-32-32V416a32 32 0 0 1 32-32h21.333333a32 32 0 0 1 32 32v63.978667z" fill="#FFC107" /><path d="M288 693.333333m-53.333333 0a53.333333 53.333333 0 1 0 106.666666 0 53.333333 53.333333 0 1 0-106.666666 0Z" fill="#FFF8E1" /><path d="M736 693.333333m-53.333333 0a53.333333 53.333333 0 1 0 106.666666 0 53.333333 53.333333 0 1 0-106.666666 0Z" fill="#FFF8E1" /><path d="M778.666667 128h-533.333334A32 32 0 0 0 213.333333 160v341.333333a53.333333 53.333333 0 0 0 53.333334 53.333334h490.666666a53.333333 53.333333 0 0 0 53.333334-53.333334v-341.333333A32 32 0 0 0 778.666667 128z" fill="#9FA8DA" /><path d="M810.666667 256H213.333333V160A32 32 0 0 1 245.333333 128h533.333334A32 32 0 0 1 810.666667 160V256z" fill="#263238" /><path d="M256 170.666667h234.666667v42.666666H256zM533.333333 170.666667h85.333334v42.666666h-85.333334z" fill="#64DD17" /><path d="M448 554.666667h-170.666667v-160a32 32 0 0 1 32-32h106.666667a32 32 0 0 1 32 32V554.666667zM746.666667 554.666667h-170.666667v-160a32 32 0 0 1 32-32h106.666667a32 32 0 0 1 32 32V554.666667z" fill="#7986CB" /><path d="M606.506667 554.666667c-5.674667-6.336-9.173333-13.589333-9.173334-21.333334 0-23.125333 29.312-42.666667 64-42.666666s64 19.541333 64 42.666666c0 7.744-3.498667 14.997333-9.173333 21.333334h48.042667c2.24-6.848 3.797333-13.909333 3.797333-21.333334 0-47.061333-47.850667-85.333333-106.666667-85.333333s-106.666667 38.272-106.666666 85.333333c0 7.424 1.557333 14.485333 3.797333 21.333334h48.042667z" fill="#3949AB" /></svg>
			</div>
		</div>
		<div :style="{flex: 4}">
			<div class="buschart-data scroll-parent">
				<div class="scroll-element ">
					<div
						v-for="(item, index) in props.series[busIndex]['data']"
						:class="`initial-animation-${index}`"
						:key="`${props.series[busIndex]['name']}-${index}`"
					>
						<div class="buschart-data-block">
							<div
								class="buschart-data-block-tag"
								:style="{
									backgroundColor: (item['y']!==0) ? color : pinkColor ,
									borderColor: 'black'
								}"
							>	
								<div class="buschart-data-block-tag-outer" :style="{flex: 1}">
									<div class="buschart-data-block-tag-inner">
										<div class="buschart-data-block-tag-inner-inner"></div>
									</div>
								</div>
								<div :style="{flex: 3}" class="buschart-data-block-tag-name">
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
								<div v-if="item['y']===0" class="buschart-data-block-time">
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
										props.series[busIndex]['data'].length - 1
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
				color: "red"
			}

			&-timeOuter {
				height: 2rem;
			}
			
			&-time {
				height: 100%;
				display:flex;
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
				min-width: 2.0rem;
				min-height: 2.0rem;
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
						width: 1.0rem;
						height: 1.0rem;
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


.slide-enter-from
{
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
