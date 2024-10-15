<template>
    <div>
        <!-- primevue dropdown
        editable biar bisa ketik dalem dropdown boxnya
        filter buat search
        kalo ga pake hapus aja tergantung keperluan dropdown -->
        <div class="pb-2">
            <label for="" class="block">Customer Name<span class="text-red-600">*</span></label>
            <Dropdown v-model="customer" editable filter :options="customerList.data" optionLabel="customer_name" placeholder="" id="dropdown"
            pt:input:class="p-0 text-sm" pt:clearIcon:class="text-black" pt:trigger:class="text-black"
            class="inputBox" v-on:blur="entry"/> 
        </div>
        <button v-on:click="log" class="bg-[#908c13] text-white rounded-sm p-2 my-2">log</button>
    </div>
</template>

<script setup>
import Dropdown from 'primevue/dropdown';
import { onMounted } from 'vue';
import { ref } from 'vue'
import axios from 'axios';

const customer = ref({})
const customerName = ref('')
const customerId = ref('08a6d425-5580-43f0-a2dd-900dbdf36d4a')

var customerList = ref([{}])

const fetchCustomer = async () => {
    const response = await axios.get(import.meta.env.VITE_API_URL + "customer")
        .then(data => {
            customerList.value = data.data
        })
        .catch(error => {
            console.error('Error fetching data:', error);

        });
}

const entry = async () => {
    if(typeof customer.value=="string" && customer.value != ""){
        let text = "New entry!\nDo you want to create new data?";
        if (confirm(text) == true) {
            const testCustomer = {
                customer_name: customer.value,
                customer_fullname: "",
                customer_field: "",
                employee: ""
            }
            try {
                const response = await axios.post(import.meta.env.VITE_API_URL + "customer", testCustomer)
                fetchCustomer()

            } catch (error) {
            }
        }
        else{
            customer.value=undefined
        }
    }
}

onMounted(async () => {
    await axios.get(import.meta.env.VITE_API_URL + `customer`)
        .then(data => {
            customerList.value = data.data
            customer.value = customerList.value.data.find(({customer_id}) => customer_id === customerId.value)
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            // Handle errors appropriately
        });
})
</script>

<style lang="scss" scoped >


.select-editable {
    @apply relative
}
.select-editable select {
    @apply absolute
}
.select-editable input {
    @apply absolute w-[90%] h-[90%] border-none text-sm top-2 m-2
}
.select-editable select:focus, .select-editable input:focus {outline:none;}




</style>