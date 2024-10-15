<template>
    <section class="w-full">
        <!--<h1 class="text-[#908c13] font-semibold text-3xl">Welcome, <span class="underline cursor-pointer">{{userStore.name}}</span></h1> -->
        <section class="flex gap-5">
            <div class="w-full basis-[65%] flex flex-col">
                <section class="flex w-full gap-4 p-2 rounded-lg">
                    <router-link to="/contracts">
                        <div
                            class="h-36 w-72 bg-white flex flex-col z-50 p-3 shadow-sm shadow-gray-400 rounded-md select-none">
                            <div class="flex w-full">
                                <span class="w-3 h-3 self-center mr-1 bg-blue-700"></span>
                                <h4 class="text-lg font-semibold">Total Project</h4>
                                <i class="pi pi-briefcase self-center ml-auto"></i>
                            </div>
                            <div class="flex mb-0 w-full h-full" >
                                <p class="text-4xl mt-3 self-center font-bold">{{ totalProject }}</p>
                                <p class="text-md mt-3 self-end ml-auto bg-white font-semibold p-1 rounded-sm" :class="{'text-green-600': totalProjectDiff > 0, 'text-red-600': totalProjectDiff < 0}" v-tooltip.left="{ value: 'Project Monthly Diff', showDelay: 500, hideDelay: 200 }">
                                    <span v-if="totalProjectDiff > 0"> <i class="pi pi-wave-pulse"></i> + </span>
                                    <span v-else-if="totalProjectDiff == 0"> <i class="pi pi-wave-pulse"></i>  </span>                                    
                                    <span v-else> <i class="pi pi-wave-pulse"></i>  </span>
                                    {{ totalProjectDiff }}
                                </p>
                            </div>
                        </div>
                    </router-link>
                    <router-link to="/contracts">
                        <div
                            class="h-36 w-72 flex flex-col z-50 p-3 shadow-sm shadow-gray-400 bg-white rounded-md hover:bg-lime-500 hover:text-white cursor-pointer transition-all duration-300 select-none">
                            <div class="flex w-full">
                                <span class="w-3 h-3 self-center mr-1 bg-blue-700"></span>
                                <h4 class="text-lg font-semibold"> Pending Project</h4>
                                <i class="pi pi-users self-center ml-auto"></i>
                            </div>
                            <div class="flex mb-0 w-full h-full">
                                <p class="text-4xl mt-3 self-center font-bold">{{ pendingProject }}</p>
                                
                            </div>
                        </div>
                    </router-link>


                    <router-link to="">
                        <div
                            class="h-36 w-72 flex flex-col z-50 p-3 shadow-sm shadow-gray-400 bg-white rounded-md hover:bg-lime-500 hover:text-white cursor-pointer transition-all duration-300 select-none">
                            <div class="flex w-full">
                                <span class="w-3 h-3 self-center mr-1 bg-blue-700"></span>
                                <h4 class="text-lg font-semibold">
                                    <span v-if="userStore.role == 'Sales'">Total Project Handle</span>
                                    <span v-else>Total Customer</span>
                                </h4>
                                <i class="pi pi-clock self-center ml-auto"></i>
                            </div>
                            <div class="flex mb-0 w-full h-full">
                                <p class="text-4xl mt-3 self-center font-bold">
                                    <span v-if="userStore.role == 'Sales'">{{ userTotalProject }}</span>
                                    <span v-else>{{ totalCustomer }}</span>
                                </p>
                                
                            </div>
                        </div>
                    </router-link>
                </section>
                <section class="w-full">
                    <div class="flex gap-2" v-if="label1 && data1">
                        <div class="self-center m-auto flex-1 h-[350px]">
                            <BarChart :bar_labels="label1" :bar_data="data1" bar_title="Top 5 Customer by Contract"></BarChart>
                        </div>
                    </div>
                    <div class="animate-pulse p-1 flex gap-2" v-else="label1 && data1">
                        <div class="self-center flex-1">
                            <div class="w-2/3 h-60 m-auto bg-slate-400 rounded-lg p-2">
                                <p class="hidden">Loading Data</p>
                            </div>
                        </div>
                    </div>
                </section>

            </div>
            <div class="h-full w-full mt-3">
                <section class="flex flex-col justify-between">
                    <router-link :to="{ path: `user/${userStore.db_id}` }">
                        <div class="rounded-lg shadow-lg bg-slate-800 flex flex-col">
                            <section class="flex flex-col p-5">
                                <img src="../assets/avatar.png"
                                    class="w-16 h-16 select-none rounded-full m-auto bg-white p-[2px]" alt="avatar">
                                <div class="text-center text-white mt-2">
                                    <h4 class="tracking-wider text-lg font-semibold">{{userStore.name}}</h4>
                                    <p class="text-sm text-gray-300">{{userStore.role}}<span><i
                                                class="pi pi-building ml-1"></i>Infracom Technology</span> </p>
                                </div>
                            </section>
                            <section class="flex justify-evenly bg-white  font-semibold">
                                <div class="flex flex-col p-2 ">
                                    <h4>
                                        <span v-if="userStore.role == 'Sales'">Assigned to you</span>
                                        <span v-else>Contract Created</span>
                                    </h4>
                                    <p class="text-center">{{ totalProjectbyUser }}</p>
                                </div>
                            </section>
                        </div>
                    </router-link>
                    <div class="rounded-lg mt-3" v-if="tempData">
                        <h4 class="py-2 text-lg text-[#908c13] font-semibold">Latest Contracts</h4>
                        <TableOnClick :data="data" :row_data="tempData" />
                    </div>
                </section>
            </div>
        </section>
    </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios';
import BarChart from '../components/BarChart.vue';
import BarChart2 from '../components/BarChart2.vue';
import TableOnClick from '../components/TableOnClick.vue';
import Avatar from '../assets/customer.png';
import { userManagement } from '../pinia';

const userStore = userManagement()
const pendingProject = ref(0)
const totalProject = ref(0)
const totalProjectbyUser = ref(0)
const totalCustomer = ref(0)
const userTotalProject = ref(0)
const totalProjectDiff = ref(0)

// Chart 1 Data
const label1 = ref()
const data1 = ref()

// Chart 2 Data
const label2 = ref()
const data2 = ref()


const tempData = ref()
const loggedUser = ref()
const userName = ref('')
const data = ["Project", "Customer", "Details"]

onMounted(async () => {
    await Promise.all([
        getTopCustomer(),
        getTotalCustomer(),
        getTotalProject(),
        getpendingProject(),
        getProjectByUser(),
        getTotalCreatedContract(),
        getUserProjectHandle(),
    ]);
});

const getpendingProject = async () => {
    let response = await axios.get(import.meta.env.VITE_API_URL+'dashboard/pending-project', {
        headers: {
            'user': `${userStore.db_id}`
        }
    })
    pendingProject.value = response.data.data
}

const getUserProjectHandle = async () => {
    try {
        const response = await axios.get(import.meta.env.VITE_API_URL+`user-dashboard/project`, {
            headers: {
                'user': `${userStore.db_id}`
            }
        })
        let temp_data = response.data.data
        userTotalProject.value = response.data.total
    } catch(e) {
        console.error(e)
    }
}

const getTotalCustomer = async () => {
    let response = await axios.get(import.meta.env.VITE_API_URL+'dashboard/customer')
    totalCustomer.value = response.data.data
}

const getTotalProject = async () => {
    let response = await axios.get(import.meta.env.VITE_API_URL+'dashboard/project', {
        headers: {
            'user': `${userStore.db_id}`
        }
    })
    totalProject.value = response.data.data
}

const getTopCustomer = async () => {
    let response = await axios.get(import.meta.env.VITE_API_URL+"dashboard/top-customers")
    label1.value = response.data.data.labels
    data1.value = response.data.data.totals
}

const getTotalCreatedContract = async () => {
    try {
        const response = await axios.get(import.meta.env.VITE_API_URL+'dashboard/total-created', {
            headers: {
                'user': `${userStore.db_id}`
            }
        })
        totalProjectbyUser.value = response.data.data
    } catch (e) {
        console.error('Error fetching data:', error);
    }
}

const getProjectByUser = async () => {
    try {        
        const response = await axios.get(import.meta.env.VITE_API_URL+`dashboard/created-by/${userStore.db_id}`)
        if (response.data.data.length > 0) {
            tempData.value = response.data.data.map((contract) => Object.values(contract));
        }
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}
</script>