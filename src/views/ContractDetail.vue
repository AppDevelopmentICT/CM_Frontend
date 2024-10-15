<template>
    <div>
        <div class="group">
            <div class="">
                <div class="flex justify-between items-center mb-2">
                    <div class="flex gap-1">
                        <h1>Contract Detail</h1>
                        <router-link v-if="userStore.role == 'Sales' || userStore.role == 'Sales Admin'" :to="{ path: `/contracts/${projectDetail.project_id}/edit`}">
                            <i class="pi pi-pencil text-[10px] text-[#908c13] bg-black p-1 rounded-md bg-opacity-10"></i>
                        </router-link>
                        
                    </div>
                    <div class="flex gap-2">
                        <div class="flex gap-2">
                            <button class="bg-[#908c13] p-2 w-48 text-white rounded-md text-sm" @click="duplicateContract()" v-if="userStore.role == 'Sales Admin'">Duplicate Contract</button>
                            <button class="bg-green-600 p-2 w-24 text-white rounded-md text-sm" @click="approvedContract()" v-if="projectDetail.project_status=='Pending' && isApprover && userStore.role == 'Sales'">Approve</button>
                            <button class="bg-red-600 text-white px-4 py-2 rounded-md text-sm" @click="rejectContract()" v-if="projectDetail.project_status=='Pending' && isApprover && userStore.role == 'Sales'">Reject</button>
                        </div>
                    </div>
                </div>
                    <div class="grid grid-cols-2 gap-x-4 gap-y-4 ">
                        <div class="subgroup">
                            <div class="flex justify-between items-center">
                                <h2>Project Information</h2>
                                <p class="text-white p-2 rounded-md" 
                                    :class="{'bg-yellow-500': projectDetail.project_status === 'Pending', 
                                    'bg-gray-400': projectDetail.project_status === 'Draft',
                                    'bg-green-500': projectDetail.project_status === 'Approved',
                                    'bg-red-600': projectDetail.project_status === 'Rejected'} ">{{projectDetail.project_status}}
                                </p>
                            </div>
                            <div class="mb-2">
                                <label for="" class="block font-bold">Customer Name</label>
                                <p>{{ projectDetail.customer_name }}</p>
                            </div>

                            <div class="mb-2">
                                <label for="" class="block">Sales Person</label>
                                <p>{{ projectDetail.sales_person }}</p>
                            </div>
                            
                            <div class="mb-2">
                                <label for="" class="block">Cost Sheet</label>
                                <p>{{ projectDetail.cost_sheets }}</p>
                            </div>

                            <div class="mb-2">
                                <label for="" class="block">Project Name</label>
                                <p>{{ projectDetail.project_name }}</p>
                            </div>                    
                        </div>
                        <div>
                            <div class="subgroup flex flex-col gap-1">
                                <h2>Contract Description</h2>
                                <div class="">
                                    <label for="" class="block">Type</label>
                                    <p>{{ projectDetail.project_type }}</p>
                                </div>
                                <div class="">
                                    <label for="" class="block">PO/Contract Number</label>
                                    <p>{{projectDetail.contract_number}}</p>
                                </div>
                                <div>
                                    <label for=""class="block">Managed Service</label>
                                    <p v-if="projectDetail.on_site_engineer">Yes</p>
                                    <p v-else>No</p>
                                </div>   
                            </div>
                            <div class="subgroup" v-if="userStore.role != 'Helpdesk'">
                                <h2>Cost Information</h2>
                                <div class="">
                                    <div class="">
                                        <label for="" class="block">Amount Reserve for Internal Cost</label>
                                        <p>Rp. {{ projectDetail.internal_cost_formatted }}</p>
                                    </div>

                                    <div class="mt-2">
                                        <label for="" class="block">Selling Price</label>
                                        <p>Rp. {{ projectDetail.selling_prices_formatted }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row-reverse gap-4">
                        <div class="subgroup w-full">
                            <div class="">
                                <label for="" class="block">CM By</label>
                                <p>{{ CM.cm_by }}</p>
                            </div>  
                            <div class="grid grid-cols-4" v-if="CM.cm_by!='None'">
                                <div class="col-span-2">
                                    <label for="" class="block">Start Date</label>
                                    <p v-if="CM.start_date=='1970-01-01'">-</p>
                                    <p v-else>{{ CM.start_date }}</p>
                                </div> 
                                <div class="col-span-2">
                                    <label for="" class="block">End Date</label>
                                    <p v-if="CM.end_date=='1970-01-01'">-</p>
                                    <p v-else>{{ CM.end_date }}</p>
                                </div>    
                                <div>
                                    <label class="block">Quantity</label>
                                    <p>{{CM.quantity}}</p>
                                </div>
                            </div>
                        </div>   
                        <div class="subgroup w-full">
                            <div class="">
                                <label for="" class="block">PM By</label>
                                <p>{{ PM.pm_by }}</p>
                            </div>  
                            <div class="grid grid-cols-2" v-if="PM.pm_by!='None'">
                                <div class="">
                                    <label for="" class="block">Start Date</label>
                                    <p>{{ PM.start_date }}</p>
                                </div> 
                                <div class="">
                                    <label for="" class="block">End Date</label>
                                    <p>{{ PM.end_date }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Maintenance Period</label>
                                    <p>{{ PM.pm_periode }}</p>
                                </div>
                                <div class="">
                                    <label for="" class="block">Quantity</label>
                                    <p>{{ PM.quantity }}</p>
                                </div>      
                            </div>
                        </div> 
                    </div>
                    <div class="flex gap-4">
                        <div class="subgroup w-1/3">
                            <div class="flex flex-col">
                                <div>
                                    <label for="" class="block">Implementation</label>
                                    <p>{{ implementation.implementation_type }}</p>
                                </div>
                                <div v-show="implementation.implementation_type!='None'">
                                    <div>
                                        <label for="" class="block">Start Date</label>
                                        <p >{{ implementation.start_date }}</p>
                                    </div>
                                    <div>
                                        <label for="" class="block">End Date</label>
                                        <p >{{ implementation.end_date }}</p>
                                    </div>
                                </div>    
                            </div>
                        </div>
                        <div class="subgroup w-full">
                            <div class="grid grid-cols-4">  
                                <div class="">
                                    <label for="" class="block">Severity 1 Response Time</label>
                                    <p v-show="sla.severity_1_response_time==''">-</p>
                                    <p>{{ sla.severity_1_response_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 1 Resolution Time</label>
                                    <p v-show="sla.severity_1_resolution_time==''">-</p>
                                    <p>{{ sla.severity_1_resolution_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 2 Response Time</label>
                                    <p v-show="sla.severity_2_response_time==''">-</p>
                                    <p>{{ sla.severity_2_response_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 2 Resolution Time</label>
                                    <p v-show="sla.severity_2_resolution_time==''">-</p>
                                    <p>{{ sla.severity_2_resolution_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 3 Response Time</label>
                                    <p v-show="sla.severity_3_response_time==''">-</p>
                                    <p>{{ sla.severity_3_response_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 3 Resolution Time</label>
                                    <p v-show="sla.severity_3_resolution_time==''">-</p>
                                    <p>{{ sla.severity_3_resolution_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 4 Response Time</label>
                                    <p v-show="sla.severity_4_response_time==''">-</p>
                                    <p>{{ sla.severity_4_response_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 4 Resolution Time</label>
                                    <p v-show="sla.severity_4_resolution_time==''">-</p>
                                    <p>{{ sla.severity_4_resolution_time }}</p>
                                </div>   
                            </div>
                        </div>
                    </div>
                    <div class="subgroup">
                        <div class="w-full">
                            <h2>Product Info</h2>
                        </div>
                        <table class="min-w-full" v-if="productInfo.length!=0" >
                            <thead class="w-full table table-fixed">
                                <tr>
                                    <th>Product</th>
                                    <th>Principal</th>
                                    <th>Product Name</th>
                                    <th>Serial Number</th>
                                    <th>SI Number</th>
                                    <th>Quantity</th>
                                </tr>
                            </thead>
                            <tbody class="overflow-y-auto block max-h-96">
                                <tr v-for="(product, index) in productInfo" v-on:click="showProductDetail(product.product_id)"
                                class="bg-white border-b cursor-pointer transition duration-300 ease-in-out hover:bg-gray-200 w-full table table-fixed"
                                :class="{'bg-yellow-300 hover:bg-yellow-400': product.serial_number == '' || product.si_number == ''}">
                                <td>{{ product.product_category }}</td>
                                <td class="truncate text-ellipsis">{{ product.principal_name }}</td>
                                <td class="truncate text-ellipsis">{{ product.product_name }}</td>
                                <td>{{ product.serial_number }}</td>
                                <td>{{ product.si_number }}</td>
                                <td>{{ product.quantity }}</td>
                            </tr>
                            </tbody>
                            
                        </table>
                        <div v-else class="flex justify-center">
                            <h3 class="text-[#a1a1a1] font-semibold text-xl">NO PRODUCTS ADDED</h3>
                        </div>
                    </div>
                        
                <div class="subgroup">
                    <h2>Additional Information</h2>
                    <div class="grid grid-cols-2 gap-x-4">
                        <div class="">
                            <label for="" class="block">Description</label>
                            <p>{{ projectDetail.description}}</p>
                        </div>

                        <div class="">
                            <label for="" class="block">Attachment File</label>
                            
                            <a v-for="file in projectFiles" :href="fileRoot + file.id + '/' + file.contract_file[0] + '?thumb=100x300'" target="_blank" class="flex gap-1 items-center hover:bg-slate-200 rounded-md px-1 my-1">
                                <i class="pi pi-file"></i>
                                <p class=" truncate text-ellipsis">{{file.contract_file[0]}}</p> 
                            </a>
                        </div>
                    </div>
                
                </div> 
            </div>   
        </div>   
    </div>

    <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75" v-if="showModal">
        <div class="bg-white rounded-lg p-8 max-w-md">
            <p class="text-lg text-center mt-4">Contract Approved!</p>
        </div>
    </div>
    <div>
        <ProductDetail
            v-model:productDetail="productDetail"
            v-model:showDetail="showDetail"
        />
    </div>
    <Toast/>
    <div class="fixed inset-0 flex flex-col items-center justify-center bg-gray-500 bg-opacity-30" v-if="loading">
        <ProgressSpinner class="w-[200px] h-[200px]"/>
        <p class="!text-[#908c13] !text-3xl !font-bold">Loading</p>
    </div>
</template>

<script setup>
import ProgressSpinner from 'primevue/progressspinner';
import { useRoute, useRouter  } from 'vue-router'
import { onMounted } from 'vue';
import {ref} from 'vue'
import axios from 'axios';
import { userManagement } from '../pinia';
import ProductDetail from '../components/ProductDetail.vue'
import PocketBase from 'pocketbase';
import { useToast } from "primevue/usetoast";

const toast = useToast();
const pb = new PocketBase(import.meta.env.VITE_PB_BASEURL);
const userStore = userManagement()
const route = useRoute();
const router = useRouter();


const customerName = ref('')
const salesName = ref('')
const contractStatus = ref('')

var projectDetail = ref({})
var projectFiles = ref()
var productInfo = ref([{}])
const loading=ref(false)
let showModal = ref(false)

let productModal = ref(false)
let productDetail = ref({})
let showDetail = ref(false)
let fileRoot = ''
let pb_id = ref()
let isApprover = ref()
var sla = ref({})
var PM = ref({})
var CM = ref({})
var implementation = ref({})

const duplicateContract = async() => {
    let projectResponse;
    var temp = JSON.parse(JSON.stringify(projectDetail.value))
    var dupeContract = {
        cost_sheets: temp.cost_sheets + '-copy',
        project_name: temp.project_name + '-copy',
        project_type: temp.project_type,
        description: temp.description,
        contract_number: temp.contract_number + '-copy',
        internal_cost: temp.internal_cost,
        selling_prices: temp.selling_prices,
        customer_id: temp.customer_id,
        created_by: temp.created_by,
        sales_person: temp.sales_person_id,
        on_site_engineer: temp.on_site_engineer,
        project_status: 'Draft'
    }

    var dupeMaintenance = {
        preventive_maintenance: JSON.parse(JSON.stringify(PM.value)),
        corrective_maintenance: JSON.parse(JSON.stringify(CM.value)),
        sla: JSON.parse(JSON.stringify(sla.value)),
        implementation: JSON.parse(JSON.stringify(implementation.value))
    }
    try {
        projectResponse = await axios.post(import.meta.env.VITE_API_URL+'project', dupeContract, {
            headers: {
                "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
            }
        });
    } catch(err) {
        toast.add({severity: 'error', summary: 'Error Message', detail: err.response.data.message, life: 5000})
    }
    const maintenanceResponse = await axios.post(import.meta.env.VITE_API_URL+'maintenance', dupeMaintenance, {
        headers:{
            'project-id': projectResponse.data.project_id,
            "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
        }
    })

    var dupeProduct
    var dupeProductCM
    var dupeProductPM
    var dupeProductSLA
    var dupeProductImplementation
    const header = {
        headers: {
            "project-id": projectResponse.data.project_id,
            "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
        }
    }

    for(var i in projectDetail.value.product_info){
        dupeProductCM = JSON.parse(JSON.stringify(projectDetail.value.product_info[i].corrective_maintenance))
        const cmResponse = await axios.post(import.meta.env.VITE_API_URL+'maintenance/cm', dupeProductCM, header)
        dupeProductCM.cm_id = cmResponse.data.id
        

        dupeProductPM = JSON.parse(JSON.stringify(projectDetail.value.product_info[i].preventive_maintenance))
        const pmResponse = await axios.post(import.meta.env.VITE_API_URL+'maintenance/pm', dupeProductPM, header)
        dupeProductPM.pm_id = pmResponse.data.id

        dupeProductSLA = JSON.parse(JSON.stringify(projectDetail.value.product_info[i].sla))
        const slaResponse = await axios.post(import.meta.env.VITE_API_URL+'maintenance/sla', dupeProductSLA, header)
        dupeProductSLA.sla_id = slaResponse.data.id


        dupeProductImplementation = JSON.parse(JSON.stringify(projectDetail.value.product_info[i].implementation))
        const implementationResponse = await axios.post(import.meta.env.VITE_API_URL+'maintenance/implementation', dupeProductImplementation, header)
        dupeProductImplementation.implementation_id = implementationResponse.data.id

        dupeProduct = JSON.parse(JSON.stringify(projectDetail.value.product_info[i]))

        const response = await axios.post(import.meta.env.VITE_API_URL + `product/project/${projectResponse.data.project_id}`, dupeProduct, {
            headers: {
                "project-id": projectResponse.data.project_id,
                "project-name": projectResponse.data.project_id,
                "pm-id": dupeProductPM.pm_id,
                "cm-id": dupeProductCM.cm_id,
                "sla-id": dupeProductSLA.sla_id,
                "implementation-id": dupeProductImplementation.implementation_id,
                "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
            }
        })
    }
    router.push(`/contracts/${projectResponse.data.project_id}/edit?duplicate=True`)
}

const showProductDetail = (id) => {

    productDetail.value = productInfo.value.find(({product_id}) => product_id === id)
    showDetail.value=true

    
}
const closeProductModal = () => {
    productModal.value=false
}

const checkApprover = async () => {
    const response = await axios.get(import.meta.env.VITE_API_URL+'isApprover', {
        headers: {
            "user-id": userStore.db_id,
            "project-id": route.params.id
        }
    })
    .then(data => {
        isApprover.value = data.data.isApprover
    })
}


const getFile = async () => {
    const record = await pb.collection('files').getList(1,5,{
        filter: `project_id="${route.params.id}"`
    })
    .then(data => {
        projectFiles.value = data.items,
        pb_id.value = data.id,
        fileRoot = "https://pocketbase.ictincub.my.id/api/files/nh8a6wpfc1smgyp/"
    })
}

const getSLA = async () => {
    const result=[{}]
    const response = await axios.get(import.meta.env.VITE_API_URL + `maintenance/sla`,
    {
        headers:{
            'project-id':route.params.id
        } 
    }).then(data => {
        result.value = data.data
        sla.value = result.value.data
    }).catch(error => {
        console.error('Error fetching data:', error);
    });
}
const getPM = async () => {
    const result=[{}]
    const response = await axios.get(import.meta.env.VITE_API_URL + `maintenance/pm`,
    {
        headers:{
            'project-id':route.params.id
        } 
    }).then(data => {
        result.value = data.data
        PM.value = result.value.data
    }).catch(error => {
        console.error('Error fetching data:', error);
    });
}
const getCM = async () => {
    const result=[{}]
    const response = await axios.get(import.meta.env.VITE_API_URL + `maintenance/cm`,
    {
        headers:{
            'project-id':route.params.id
        } 
    }).then(data => {
        result.value = data.data
        CM.value = result.value.data
    }).catch(error => {
        console.error('Error fetching data:', error);
    });
}

const getImple = async () => {
    const result=[{}]
    const response = await axios.get(import.meta.env.VITE_API_URL + `maintenance/implementation`,
    {
        headers:{
            'project-id':route.params.id
        } 
    }).then(data => {
        result.value = data.data
        implementation.value = result.value.data
        
    }).catch(error => {
        console.error('Error fetching data:', error);
    });
}

const fetchProjectDetails = async () => {
    try {
        const response = await axios.get(import.meta.env.VITE_API_URL + `project/${route.params.id}`);
        const result = response.data;
        projectDetail.value = result.data;
        
        const formatNumber = (number) => {
            return new Intl.NumberFormat('de-DE').format(number);
        }  

        projectDetail.value.internal_cost_formatted = formatNumber(projectDetail.value.internal_cost);
        projectDetail.value.selling_prices_formatted = formatNumber(projectDetail.value.selling_prices);
        productInfo.value = result.data.product_info;
    
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

onMounted(async () => {
    
    await fetchProjectDetails();

    if(projectDetail.value.remaining_date > 0) {
        contractStatus.value =  "OnGoing"
    } else {
        contractStatus.value =  "Expired"
    }

    await checkApprover()
    await getFile()
    await getSLA()
    await getPM()
    await getCM()
    await getImple()
})

const approvedContract = async () => {
    loading.value=true
    try {
        const response = await axios.patch(import.meta.env.VITE_API_URL + `project/approve/${route.params.id}`, null, {
            headers: {
                'user-id': userStore.db_id
            }
        })
        loading.value = false
        toast.add({severity: 'success', summary: 'Success Message', detail: response.data.message, life: 5000})
        setTimeout(() => {
            router.push('/');
        }, 1000);
    } catch(e) {
    }   
}

const rejectContract = async () => {
    loading.value=true
    try {
        const response = await axios.patch(import.meta.env.VITE_API_URL + `project/reject/${route.params.id}`, null, {
            headers: {
                'user-id': userStore.db_id
            }
        })
        loading.value = false
        toast.add({severity: 'success', summary: 'Success Message', detail: response.data.message, life: 5000})
        setTimeout(() => {
            router.push('/');
        }, 1000);
    } catch(e) {
        console.error('Error rejecting data:', error);
    }   
}
</script>

<style lang="scss" scoped>
.inputNum::-webkit-outer-spin-button,
.inputNum::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

</style>