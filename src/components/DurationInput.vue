<template>
    <div class="flex gap-2">
        <input type="number" class="inputBox basis-2/5" v-model="duration" @change="changeDuration" v-show="type=='Minute(s)'" min='0' max='60'></input>
        <input type="number" class="inputBox basis-2/5" v-model="duration" @change="changeDuration" v-show="type=='Hour(s)'" min='0' max='24'></input>
        <!-- <select class="inputBox basis-2/5" v-model="duration" @change="changeDuration">
            <option v-if="type=='Minute(s)'" v-for="duration in 60" :value="duration">{{ duration }}</option>
            <option v-if="type=='Hour(s)'" v-for="duration in 24" :value="duration">{{ duration }}</option>
        </select> -->
        <select class="inputBox basis-3/5" v-model="type" @change="changeDuration">
            <option v-for="test in typeList" :value="test">{{ test }}</option>
        </select>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import {ref} from 'vue'
import axios from 'axios';

const time = defineModel('time')
var duration = ref()
const type = ref('Minute(s)')

if(time.value != ''){
    const splitArr = time.value.split(' ')
    duration.value = splitArr[0]
    type.value = splitArr[1]
}



const typeList = ['Minute(s)','Hour(s)']

const changeDuration = () => {
    if(type.value == "Hour(s)" && duration.value>24){
        duration.value=undefined
    }
    if(type.value == "Minute(s)" && duration.value>60){
        duration.value=undefined
    }
    if(duration.value!=''){
        time.value = duration.value+ " " + type.value
    }
    
}

</script>

<style lang="scss" scoped>

</style>