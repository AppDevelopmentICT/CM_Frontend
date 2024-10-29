<template>
    <div class="flex gap-2">
        <input type="number" class="inputBox w-full basis-2/5" min="0" v-model="num" @change="changeQuantity"></input>
        <Dropdown v-model="type" :options="typeList" placeholder="" id="dropdown"  @change="changeQuantity"
        pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
        class="inputBox"/>   
    </div>
</template>

<script setup>
import { onMounted, watch } from 'vue';
import {ref} from 'vue'
import axios from 'axios';
import Dropdown from 'primevue/dropdown';

const quantity = defineModel('quantity')
var num = ref('')
const type = ref('')


const seperateArr = async () => {
    if(quantity.value!=''){
        var splitarr = quantity.value.split(/ (.*)/s)
        num.value = splitarr[0]
        type.value = splitarr[1]
    }
};

onMounted(() => {
    seperateArr()
})

const typeList = ['Ticket','Man Days']

const changeQuantity = () => {
    if(num.value!=''){
        quantity.value = num.value+ " " + type.value
    }
}

watch(quantity, (x)=> {
    var splitarr = x.split(/ (.*)/s)
    num.value = splitarr[0]
    type.value = splitarr[1]
})

</script>

<style lang="scss" scoped>

</style>