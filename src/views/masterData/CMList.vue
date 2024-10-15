<template>
    <div class="flex flex-row justify-between px-8">
        <h1>CM</h1>
        <button v-on:click="addCM" class="bg-[#908c13] p-2 text-white flex items-center rounded-md">
            <i class="pi pi-plus pr-2"></i>
            Add New CM
        </button>
    </div>
    <div class="flex items-center gap-4 justify-end px-8">
        <div class="flex w-1/4">
            <IconField iconPosition="right" class="w-full">
                <InputIcon>
                    <i class="pi pi-search"/>
                </InputIcon>
                <input type="text" class="inputBox"  v-model="searchInput">
            </IconField>
        </div>
    </div>
    <div class="flex flex-col">
        <div class="overflow-x-auto sm:mx-0.5 lg:mx-0.5">
            <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
                <div class="overflow-hidden">
                    <table class="min-w-full">
                        <thead class="bg-[#908c13] border-b">
                            <tr>
                                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                                CM Name
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="CM in currList" :key="CM.name"
                                class="flex justify-between px-4 ">
                                <td class="text-sm text-gray-900 font-light whitespace-nowrap">{{ CM.name }}</td>
                                <button class="bg-red-600 m-2 px-2 rounded-md text-white"
                                    v-on:click="deleteCM(CM.name)">Delete</button>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    <div class="fixed inset-0 flex items-center  justify-center bg-gray-800 bg-opacity-75" v-if="showModal">
        <div class="bg-white rounded-lg p-8 max-w-md">
            <div class="flex justify-end">
                <button class="pi pi-times " v-on:click="addCM"></button>
            </div>
            <h1 class=" text-center mt-4 text-[#908c13] font-semibold text-2xl mb-4">Add CM</h1>
            <div class="py-2">
                <label class="block">CM Name<span class="text-red-600">*</span></label>
                <input type="text" class="inputBox"
                    v-model="CMName">
            </div>

            <div class="flex justify-end">
                <button class="bg-[#908c13] text-white px-2 py-1 rounded-md " v-on:click="submitCM">submit</button>
            </div>
        </div>

    </div>
    <Transition>
        <div class="fixed top-0 left-1/2 translate-x-[-50%] my-2  " v-if="showToast">
            <div class="bg-white rounded-lg p-4 min-w-48 max-w-md flex justify-center">
                invalid or empty input
            </div>
        </div>
    </Transition>
    <Toast/>
</template>

<script setup>

import { onMounted } from 'vue';
import { ref, watch } from 'vue'
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router'
import { useToast } from "primevue/usetoast";
import _ from 'lodash'
import 'primeicons/primeicons.css'
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';

const searchInput = ref('')
const currList = ref([{}])
let searchList


const toast = useToast();
const route = useRoute();
const router = useRouter();

let cmList = ref([{}])
let loading = true
const CMName = ref('')

const showModal = ref(false)
const showToast = ref(false)
const test = ref(false)

watch(searchInput, (x) => {
    
    if(searchInput.value == ''){
        searchList = cmList.value
        
        currList.value = _.cloneDeep(searchList.value)
    }
    else{
        
        searchList = cmList.value.filter((list) => list.name.toLowerCase().includes(searchInput.value.toLowerCase()))
    }
    currList.value = _.cloneDeep(searchList)
})

const addCM = () => {
    CMName.value = ''
    test.value = false
    showModal.value = !showModal.value

}

const deleteCM = async (CM_id) => {
    let text = "Are you sure you want to delete data?";
    if (confirm(text) == true) {
        try {
            const CMId = { id: CM_id }
            const response = await axios.delete(import.meta.env.VITE_API_URL + `cm_by/${CM_id}`,{
            headers: {
                "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
            }
        })

        } catch (error) {
            console.log(error)
        }
        toast.add({severity: 'success', summary: 'Success Message', detail: "Data successfully deleted!", life: 5000})
        fetchCM()
    }

}

const fetchCM = async () => {
    const response = await axios.get(import.meta.env.VITE_API_URL + "cm_by")
        .then(data => {
            cmList.value = data.data.data
        })
        .catch(error => {
            console.error('Error fetching data:', error);

        });
        searchList = cmList
        currList.value = _.cloneDeep(searchList.value)
        searchInput.value = ''
}

const submitCM = async () => {
    if (CMName.value == '') {
        toast.add({severity: 'warn', summary: 'Warn Message', detail: "Please fill all the required field!", life: 5000})
        return
    }
    const testCM = { name: CMName.value }
    try {
        const response = await axios.post(import.meta.env.VITE_API_URL + "cm_by", testCM, {
            headers: {
                "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
            }
        })
    } catch (error) {
        console.log(error)
    }
    toast.add({severity: 'success', summary: 'Success Message', detail: "Data successfully added!", life: 5000})
    showModal.value = false
    fetchCM()
}

onMounted(async () => {
    fetchCM()
})
</script>

<style scoped>
.asd {
    @apply border-red-500
}

h1 {
    @apply text-[#908c13] font-semibold text-2xl mb-4
}

table tbody tr {
    @apply bg-white
}

.v-enter-active,
.v-leave-active {
    transition: opacity 0.25s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}
</style>