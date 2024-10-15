<template>
    <div class="flex flex-row justify-between px-8">
        <h1>Implementation</h1>
        <button v-on:click="addImplementation" class="bg-[#908c13] p-2 text-white flex items-center rounded-md">
            <i class="pi pi-plus pr-2"></i>
            Add New Implementation
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
                                Implementation By
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="Implementation in currList" :key="Implementation.implementation_type"
                                class="flex justify-between px-4 ">
                                <td class="text-sm text-gray-900 font-light whitespace-nowrap">{{ Implementation.implementation_type }}</td>
                                <button class="bg-red-600 m-2 px-2 rounded-md text-white"
                                    v-on:click="deleteImplementation(Implementation.implementation_type)">Delete</button>
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
                <button class="pi pi-times " v-on:click="addImplementation"></button>
            </div>
            <h1 class=" text-center mt-4 text-[#908c13] font-semibold text-2xl mb-4">Add Implementation By</h1>
            <div class="py-2">
                <label class="block">Implementation By<span class="text-red-600">*</span></label>
                <input type="text" class="inputBox"
                    v-model="ImplementationBy">
            </div>

            <div class="flex justify-end">
                <button class="bg-[#908c13] text-white px-2 py-1 rounded-md " v-on:click="submitImplementation">submit</button>
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

let implementationList = ref([{}])
let loading = true
const ImplementationBy = ref('')

const showModal = ref(false)
const showToast = ref(false)
const test = ref(false)

watch(searchInput, (x) => {
    
    if(searchInput.value == ''){
        searchList = implementationList.value
        
        currList.value = _.cloneDeep(searchList.value)
    }
    else{
        
        searchList = implementationList.value.filter((list) => list.name.toLowerCase().includes(searchInput.value.toLowerCase()))
    }
    currList.value = _.cloneDeep(searchList)
})

const addImplementation = () => {
    ImplementationBy.value = ''
    test.value = false
    showModal.value = !showModal.value

}

const deleteImplementation = async (Implementation_id) => {
    let text = "Are you sure you want to delete data?";
    if (confirm(text) == true) {
        try {
            const response = await axios.delete(import.meta.env.VITE_API_URL + `implementation_by/${Implementation_id}`,{
            headers: {
                "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
            }
        })

        } catch (error) {
            console.log(error)
        }
        toast.add({severity: 'success', summary: 'Success Message', detail: "Data successfully deleted!", life: 5000})
        fetchImplementation()
    }

}

const fetchImplementation = async () => {
    const response = await axios.get(import.meta.env.VITE_API_URL + "implementation_by")
        .then(data => {
            implementationList.value = data.data.data
        })
        .catch(error => {
            console.error('Error fetching data:', error);

        });
        searchList = implementationList
        currList.value = _.cloneDeep(searchList.value)
        searchInput.value = ''
}

const submitImplementation = async () => {
    if (ImplementationBy.value == '') {
        toast.add({severity: 'warn', summary: 'Warn Message', detail: "Please fill all the required field!", life: 5000})
        return
    }
    const testImplementation = { implementation_by: ImplementationBy.value }
    try {
        const response = await axios.post(import.meta.env.VITE_API_URL + "implementation_by", testImplementation, {
            headers: {
                "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
            }
        })
    } catch (error) {
        console.log(error)
    }
    toast.add({severity: 'success', summary: 'Success Message', detail: "Data successfully added!", life: 5000})
    showModal.value = false
    fetchImplementation()
}

onMounted(async () => {
    fetchImplementation()
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