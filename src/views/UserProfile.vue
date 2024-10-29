<template>
    <h4 class="text-2xl font-semibold mb-4">User Profile</h4>
    <div class="flex gap-5">
        <section class="rounded-md w-full">
            <div class="py-2">
                <div class="flex flex-col gap-3">
                    <div class="border border-black p-2">
                        <h4 class="font-semibold">Name</h4>
                        <input type="text" class="w-full my-2 border-b-2 border-black focus:outline-none disabled" v-model="userEditData.username" v-bind:disabled="editable == false">
                    </div>
                    <!--
                    <div class="border border-black p-2">
                        <h4 class="font-semibold">Email</h4>
                        <input type="email" class="w-full my-2 border-b-2 border-black focus:outline-none disabled" v-model="userEditData.email" v-bind:disabled="editable == false">
                    </div>
                    -->
                    <div class="border border-black p-2">
                        <h4 class="font-semibold">Roles</h4>
                        <p class="text-[14px] text-gray-500 font-[14px]">{{ userEditData.user_roles }}</p>
                    </div>
                    <div class="border border-black p-2 flex gap-8">
                        <div class="">
                            <h4 class="font-semibold">Approver privilege</h4>
                            <input type="checkbox" v-model="userEditData.isapprover" v-bind:disabled="editable == false">
                        </div>
                        <div class="">
                            <h4 class="font-semibold">Login Info</h4>
                            <input type="checkbox" v-model="userEditData.isLogin" v-bind:disabled="editable == false">
                        </div>
                    </div>
                    <div class="flex gap-4 justify-end">
                        <button v-if="userData.user_roles == 'Super Admin'" class="bg-red-600 p-2 text-white rounded-md" @click="deleteUser" :class="{'hidden': editable}">Delete User</button>
                        <button class="bg-[#908c13] p-2 text-white rounded-md" @click="openChangePassword" :class="{'hidden': editable}">Change Password</button>
                        <button class="bg-[#908c13] p-2 text-white rounded-md" @click="editable = !editable" :class="{'hidden': editable}">Edit User</button>
                        <button class="bg-orange-500 p-2 text-white rounded-md" @click="cancelClick" :class="{'hidden': !editable}">Cancel Changes</button>
                        <button class="bg-emerald-600 p-2 text-white rounded-md" @click="saveClick" :class="{'hidden': !editable}">Save Changes</button>
                    </div>
                </div>
            </div>
        </section>
        <div v-if="userData.user_roles == 'Sales'" class="w-full h-fit flex flex-col gap-7">
            <section class=" flex gap-5 justify-center">
                <div class="h-36 w-72 bg-green-500 flex flex-col  p-3 shadow-sm shadow-gray-400 rounded-md select-none text-white">
                    <div class="flex w-full">
                        <span class="w-3 h-3 self-center mr-1 bg-blue-700"></span>
                        <h4 class="text-lg font-semibold">Project Handle</h4>
                        <i class="pi pi-briefcase self-center ml-auto"></i>
                    </div>
                    <div class="flex mb-0 w-full h-full">
                        <p class="text-4xl mt-3 self-center font-bold">{{userTotalProject}}</p>
                        <p class="text-md mt-3 self-end ml-auto">Test</p>
                    </div>
                </div>
                <div class="">
                    <div class="h-36 w-72 flex flex-col z-50 p-3 shadow-sm shadow-gray-400 rounded-md select-none text-black">
                        <div class="flex w-full">
                            <span class="w-3 h-3 self-center mr-1" :class="{'bg-green-600': userData.isapprover === true, 'bg-red-600': userData.isapprover === false}"></span>
                            <h4 class="text-lg font-semibold">Contract Approved</h4>
                            <i class="pi self-center ml-auto" :class="{'pi-check': userData.isapprover === true, 'pi-times': userData.isapprover === false}"></i>
                        </div>
                        <div class="flex mb-0 w-full h-full">
                            <p v-if="userData.isapprover" class="text-4xl mt-3 self-center font-bold">{{userApprovedProject}}</p>
                            <p v-else class="text-lg mt-3 self-center text-red-600 w-full text-center font-bold">Can't approve project</p>
                        </div>
                    </div>
                </div>
            </section>
            <section class="px-6">
                <div class="flex flex-col">
                    <div class="flex justify-between">
                        <h3 class="my-3 text-lg font-semibold"> 
                            <span v-if="!tableCondition">Approved Project</span>
                            <span v-else>Project Handled</span>
                            By: {{ userData.username }}</h3>
                        <button class="bg-[#908c13] my-2 p-1 text-white rounded-md text-sm" @click="tableCondition = !tableCondition">Change Table</button>
                    </div>
                    <TableOnClick :data="tableHeader" :row_data="tableData" v-if="!tableCondition"/>
                    <TableOnClick :data="tableHeader" :row_data="tableData2" v-else="tableCondition"/>
                </div>
            </section>
        </div>
    </div>
    <div class="fixed inset-0 flex items-center z-50 justify-center bg-gray-800 bg-opacity-75" v-if="showChangePass">
        <div class="bg-white rounded-lg p-8 min-w-[400px]  max-w-md">
            <div class="flex justify-end">
                <button class="pi pi-times " v-on:click="openChangePassword"></button>
            </div>
            <div>
                <label for="" class="block">Old Password</label>
                <input class="inputBox" type="text" v-model="oldPass">
                <label for="" class="block pt-4">New Password</label>
                <input class="inputBox" type="text" v-model="newPass">
                <div class="flex justify-end">
                    <button class="bg-[#908c13] p-2 w-32 text-white rounded-md" @click="checkPass">check pass</button>
                </div>
                
            </div>
        </div>

    </div>
    <Toast/>
</template>

<script setup>
import {onMounted, ref, watch} from 'vue';
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios';
import { useToast } from "primevue/usetoast";
import PocketBase from 'pocketbase';
import TableOnClick from '../components/TableOnClick.vue';

const pb = new PocketBase(import.meta.env.VITE_PB_BASEURL);
const toast = useToast();
const route = useRoute()
const router = useRouter();
const userData = ref({})
const userEditData = ref({})
const userTotalProject = ref(0)
const userApprovedProject = ref(0)
const approvedProject = ref({})
const showChangePass = ref(false)
const oldPass = ref('')
const newPass = ref('')

// Table Approved project
const tableHeader = ["Project", "Details"]
const tableData = ref()
const tableCondition = ref(false)

// Table Project Handle
const tableData2 = ref()

const editable = ref(false)

const getUserbyId = async () => {
    try {
        const record = await pb.collection('users').getOne(route.params.id);
        const response = await axios.get(import.meta.env.VITE_API_URL+`user/${route.params.id}`)
        userData.value = {...response.data.data,isLogin: record.loginAccount}
        userEditData.value = {
            ...userData.value,
            isLogin: record.loginAccount
        }
    } catch(error) {
        console.log(error)
    }
}

const openChangePassword = () => {
    showChangePass.value = !showChangePass.value
    console.log(showChangePass.value)
}
const checkPass = () => {
    console.log(oldPass.value)
    console.log(newPass.value)
}

const cancelClick = () => {
    editable.value = !editable.value
    userEditData.value = {...userData.value}
}

const saveClick = async () => {
    const pbbody = {
        name: userEditData.value.username,
        loginAccount: userEditData.value.isLogin
    }
    const dbbody = {
        username: userEditData.value.username,
        email: userEditData.value.email,
        isApprover: userEditData.value.isapprover
    }
    try {
        const record = await pb.collection('users').update(userEditData.value.user_id, pbbody);
        try {
            const response = await axios.patch(import.meta.env.VITE_API_URL+`user/${route.params.id}`, dbbody)
            getUserbyId()
            editable.value = false
            toast.add({severity: 'success', summary: 'Success Message', detail: response.data.message, life: 5000})
        } catch (e) {
            toast.add({severity: 'error', summary: 'Error Message', detail: "Error updating data!", life: 5000})
        }
    } catch (error) {
        console.log(error);
        toast.add({severity: 'error', summary: 'Error Message', detail: "Error updating data!", life: 5000})
    }
}

const getUserProjectHandle = async () => {
    try {
        const response = await axios.get(import.meta.env.VITE_API_URL+`user-dashboard/project`, {
            headers: {
                'user': `${userData.value.user_id}`
            }
        })
        let temp_data = response.data.data
        userTotalProject.value = response.data.total
        tableData2.value = temp_data.map((project) => Object.values(project))
    } catch(e) {
        console.error(e)
    }
}

const getTotalApprovedProject = async () => {
    try {
        const response = await axios.get(import.meta.env.VITE_API_URL+`user-dashboard/approved`, {
            headers: {
                'user': `${userData.value.user_id}`
            }
        })
        let temp_data = response.data.data
        userApprovedProject.value = response.data.total
        approvedProject.value = temp_data.map((project) => Object.values(project))

        tableData.value = approvedProject.value
    } catch(e) {
        console.error(e)
    }
}

const deleteUser = async() => {
    let response = ''
    let text = "Are you sure you want to delete this user?\n";
    if (confirm(text) == true) {
        try {
            response = await axios.delete(import.meta.env.VITE_API_URL + `user/${route.params.id}`)
            console.log(response)
            if(response.status == 200){
                await pb.collection('users').delete(route.params.id)
            }
        } catch (error) {
            console.log(error)
        }
        toast.add({severity: 'success', summary: 'Success Message', detail: response.data.message, life: 5000})
        setTimeout(() => {
            router.push(`/user`);
        }, 1000);
    }
}

watch(userData, (x) => {
    
})



onMounted(async() => {
    await getUserbyId();
    getUserProjectHandle()
    getTotalApprovedProject()
})
</script>