<template>
    <section class="flex">
        <div class="w-full">
            <div class="p-2 w-full">
                <label for="fullname">Full Name<span class="text-red-600">*</span></label>
                <input class="inputBox" id="fullname" type="text" v-model="data.username" autocomplete="off" required>
            </div>
            <div class="p-2 w-full">
                <label for="email">Email<span class="text-red-600">*</span></label>
                <div class="flex">
                    <input class="inputBox" id="email" type="text" v-model="data.email" autocomplete="off" required>
                    <span class="bg-gray-400 min-w-fit text-md text-white rounded-sm p-2 my-2">@infracom-tech.com</span>
                </div>
            </div>
            <div class="p-2 w-full">
                <label for="roles" class="block">Roles<span class="text-red-600">*</span></label>
                <Dropdown v-model="data.user_roles" :options="roleList" placeholder="" id="dropdown"
                                pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
                                class="inputBox"/> 
            </div>
            <div class="flex justify-evenly">
                <div class="p-2 flex items-center gap-2">
                    <input id="approver" type="checkbox" v-model="data.isApprover" class="w-4 h-4 mt-1">
                    <label for="approver">Assign as Approver</label>
                </div>
                <div class="p-2 flex items-center gap-2">
                    <input id="loginEnabled" type="checkbox" :disabled="data.isApprover == true" v-model="data.createAccount" class="w-4 h-4 mt-1">
                    <label for="loginEnabled">Enable Login</label>
                </div>
            </div>

        </div>
        <div class="w-full">
            <div class="p-2 w-full">
                <label for="password">Password</label>
                <input class="inputBox" id="password" v-model="data.password" type="password" disabled autocomplete="off">
            </div>
            <div class="p-2 w-full">
                <label for="confirm_password">Confirm Password</label>
                <input class="inputBox" id="confirm_password" v-model="data.confirm_password" type="password" disabled autocomplete="off">
            </div>
            <div class="flex justify-between w-full px-2">
                <p class="text-sm self-center">Default Password: <span class="underline font-bold">ICT_{{passwordPlaceholder}}</span></p>
                <button class="p-1 bg-orange-300 text-white text-sm rounded-sm hidden">Set Password</button>
            </div>
        </div>
    </section>
    <div class="w-full flex">
        <button @click="submitForm()" class="bg-emerald-600 text-white p-[6px] rounded-md ml-auto w-[120px] flex items-center justify-center">
            <span v-if="!loading" class="flex items-center">
                <span>Create Account</span>
            </span>
            <span v-else class="flex items-center">
                <Loader />
            </span>
        </button>
    </div>
    <Toast/>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useToast } from "primevue/usetoast";
import Loader from '../Loader.vue'
import axios from 'axios';
import PocketBase from 'pocketbase';
import Dropdown from 'primevue/dropdown';
import { useRoute, useRouter } from 'vue-router'

const toast = useToast();
const pb = new PocketBase(import.meta.env.VITE_PB_BASEURL);

const router = useRouter();

const roleList = ['Super Admin', 'Sales Admin', 'Sales', 'Helpdesk']

const data = ref({
    username: '',
    email: '',
    user_roles: '',
    isApprover: false,
    password: '',
    confirm_password: '',
    createAccount: false,
    loginAccount: false
})
const passwordPlaceholder = ref('')
let loading = ref(false)

const clearValue = () => {
    data.value.username = ''
    data.value.email = ''
    data.value.user_roles = ''
    data.value.password = ''
    data.value.confirm_password = ''
    data.value.createAccount = false
    data.value.isApprover = false
    data.createAccount = false
}

const getSecretKey = async () => {
    try {
        const response = await axios.get(import.meta.env.VITE_API_URL + "secret-key", {
            headers: {
                id: JSON.parse(localStorage.getItem('user')).pb_id
            }
        })
        return response.data
    }catch(e) {
        console.error(e);
    }
}

const insertData = async () => {
    loading.value = true
    let token = await getSecretKey()
    
    let message = ''
    let pb_id_response = ''
    const pb_body = {
        "username": data.value.username.replace(/\s+/g,'.').toLocaleLowerCase(),
        "email": data.value.email + '@infracom-tech.com',
        "emailVisibility": true,
        "password": data.value.password,
        "passwordConfirm": data.value.confirm_password,
        "name": data.value.username,
        "loginAccount": data.value.createAccount,
        "secret_key": token
    }
    try {
        const pb_response = await pb.collection('users').create(pb_body);
        pb_id_response = pb_response.id
        if(pb_id_response) {
            try {
                const db_response = await axios.post(import.meta.env.VITE_API_URL+'register', {
                    "id": pb_response.id,
                    "username": data.value.username,
                    "password": data.value.password,
                    "email": data.value.email + '@infracom-tech.com',
                    "user_roles": data.value.user_roles,
                    "isApprover": data.value.isApprover
                }, {headers:{
                    "user-token": JSON.parse(localStorage.getItem('pocketbase_auth')).token
                }});
                clearValue()
            } catch(e) {
                console.error(e)
            }
        }
    } catch(e) {
        console.error(e)
    }
    toast.add({ severity: 'success', summary: 'Success', detail: message, life: 5000 });
    
    loading.value = false
    setTimeout(() => {
            router.go();
        }, 1000);
    }

const submitForm = () => {
    if(data.value.password == '') {
        data.value.password = "ICT_" + data.value.username.replace(/\s+/g, '');
        data.value.confirm_password = "ICT_" + data.value.username.replace(/\s+/g, '');
        insertData()
    } else {
        if(data.value.password !== data.value.confirm_password) {
            alert("Password Doesn't Match") 
            return
        }
        insertData()
    }
}

watch(() => data.value.username, (x, y) => {
    passwordPlaceholder.value = x.replace(/\s+/g,'')
    data.value.email = x.replace(/\s+/g,'.').toLocaleLowerCase()
})

watch(() => data.value.isApprover, (x, y) => {
    if (x === true) {
        data.value.createAccount = true
    }
})


onMounted(() => {
    
})

</script>