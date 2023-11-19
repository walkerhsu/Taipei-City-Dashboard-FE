<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { ref, computed, onMounted } from "vue";
import { useMapStore } from "../../store/mapStore";

const props = defineProps([
	"chart_config",
	"activeChart",
	"series",
	"map_config",
]);

const mapStore = useMapStore();

const height = () => {
	let max = -Infinity;

	props.series[0].data.forEach((strNumber) => {
		const tmp = parseInt(strNumber);
		if (!isNaN(tmp)) {
			max = Math.max(max, tmp);
		}
	});

	return max;
};

const width = () => {
	return props.series[0].data.length;
};

let hexagons = [];

const createHexagonalGrid = (height, width) => {
	//logic to locate hexagonal shape's center
	const sqrt3 = Math.sqrt(3);
	const radius = 4 / sqrt3; // 4 years for each horizontal center

	const hexHeight = 2 * radius;
	const hexWidth = sqrt3 * radius;
	const horizSpacing = sqrt3 * radius;
	const vertSpacing = (3 / 2) * radius;

	// console.log(hexHeight, hexWidth, height, width)

	for (let y = 0; y + hexHeight / 2 < height; y += vertSpacing) {
		let xOffset = (y / hexHeight) % 2 == 0 ? 0 : radius * (3 / 4);
		for (let x = 0; x + hexWidth / 2 < width; x += horizSpacing) {
			hexagons.push({ x: x + xOffset, y: y });
		}
	}
	return hexagons;
};

const distance = (x1, x2, y1, y2) => {
	return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
};

const findHexagonForPoint = (point, hexagons) => {
	let minDistance = Infinity;
	let closestHexagon = null;

	for (let hexagon of hexagons) {
		let pointCenterDistance = distance(
			point.x,
			hexagon.x,
			point.y,
			hexagon.y
		);

		// console.log(pointCenterDistance)
		if (pointCenterDistance <= minDistance) {
			minDistance = pointCenterDistance;
			closestHexagon = hexagon;
		}
	}

	// console.log(closestHexagon)
	return closestHexagon;
};

const hexagonDataSums = (points) => {
	let hexagonDataSums = {};
	let tmp = null;
	let cnt = null;
	for (let point of points) {
		tmp = findHexagonForPoint(point, hexagons);
		let hexagonKey = `x${tmp.x}y${tmp.y}`;
		// console.log(tmp)

		if (!hexagonDataSums[hexagonKey]) {
			hexagonDataSums[hexagonKey] = { x: tmp.x, y: tmp.y, count: 1 };
		} else {
			hexagonDataSums[hexagonKey].count++;
		}
	}

	// console.log(hexagonDataSums)

	return hexagonDataSums;
};

// const storeHexagonForPoint  = ()

// const summation()

const chartHeight = computed(() => {
	// return `${40 + props.series[0].data.length * 10}`;
	return 450;
});

// export default {
// 	const calculateHexagonPoints = (hexagons)=>{

// 	},

// }

const addHexagonSVGs = (chartContext) => {
	const svgNS = "http://www.w3.org/2000/svg";

	hexagons.forEach((hexagon) => {
		let newIcon = document.createElementNS(svgNS, "svg");
		newIcon.setAttributeNS(null, "width", 200); // Adjust size as needed
		newIcon.setAttributeNS(null, "height", 200); // Adjust size as needed

		let polygon = document.createElementNS(svgNS, "polygon");
		polygon.setAttributeNS(
			null,
			"points",
			"53.21,0 79.81,15.36 106.42,30.72 106.42,61.44 106.42,92.16 79.81,107.52 53.21,122.88 26.6,107.52 0,92.16 0,61.44 0,30.72 26.6,15.36 53.21,0"
		);
		newIcon.appendChild(polygon);

		// Use the calculated x and y values from the hexagon array
		let xPos = hexagon.x;
		let yPos = hexagon.y;

		newIcon.style.position = "absolute";
		newIcon.style.left = `${xPos}px`;
		newIcon.style.top = `${yPos}px`;

		chartContext.el.appendChild(newIcon);
	});
};

// chartOptions.value.chart.events.mounted = (chartContext, config) => {
//   addSvgToChart(chartContext, config);
// };

const chartOptions = ref({
	chart: {
		type: "scatter",
		events: {
			mounted: (chartContext) => {
				addHexagonSVGs(chartContext);
			},
			updated: (chartContext) => {
				addHexagonSVGs(chartContext);
			},
		},
		toolbar: {
			show: true,
			offsetX: 0,
			offsetY: 0,
			tools: {
				download: true,
				selection: true,
				zoom: true,
			},
		},
		export: {
			csv: {
				filename: undefined,
				columnDelimiter: ",",
				headerCategory: "category",
				headerValue: "value",
				dateFormatter(timestamp) {
					return new Date(timestamp).toDateString();
				},
			},
			svg: {
				filename: undefined,
			},
			png: {
				filename: undefined,
			},
		},
		autoSelected: "zoom",
	},

	// autoSelected: 'zoom'

	xaxis: {
		categories: props.chart_config.xaxis,
	},

	yaxis: {},
	tooltip: {
		theme: "dark", // Or 'light', depending on your preference
		style: {
			fontSize: "12px",
			fontFamily: "Helvetica, Arial, sans-serif",
			colors: ["#FFF"], // This sets the font color
		},
	},
	markers: {
		size: props.chart_config.size,
		// colors: ["#FFD700"], // Bright color for data points
		strokeColors: "#333", // Border color of the data poicalts
		strokeWidth: 2, // Border width of the data points
	},
});

onMounted(() => {
	let maxwidth = width();
	let maxheight = height();
	// console.log(maxheight)
	createHexagonalGrid(maxheight, maxwidth);
	// console.log(hexagons);

	let points = [];
	for (let i = 1; i < props.series.length - 1; ++i) {
		for (let y of props.series[i].data) {
			// point_x corresponding to index number, point_ y with scaling with proportion with x: {x.length* y/max.y}
			points.push({
				x: parseInt(i),
				y: (parseInt(y) * maxwidth) / 4 / maxheight,
			});
		}
	}
	// console.log(props.series)
	// console.log(points)

	hexagonDataSums(points);

	chartOptions.value.chart.events.mounted = (chartContext, config) => {
		addHexagonSVGs(chartContext);
	};
});
</script>

<template>
	<div v-if="activeChart === 'HexagonalBinning'">
		<!-- <div>
			<svg width="200" height="200"  >
				<polygon points="53.21,0 79.81,15.36 106.42,30.72 106.42,61.44 106.42,92.16 79.81,107.52 53.21,122.88 26.6,107.52 0,92.16 0,61.44 0,30.72 26.6,15.36 53.21,0"/>
			</svg>	
		</div> -->
		<apexchart
			width="100%"
			:height="chartHeight"
			type="scatter"
			:options="chartOptions"
			:series="series"
		>
		</apexchart>
	</div>

	<!-- 
			<svg width="200" height="200">
            <polygon :v-for="hexagon in hexagons" 
                     :points="calculateHexagonPoints(hexagon)"
                     stroke="black" fill="none" />
        </svg>
	</div> -->
</template>
