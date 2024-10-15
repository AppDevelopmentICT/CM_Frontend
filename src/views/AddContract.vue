<template>
    <div class="">
        <div class="group">
            <h1 class="">Add Contract</h1>
            <div class="grid grid-cols-2 gap-x-4 gap-y-4 ">
                <div class="subgroup">
                    <h2>Contract Information</h2>
                    <div class="pb-2">
                        <label for="" class="block">Customer Name<span class="text-red-600">*</span></label>
                        <Dropdown v-model="project.customer" editable filter :options="customerList.data" optionLabel="customer_name" placeholder="" id="dropdown"
                        pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
                        class="inputBox" v-on:blur="addCustomer"/>   
                    </div>
                    <div class="pb-2">
                        <label for="" class="block">Sales Person<span class="text-red-600">*</span></label>
                        <Dropdown v-model="project.sales" filter :options="salesList.data" optionLabel="username" placeholder="" id="dropdown"
                        pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
                        class="inputBox"/>   
                    </div>
                    <div class="">
                        <label for="" class="block">Cost Sheet<span class="text-red-600">*</span></label>
                        <input type="text" class="inputBox" v-model="project.costSheet">
                    </div>

                    <div class="">
                        <label for="" class="block">Project Name<span class="text-red-600">*</span></label>
                        <input type="text" class="inputBox" v-model="project.projectName">
                    </div>
                </div>
                <div>
                    <div class="subgroup">
                        <h2>Contract Description</h2>
                        <div class="grid grid-cols-2 gap-x-6 ">
                            <div class="">
                                <label for="" class="block">Type<span class="text-red-600">*</span></label>
                                <Dropdown v-model="project.contractType" :options="contractTypeList" placeholder="" id="dropdown"
                                pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
                                class="inputBox"/> 
                                

                            </div>

                            <div class="">
                                <label for="" class="block">PO/Contract Number<span
                                        class="text-red-600">*</span></label>
                                <input type="text" class="inputBox" v-model="project.contractNumber">
                            </div>
                            <div>
                                <label for="onSiteEngineer">Managed Service<span class="text-red-600"></span></label> <br/>
                                <input id="onSiteEngineer" type="checkbox" v-model="project.onSiteEngineer">
                            </div>
                            <!-- <div v-for="file in finalFileList" :key="file" >{{file.name}}</div> -->
                        </div>
                    </div>
                    <div class="subgroup">
                        <h2>Cost Information</h2>
                        <div class="">
                            <label for="" class="block">Amount Reserve for Internal Cost<span class="text-red-600">*</span></label>
                            <div class="flex">
                                <span class="bg-gray-400 text-gray-200 p-2 my-2">Rp.</span>
                                <InputNumber class="w-full p-0 self-center focus:outline-none rounded-none" v-model="project.internalCost" inputId="integeronly" />
                            </div>
                        </div>
                        <div class="">
                            <label for="" class="block">Selling Price<span class="text-red-600">*</span></label>
                            <div class="flex">
                                <span class="bg-gray-400 text-gray-200 rounded-sm p-2 my-2">Rp.</span>
                                <InputNumber class="w-full p-0 self-center focus:outline-none rounded-none" v-model="project.sellingPrice" inputId="integeronly" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex w-full gap-4">
                <div class="subgroup w-full h-fit">
                    <PM v-model:pm="pm"/>
                </div>
                <div class="subgroup w-full h-fit">
                    <CM v-model:cm="cm"/>
                </div>
            </div>
            <div class="flex gap-4">
                <div class="subgroup w-1/3 h-fit">
                    <implementation v-model:implementation="implementation"/>
                </div>
                <div class="subgroup w-full">
                    <SLA v-model:sla="sla"/>
                </div>
            </div>
            <div class="subgroup">
                <h2>Additional Information</h2>
                <div class="grid grid-cols-2 gap-x-4">
                    <div class="">
                        <label for="" class="block">Description</label>
                        <textarea name="" id=""
                            class="inputBox min-h-24"
                            v-model="project.contractDescription"></textarea>
                    </div>

                    <div class="">
                        <label for="" class="block">Attachment File</label>
                        <div class="fileUpload" @dragenter.prevent="toggleActive" @dragleave.prevent="toggleActive"
                            @dragover.prevent @drop.prevent="drop" :class="{ 'active-dropzone': active }">
                            <label for="upload" class="">
                                <p
                                    class="text-lg font-normal bg-[#bbbbbb2d] p-4 rounded-lg  hover:bg-[#908c13] hover:text-white transition ease-in-out duration-200">
                                    Add New File (Max 5 files)</p>

                            </label>
                            <input type="file" id="upload" class="testFile" multiple v-on:change="uploadFile"
                                accept=".doc,.docx,.pdf,.pptx,.xlsx,.jpg,.jpeg,.png">
                            <div id="fileList"
                                class="flex flex-col items-center justify-center w-full min-h-16  text-gray-500 rounded-xl"
                                v-show="finalFileList.length != 0">
                                <pre class="output">Selected files:</pre>
                                <ul>
                                    <li v-for="test in finalFileList" class="text-base font-normal pb-2 pl-4"
                                        :key="test.name">
                                        <div @click.stop="" class="flex flex-row">
                                            <p class="text-wrap break-words break-all basis-5/6">{{ test.name }}</p>
                                            <div class="basis-1/6 content-center">
                                                <button class="rounded-md bg-red-600 text-white px-2 mx-4 "
                                                    @click.self="deleteFile(test)">delete</button>
                                            </div>

                                        </div>

                                    </li>
                                </ul>
                            </div>
                            <p class="text-[10px]">drag and drop files here...</p>

                        </div>
                    </div>
                </div>

            </div>
            <div class="flex justify-end gap-2">
                <button class="bg-[#908c13] p-2 w-32 text-white rounded-md"
                    v-on:click="submitContract('Draft')">Save Draft</button>
                <button class="bg-green-500 p-2 w-32 text-white rounded-md"
                    v-on:click="submitContract('Pending')">Submit</button>
            </div>
        </div>
        <Toast/>
        <div class="fixed inset-0 flex flex-col items-center justify-center bg-gray-500 bg-opacity-30" v-if="loading">
            <ProgressSpinner class="w-[200px] h-[200px]"/>
            <p class="!text-[#908c13] !text-3xl !font-bold">Loading</p>
        </div>
    </div>
</template>

<script setup>
import ProgressSpinner from 'primevue/progressspinner';
import Dropdown from 'primevue/dropdown';
import InputNumber from 'primevue/inputnumber';
import { onMounted } from 'vue';
import { ref } from 'vue'
import axios from 'axios';
import PM from '../components/PreventiveMaintenance.vue'
import CM from '../components/CorrectiveMaintenance.vue'
import SLA from '../components/SLA.vue'
import Implementation from '../components/Implementation.vue'
import { useRoute, useRouter } from 'vue-router'
import { userManagement } from '../pinia';
import PocketBase from 'pocketbase';
import { useToast } from "primevue/usetoast";

const toast = useToast();
const pb = new PocketBase(import.meta.env.VITE_PB_BASEURL);
const route = useRoute();
const router = useRouter();
const userStore = userManagement()

var valid = false
var output = ""
var dupe = false
var fileUpload = []
var finalFileList = ref([])
const active = ref(false)
const loading = ref(false)

const contractTypeList = ['Contract', 'Purchase Order', 'SPK', 'Other']


var project = ref({
    customer: "",
    costSheet: "",
    projectName: "",
    internalCost: "",
    sellingPrice: "",
    sales: "",
    contractType: "",
    contractNumber: "",
    contractDescription: "",
    onSiteEngineer: false
})
var pm = ref({
    pm_by: '',
    start_date: '',
    end_date: '',
    pm_periode: '',
    quantity: ''
})
var cm = ref({
    cm_by: '',
    start_date: '',
    end_date: '',
    quantity: ''
})
var sla = ref({
    severity_1_response_time: '',
    severity_1_resolution_time: '',
    severity_2_response_time: '',
    severity_2_resolution_time: '',
    severity_3_response_time: '',
    severity_3_resolution_time: '',
    severity_4_response_time: '',
    severity_4_resolution_time: ''
})
var implementation = ref({
    implementation_type: '',
    start_date: '',
    end_date: '',
})

var pKey = 1

const addCustomer = async () => {
    if(typeof project.value.customer=="string" && project.value.customer!=""){
        var checkExist = customerList.value.data.find(({customer_name}) => customer_name.toLowerCase() === project.value.customer.toLowerCase())
        if(checkExist!=undefined){
            project.value.customer = checkExist
        }
        else{
            let text = "New entry!\nDo you want to create new data?";
            if (confirm(text) == true) {
                const testCustomer = {
                    customer_name: project.value.customer,
                    customer_fullname: "",
                    customer_field: "",
                    employee: ""
                }
                try {
                    await axios.post(import.meta.env.VITE_API_URL + "customer", testCustomer, {
                        headers: {
                            "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
                        }
                    })
                    getCustomer()
                } catch (error) {
                    console.error(error)
                }
            }
            else{
                project.value.customer=undefined
            }

        }
        
    }
}
// const existUser = () => {
//     if(typeof project.value.sales=="string" && project.value.sales!=""){
//         let text = "Entry Not Found!\nPlease select an existing sales person";
//         toast.add({severity: 'error', summary: 'Error Message', detail: text, life: 3000})
//         project.value.sales=undefined
//     }
// }

const toggleActive = () => {
    active.value = !active.value
}

const drop = (e) => {
    fileUpload = e.dataTransfer.files
    pushFile(fileUpload)
    toggleActive()
}

const uploadFile = async (e) => {

    e.preventDefault()

    output = document.querySelector(".output");
    fileUpload = document.querySelector('.testFile').files
    pushFile(fileUpload)
}

const allowedExt = ['pdf', 'xls', 'xlsx', 'png', 'jpg', 'jpeg', 'doc', 'docx', 'ppt', 'pptx', 'csv']

const pushFile = (fileUpload) => {
    for (const file of fileUpload) {
        const extension = file.name.split('.').pop().toLowerCase()
        if (!allowedExt.includes(extension)) {
            alert("file type invalid")
            continue
        }
        if (finalFileList.value.length >= 5) {
            alert("max file number reached")
            break
        }
        for (const test of finalFileList.value) {

            if (test.name == file.name) {
                dupe = true
                break
            }
        }
        if (dupe == false) {
            finalFileList.value.push(file)
            // output.innerText += `\n${file.name}`
        }
        dupe = false

    }
}

const deleteFile = async (file, e) => {
    finalFileList.value.splice(finalFileList.value.indexOf(file), 1)
}


const validate = () => {
    var checkPmQuantity = pm.value.quantity.split(" ")
    var checkCmQuantity = cm.value.quantity.split(" ")
    console.log(pm.value)
    if(project.value.customer!="" &&
        project.value.costSheet!="" &&
        project.value.projectName!="" &&
        project.value.internalCost!="" &&
        project.value.sellingPrice!="" &&
        project.value.sales!="" &&
        project.value.contractType!= "" &&
        project.value.contractNumber!="" &&
        (cm.value.cm_by!='' && pm.value.pm_by!='' && implementation.value.implementation_type!='')&&
        Object.values(sla.value).every(x => x != '')
    ){
        if((cm.value.cm_by=='None' || (cm.value.cm_by!='None' && (cm.value.start_date != "" && cm.value.end_date != "" && (cm.value.quantity.includes('Ticket') || cm.value.quantity.includes('Man Days')))))&&
            (pm.value.pm_by=='None' || (pm.value.pm_by!='None' && (pm.value.start_date != "" && pm.value.end_date != "" && pm.value.pm_periode != "" && (pm.value.quantity.includes('Ticket') || pm.value.quantity.includes('Man Days')))))&&
            (implementation.value.implementation_type=='None' || (implementation.value.implementation_type!='None' && (implementation.value.start_date!="" && implementation.value.end_date != ""))))
            {
                if((cm.value.cm_by=="None" || (checkCmQuantity.length > 1 && checkCmQuantity[1]!="")) && (pm.value.pm_by=="None" || (checkPmQuantity.length > 1 && checkPmQuantity[1]!=""))){
                    valid=true
                }
            }
    }
    else{
        valid=false
    }

    // if(cm.value.cm_by!='' && pm.value.pm_by!='' && implementation.value.implementation_type!='') {
    //     if(Object.values(project.value).every(x=>x!='')){
    //         console.log("hehe")
    //         if(Object.values(sla.value).every(x => x != '')){
    //         valid=true
    //     }
    //     }
        
    //     // if(cm.value.cm_by!='None' && cm.value.start_date == new Date(0) && cm.value.end_date == new Date(0)){

    //     // }
        
    // }
    // else {
    //     valid=false
    // }
}

const submitContract = async (status) => {
    loading.value = true
    valid=false
    validate()
    if(valid==false){
        loading.value = false
        toast.add({severity: 'error', summary: 'Error Message', detail: "Data incomplete", life: 3000})
        return
    }
    let projectResponse;
    let message = "Halo";
    const finalContract = {
        customer_id: project.value.customer.customer_id,
        created_by: userStore.db_id,
        cost_sheets: project.value.costSheet,
        project_name: project.value.projectName,
        project_type: project.value.contractType,
        description: project.value.contractDescription,
        contract_number: project.value.contractNumber,
        internal_cost: project.value.internalCost,
        selling_prices: project.value.sellingPrice,
        sales_person: project.value.sales.id,
        on_site_engineer: project.value.onSiteEngineer,
        project_status: status
        
    }

    const maintenance = {
        preventive_maintenance: pm.value,
        corrective_maintenance: cm.value,
        sla: sla.value,
        implementation: implementation.value
    }


    try{
        projectResponse = await axios.post(import.meta.env.VITE_API_URL+'project', finalContract, {
            headers: {
                "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
            }
        });
        const maintenanceResponse = await axios.post(import.meta.env.VITE_API_URL+'maintenance', maintenance, {
            headers:{
                'project-id': projectResponse.data.project_id,
                "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
            }
        })
        loading.value = false
        toast.add({severity: 'success', summary: 'Success Message', detail: projectResponse.data.message, life: 5000})
        setTimeout(() => {
            router.push(`/contracts/${projectResponse.data.project_id}`);
        }, 1000);
    } catch(err){
        console.log(err)
        toast.add({severity: 'error', summary: 'Error Message', detail: err.response.data.message, life: 5000})
        loading.value = false
        return
    }

        for (const index in finalFileList._rawValue) {
            const formData = new FormData()
            formData.append('contract_file', finalFileList._rawValue[index])
            formData.append('project_id',projectResponse.data.project_id)
            try{
                await pb.collection('files').create(formData)
            }catch(error){
                console.log(err)
                toast.add({severity: 'error', summary: 'Error Message', detail: err.response.data.message, life: 5000})
                loading.value = false
            }
            
        }
}

let customerList = ref([{}])
let salesList = ref([{}])

const getCustomer = async () => {
    const response = await axios.get(import.meta.env.VITE_API_URL + `customer`)
    .then(data => {
            customerList.value = data.data
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

onMounted(async () => {
    getCustomer()

    var response = await axios.get(import.meta.env.VITE_API_URL + `user`)
        .then(data => {
            salesList.value = data.data
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            // Handle errors appropriately
        });
})

</script>

<style lang="scss" scoped>
input[type="radio"] {
    @apply w-4 h-4 mr-2
}

input[type="file"] {
    @apply hidden
}

.fileUpload {
    @apply flex flex-col items-center justify-center w-full min-h-24 bg-[#ffffff3f] text-gray-500 rounded-sm my-2 py-2 border border-[#b6b6b6] border-dashed transition ease-in-out duration-500
}

.active-dropzone {
    @apply bg-[#908c13] border-white
}

.active-dropzone p {
    @apply text-white
}

.active-dropzone #fileList {
    @apply text-white
}

.inputNum::-webkit-outer-spin-button,
.inputNum::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

</style>