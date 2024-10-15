<script setup>
import { onMounted } from 'vue';
import Chart from 'chart.js/auto';

const props = defineProps({
    bar_labels: Array,
    bar_data: Array,
    bar_title: String,
})

let chart;

onMounted(async () => {
    const max = props.bar_data.reduce((i,j) => Math.max(i, j), -Infinity)
    const ctx = document.getElementById('myChart2');
    const config = {
    type: 'bar',
    data: {
            labels: props.bar_labels,
            datasets: [{
                label: props.bar_title,
                data: props.bar_data,
                borderWidth: 1,
                hoverBackgroundColor: '#42A5F5', // Blue shade for hover background
                hoverBorderColor: '#fff',
                backgroundColor: [
                    'rgba(33, 150, 243, 0.5)', // Blue shade
                ],
                borderRadius: 2
            }]
        },
    options: {
        plugins: {
            tooltip: {
                usePointStyle: true,
                callbacks: {
                    title: function(context) {
                        return "Number of Contract"
                    },                    
                    labelPointStyle: function(context) {
                        return {
                            pointStyle: 'triangle',
                            rotation: 0
                        };
                    }
                }
            }
        },
        scales: {
        y: {
          beginAtZero: true,
          type: 'linear',
          max: max + 1,
          ticks: {
            callback: function(value) {
                return Number.isInteger(value) ? value : '';
            }}
        }
      }
    }
  }
    chart = new Chart(ctx, config);
})

</script>

<template>
    <canvas class="h-full m-auto" id="myChart2"></canvas>
</template>