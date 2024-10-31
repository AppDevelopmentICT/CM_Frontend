<template>
  <div v-if="$route.fullPath == '/login'">
    <Login/>
  </div>
  <section v-else class="bg-slate-50 w-full h-screen overflow-auto" :class="{'overflow-hidden': isHome}">
    
    
    <div class="flex">
        <SideBar/>
        <div class="p-5 ml-[16rem] w-full h-full min-h-screen">
          <div class="flex items-center">
            <div class="flex items-center hover:text-[#908c13]" v-for="(d,index) in dir" v-on:click="redirect(index)">
              <button class="p-1 px-2 bg-[#908c13] text-white rounded-md hover:bg-[#c1bd60] transition-all">
                <span v-if="d === ''">Home</span>
                <span v-else>{{ displayText(d) }}</span>
              </button>
              
              <i v-show="index!=dir.length-1" class="pi pi-chevron-right text-base px-1 text-[#908c13]"></i>
            </div>
          </div>
          
          <main class="mt-2">
            <RouterView />
          </main>
      </div>
    </div>
    
  </section>
  
</template>

<script setup>
// @ts-ignore
import { ref } from 'vue';
import BarChart from './components/BarChart.vue';
import SideBar from './components/SideBar.vue'
import 'primeicons/primeicons.css'
import Login from './views/Login.vue'
import { onMounted, onUpdated, watch } from 'vue';
import { useRoute, useRouter  } from 'vue-router'

const route = useRoute();
const router = useRouter();
const isHome = ref(false)


const dir = ref([])
import { defineProps } from 'vue';

const props = defineProps({
  d: {
    type: String,
    required: true
  }
});

const displayText = (text) => {
  return text.length > 30 ? 'id' : text;
};
watch(route, async()=>{
    if(route.path=='/'){
      dir.value = ['Home']
      isHome.value = true
    }
    else{
      dir.value = route.path.split('/')
      isHome.value = false
    }
       
    
})

onMounted(() => {

})

const redirect = (index) => {
  var address = ''
  for(let i=0; i<=index; i++){
    if(dir.value[i]=='' || dir.value[i]=='Home'){
      
    }
    else{
      address += '/'+dir.value[i] 
    }
  }
  if(address==''){
    address='/'
  }
  router.push(address)
}


</script>

<style lang="scss" scoped>

</style>