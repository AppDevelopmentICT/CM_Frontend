<script setup lang="ts">
import { ref } from 'vue';
import { userManagement } from '../pinia';

const store = userManagement();

let showDropdown = ref(false);

const handleMouseOver = () => {
    showDropdown.value = true;
}

const handleMouseOut = (event: any) => {
    if (!event.relatedTarget || !event.relatedTarget.closest('#master-data-dd') && !event.relatedTarget.closest('#master-data-list')) {
        showDropdown.value = false;
    }
}
</script>

<template>
    <nav class="fixed w-[16rem] p-5 bg-slate-100 h-dvh z-10" @mouseout="handleMouseOut">
        <RouterLink to="/">
            <div class="flex gap-4 justify-center cursor-pointer">
                <img src="../assets/ict.png" alt="Logo ICT" class="w-9 h-9">
                <h4 class="text-md font-bold self-center text-[#908c13]">Contract <br> Management</h4>
            </div>
        </RouterLink>
        <hr>
        <section class="flex flex-col mt-3 h-full" >
            <div class="flex flex-col text-center cursor-pointer">
                <p class="text-black font-bold">{{store.name}}</p>
                <p class="text-neutral-400">{{store.role}}</p>
            </div>

            <section class="flex flex-col mt-6 gap-2 relative">
                <RouterLink to="/" active-class="active-link" v-if="store.role != 'Helpdesk'">
                    <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-3 text-neutral-400 gap-4 transition">
                        <i class="pi pi-home" style="font-size: 1.5rem"></i>
                        <p class="">Home</p>
                    </div>
                </RouterLink>
                <RouterLink to="/addContract" v-if="store.role == 'Sales Admin'">
                    <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-3 text-neutral-400 gap-4 transition">
                        <i class="pi pi-plus" style="font-size: 1.5rem"></i>
                        <p class="">Add Contract</p>
                    </div>
                </RouterLink>
                <RouterLink to="/contracts" v-if="store.role == 'Sales Admin' || store.role == 'Sales'|| store.role == 'Super Admin' || store.role == 'Helpdesk'">
                    <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-3 text-neutral-400 gap-4 transition">
                        <i class="pi pi-list" style="font-size: 1.5rem"></i>
                        <p class="">List Contract</p>
                    </div>
                </RouterLink>
                <!-- <RouterLink to="/pendingContract" v-if="store.role == 'Sales Admin' || store.role == 'Sales'">
                    <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-3 text-neutral-400 gap-4 transition">
                        <i class="pi pi-info-circle" style="font-size: 1.5rem"></i>
                        <p class="">Pending List</p>
                    </div>
                </RouterLink> -->
                <RouterLink to="/user" v-if="store.role == 'Super Admin'">
                    <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-3 text-neutral-400 gap-4 transition">
                        <i class="pi pi-cog" style="font-size: 1.5rem"></i>
                        <p class="">Manage User</p>
                    </div>
                </RouterLink>
                <RouterLink to="/audit-log">
                    <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-3 text-neutral-400 gap-4 transition">
                        <i class="pi pi-file-edit" style="font-size: 1.5rem"></i>
                        <p class="">Audit Log</p>
                    </div>
                </RouterLink>
                <section @mouseover="handleMouseOver" v-if="store.role == 'Sales Admin'">
                    <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-3 text-neutral-400 gap-4 transition cursor-pointer" id="master-data-dd">
                        <i class="pi pi-chevron-down" style="font-size: 1.5rem"></i>
                        <p class="">Master Data</p>
                    </div>
                    <section id="master-data-list" class="w-full pl-8 flex flex-col gap-1 mt-1" v-if="showDropdown" @mouseover="handleMouseOver" @mouseout="handleMouseOut"> 
                        <RouterLink to="/brand">
                        <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-1 px-2 text-neutral-400 transition text-[13px]">
                            <p class="">Brand</p>
                        </div>
                        </RouterLink>
                        <RouterLink to="/periode">
                        <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-1 px-2 text-neutral-400 transition text-[13px]">
                            <p class="">Maintenance Period</p>
                        </div>
                        </RouterLink>
                        <RouterLink to="/customer">
                            <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-1 px-2 text-neutral-400 transition text-[13px]">
                                <p class="">Customer</p>
                            </div>
                        </RouterLink>
                        <RouterLink to="/cm_by">
                            <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-1 px-2 text-neutral-400 transition text-[13px]">
                                <p class="">Corrective Maintenance</p>
                            </div>
                        </RouterLink>
                        <RouterLink to="/pm_by">
                            <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-1 px-2 text-neutral-400 transition text-[13px]">
                                <p class="">Preventive Maintenance</p>
                            </div>
                        </RouterLink>
                        <RouterLink to="/category">
                            <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-1 px-2 text-neutral-400 transition text-[13px]">
                                <p class="">Product Category</p>
                            </div>
                        </RouterLink>
                    </section>
                </section>
                <router-link to="/logout">
                <div class="hover:bg-[#908c13] hover:text-white rounded-lg flex p-3 text-neutral-400 gap-4 transition">
                    <i class="pi pi-user" style="font-size: 1.5rem"></i>
                    <p class="">Logout</p>
                </div>
                </router-link>
            </section>
        </section>
    </nav>
</template>
<style scoped>
.active-link .nav-item {
  background-color: #908c13; 
  color: white; 
}
</style>