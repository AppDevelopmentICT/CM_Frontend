<template>
    <div>
        <h2>Implementation</h2>
        <div class="pb-2" v-if="implementation.implementation_type == undefined || implementation.implementation_type == 'None' || implementation.implementation_type == '' ">
            <label for="" class="block">Implementation By<span class="text-red-600">*</span></label>
            <Dropdown v-model="impleObj" :options="ImpleList.data" optionLabel="implementation_type" placeholder="" id="dropdown"
            pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
            class="inputBox"/>   
        </div>
        <div v-else class="flex flex-col">
            <div class="w-full">
                <label for="" class="block">Implementation By<span class="text-red-600">*</span></label>
                <Dropdown v-model="impleObj" :options="ImpleList.data" optionLabel="implementation_type" placeholder="" id="dropdown"
                pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
                class="inputBox"/>   
            </div>
            <div class="w-full">
                    <label for="" class="block">Start Date<span class="text-red-600">*</span></label>
                    <input type="date" class="inputBox"
                        v-model="implementation.start_date">
            </div>
            <div class="w-full pb-2">
                <label for="" class="block">End Date<span class="text-red-600">*</span></label>
                <input type="date" class="inputBox"
                    v-model="implementation.end_date">
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, watch } from 'vue';
import {ref} from 'vue'
import axios from 'axios';
import Dropdown from 'primevue/dropdown';

const implementation = defineModel('implementation')
const impleObj = ref({})
const ImpleList = ref([{}])
let initList = []
// const ImplementationList = ['None', 'By PMO', 'Without PMO']
const periodList = ['Monthly', 'Bimonthly', 'Quarterly', 'Semesterly', 'Yearly']


onMounted(async() => {
    const response = await axios.get(import.meta.env.VITE_API_URL + `implementation_by`)
        .then(data => {
            initList = data.data.data
            ImpleList.value.data = initList
            impleObj.value = ImpleList.value.data.find(({implementation_type}) => implementation_type === implementation.value.implementation_type)
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
    
})

watch(impleObj, async () => {
    if(impleObj.value!=undefined){
        implementation.value.implementation_type = impleObj.value.implementation_type
    }
    
})

</script>

<style lang="scss" scoped>

</style>