<template>
    <div class="w-full">
        <h1 class="text-[#908c13] font-semibold text-3xl mb-12">Contract List</h1>

        <div class="flex items-center gap-4 justify-end">
            <div v-show="filterBox==true" class="text-sm grid grid-cols-2 gap-x-8 w-2/3">
                <div class="flex items-center gap-2">
                    <label for="" class="!text-base !whitespace-nowrap">Sales Person</label>
                    <Dropdown v-model="salesPerson" showClear filter :options="salesList.data" optionLabel="username" placeholder="" id="dropdown"
                            pt:input:class="p-0 text-sm text-gray-500" pt:clearIcon:class="text-gray-500 " pt:trigger:class="text-black"
                            class="inputBox !py-2" v-on:change="filterSales"/> 

                </div>
                <div class="flex items-center gap-2">
                    <label for="" class="!text-base">Status</label>
                    <Dropdown v-model="status" showClear :options="statusList" placeholder="" id="dropdown"
                            pt:input:class="p-0 text-sm text-gray-500" pt:clearIcon:class="text-gray-500 " pt:trigger:class="text-black"
                            class="inputBox !py-2" v-on:change="filterStatus"/>
                </div>
            </div>
            <i class="pi pi-filter text-[#908c13] text-xl" v-on:click="showFilter"></i>
            <div class="flex w-1/3">
                <Dropdown v-model="searchType" :options="searchTypeList"  placeholder="Search Category" pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
                class="inputBox basis-2/5" />
                <IconField iconPosition="right" class="basis-3/5">
                    <InputIcon>
                        <i class="pi pi-search"/>
                    </InputIcon>
                    <input type="text" class="inputBox"  v-model="searchInput">
                </IconField>
                
            </div>
            
        </div>
        


        <div class="card overflow-hidden" v-if="userStore.role != 'Helpdesk'">
            <DataTable :value="testing" columnResizeMode="fit" tableStyle="min-width: 100%" removableSort paginator :rows="20" :rowsPerPageOptions="[20, 30, 35]">
                <template #empty> No contracts found... </template>
                <Column header="">
                    <template #body="slotProps">
                        <span class="w-3 h-3 self-center inline-block rounded-[50%]" 
                        :class="{
                            'bg-gray-400': slotProps.data.project_status === 'Draft', 
                            'bg-yellow-500': slotProps.data.project_status === 'Pending', 
                            'bg-green-500': slotProps.data.project_status === 'Approved',
                            'bg-red-500': slotProps.data.project_status === 'Rejected'
                            }"></span>
                    </template>
                </Column>
                <Column field="customer_name" header="Customer Name" class="text-ellipsis" sortable pt:sortIcon:class="text-white"></Column>
                <Column field="costsheet" header="Cost Sheet" class="text-ellipsis" sortable></Column>
                <Column field="sales_person" header="Sales Person" class="text-ellipsis" sortable></Column>
                <Column field="project_name" header="Project Name" class="text-ellipsis" sortable></Column>
                <Column field="product" header="Products" class="text-ellipsis" sortable></Column>
                <Column field="project_status" header="Status" class="text-ellipsis" sortable></Column>
                <Column header="">
                    <template #body="slotProps">
                        <div class="flex">
                            <router-link :to="{ path: `contracts/${slotProps.data.project_id}` }">
                                <div class="flex gap-4 justify-center cursor-pointer">
                                    <i class="pi pi-info-circle text-[#908c13]" v-tooltip.left="{ value: 'Contract Detail', showDelay: 500, hideDelay: 200 }"></i>
                                </div>
                            </router-link>
                            <!-- <div class="flex gap-4 justify-center cursor-pointer">
                                <i class="pi pi-clone text-[#908c13]"></i>
                            </div> -->
                        </div>
                        
                    </template>
                </Column>
            </DataTable>
        </div>
        <div class="card w-full" v-else>
            <DataTable :value="testing" tableStyle="min-width: 100%" removableSort >
                <template #empty> No contracts found... </template>
                <Column header="">
                    <template #body="slotProps">
                        <span class="w-3 h-3 self-center inline-block rounded-[50%]" 
                        :class="{
                            'bg-green-500': slotProps.data.status === 'Ongoing',
                            'bg-red-500': slotProps.data.status === 'Expired'
                            }"></span>
                    </template>
                </Column>
                <Column field="customer_name" header="Customer Name" sortable pt:sortIcon:class="text-white"/>
                <Column field="product_name" header="Product Name" sortable></Column>
                <Column field="project_name" header="Project Name" sortable></Column>
                <Column field="sales_person" header="Sales Person" sortable></Column>
                <Column field="status" header="Status" sortable></Column>
                <Column header="">
                    <template #body="slotProps">
                        <div class="flex">
                            <router-link :to="{ path: `contracts/${slotProps.data.project_id}` }">
                                <div class="flex gap-4 justify-center cursor-pointer">
                                    <i class="pi pi-info-circle text-[#908c13]" v-tooltip.left="{ value: 'Contract Detail', showDelay: 500, hideDelay: 200 }"></i>
                                </div>
                            </router-link>
                            <!-- <div class="flex gap-4 justify-center cursor-pointer">
                                <i class="pi pi-clone text-[#908c13]"></i>
                            </div> -->
                        </div>
                        
                    </template>
                </Column>
            </DataTable>
        </div>
    </div>
</template>

<script setup>
import Tooltip from 'primevue/tooltip';
import Dropdown from 'primevue/dropdown';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';  
import { onMounted } from 'vue';
import { ref, watch } from 'vue'
import axios from 'axios';
import { userManagement } from '../pinia';
import _ from 'lodash'
import 'primeicons/primeicons.css'
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';

const userStore = userManagement()

const searchInput = ref('')
const searchTypeList = ['Customer Name','Cost Sheet','Project Name']
const searchType = ref('Customer Name')


const salesPerson = ref()
const status = ref()

const statusList = ['Approved', 'Draft', 'Pending', 'Rejected']

let filterBox = ref(false)

const showFilter = () => {
    filterBox.value = !filterBox.value
}

const filterSales = () => {
    if(salesPerson.value == null){
        filterSalesList = contracts
        testing.value = _.cloneDeep(filterSalesList)
    }
    else{
        
        filterSalesList = contracts.filter((contract) => contract.sales_person.includes(salesPerson.value.username))
    }
    const intersection = _.intersection(searchList, filterSalesList, filterStatusList);
    testing.value = _.cloneDeep(intersection)
    
}

const filterStatus = () => {
    if(status.value == null){
        filterStatusList = contracts
        testing.value = _.cloneDeep(filterStatusList)
    }
    else{
        
        filterStatusList = contracts.filter((contract) => contract.project_status.includes(status.value))
    }
    const intersection = _.intersection(searchList, filterSalesList, filterStatusList);
    testing.value = _.cloneDeep(intersection)
}

watch(searchType, (x) => {
    searchInput.value = ''   
})
watch(searchInput, (x) => {
    
    if(searchInput.value == ''){
        searchList = contracts
        testing.value = _.cloneDeep(searchList)
    }
    else{
        
        if(searchType.value == 'Customer Name'){
            searchList = contracts.filter((contract) => contract.customer_name.toLowerCase().includes(searchInput.value.toLowerCase()))
            // testing.value = _.cloneDeep(searchList)
        }
        
        else if(searchType.value == 'Cost Sheet'){
            searchList = contracts.filter((contract) => contract.costsheet.toLowerCase().includes(searchInput.value.toLowerCase()))
        }
        else{
            searchList = contracts.filter((contract) => contract.project_name.toLowerCase().includes(searchInput.value.toLowerCase()))
        }
    }
    const intersection = _.intersection(searchList, filterSalesList, filterStatusList);
    testing.value = _.cloneDeep(intersection)
})




let testing = ref([{}])
let searchList
let filterSalesList
let filterStatusList
let contracts
let loading = true

let salesList = ref([{}])

const getSales = async() => {
    const response = await axios.get(import.meta.env.VITE_API_URL + `user`)
        .then(data => {
            salesList.value = data.data
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

const getProjectList = async() => {
    const response = await axios.get(import.meta.env.VITE_API_URL + "project", {
        headers: {
            'user': userStore.db_id
        }
    }).then(data => {
        contracts = data.data.data
        searchList = contracts
        filterSalesList = contracts
        filterStatusList = contracts
        testing.value = _.cloneDeep(contracts)
        loading = false
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}

const getProductList = async() => {
    try {
        const response = await axios.get(import.meta.env.VITE_API_URL + "product")
        contracts = response.data.data
        searchList = contracts
        filterSalesList = contracts
        filterStatusList = contracts
        testing.value = _.cloneDeep(contracts)
        loading = false
    } catch(e) {
        console.log(e);
    }
}

const getListDec = async () => {
    if (userStore.role == "Helpdesk") {
        await getProductList()
        return
    } else {
        await getProjectList()
        return
    }
}

onMounted(async () => {
    await getSales()
    await getListDec()
})



</script>

<style lang="scss" scoped>



</style>