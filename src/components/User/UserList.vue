<template>
    <div class="flex justify-between px-8">
        <h4 class="self-center text-[#908c13] text-2xl font-semibold">User</h4>
    </div>
    <div class="flex flex-col">
        <div class="overflow-x-auto sm:mx-0.5 lg:mx-0.5">
            <div class="py-2 inline-block min-w-full">
                <div class="overflow-hidden">
                    <table class="min-w-full">
                        <thead class="bg-[#908c13] border-b">
                            <tr>
                                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                                    Name
                                </th>
                                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                                    Email
                                </th>
                                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                                    Role
                                </th>
                                <th class="text-sm font-medium text-white px-6 py-4">
                                    isApprover
                                </th>
                                <th class="text-sm font-medium text-white px-6 py-4">
                                    Login
                                </th>
                                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                                    Details
                                </th>
                            </tr>

                        </thead>
                        <tbody>
                            <tr v-for="user in userList" :key="user.id"
                                class="items-center px-4 bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100 text-sm text-gray-900 font-light whitespace-nowrap">
                                <td class="">{{ user.username }}</td>
                                <td class="">{{ user.email }}</td>
                                <td class="">{{ user.user_roles }}</td>
                                <td class="w-fit"><input class="flex w-full mx-auto" type="checkbox" name="" id="" disabled v-bind:checked="user.isapprover"></td>
                                <td class="w-fit"><input class="flex w-full mx-auto" type="checkbox" name="" id="" disabled v-bind:checked="user.isLogin"></td>
                                <router-link :to="{ path: `user/${user.id}` }">    
                                    <button class="bg-emerald-800 p-2 rounded-md text-white m-2 px-2">Users Details</button>
                                </router-link>
                            </tr>
                        </tbody>
                    </table>
                </div>
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

</template>

<script setup>

import { onMounted } from 'vue';
import { ref } from 'vue'
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router'
import PocketBase from 'pocketbase';
import { userManagement } from '../../pinia';

const store = userManagement();
const pb = new PocketBase(import.meta.env.VITE_PB_BASEURL);
const route = useRoute();
const router = useRouter();

let userList = ref()
let loading = true
const userName = ref('')
const userEmail = ref('')
const userRole = ref('')
const isApprover = ref(false)
const userData = ref({})

const fetchUser = async () => {
    try {
        const record = pb.collection()
        const response = await axios.get(import.meta.env.VITE_API_URL + "all_user", {
            headers: {
                'user-id': `${store.db_id}`
            }
        })
        userList.value = {
            ...response.data.data,
        }
    } catch (e) {
        console.error(e)
    }
    
}

onMounted(async () => {
    fetchUser()
})
</script>

<style scoped>
table td {
    @apply py-2 px-6
}

input[type="text"], select {
    @apply border-b-2 focus:border-[#908c13] focus:outline-0 w-full mb-4
}
input[type="checkbox"]{
    @apply size-4 accent-[#908c13]
}

.asd {
    @apply border-red-500
}

h1 {
    @apply text-[#908c13] font-semibold text-2xl mb-4
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