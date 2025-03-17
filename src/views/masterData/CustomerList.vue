<template>
  <div class="flex flex-row justify-between px-8">
    <h1>Customer</h1>
    <button
      v-on:click="addCustomer"
      class="bg-[#908c13] p-2 text-white flex items-center rounded-md"
    >
      <i class="pi pi-plus pr-2"></i>
      Add New Customer
    </button>
  </div>
  <div class="flex items-center gap-4 justify-end px-8">
    <div class="flex w-1/3">
      <Dropdown
        v-model="searchType"
        :options="searchTypeList"
        placeholder="Search Category"
        pt:input:class="p-0 text-sm"
        pt:clearIcon:class="text-black"
        pt:trigger:class="text-black"
        class="inputBox basis-2/5"
      />
      <IconField iconPosition="right" class="basis-3/5">
        <InputIcon>
          <i class="pi pi-search" />
        </InputIcon>
        <input type="text" class="inputBox" v-model="searchInput" />
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
                <th></th>
                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                  Name
                </th>
                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                  Full Name
                </th>
                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                  Field
                </th>
                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                  Employee Count
                </th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="customer in currList"
                :key="customer.customer_id"
                class="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100 text-sm text-gray-900 font-light whitespace-nowrap"
                v-on:click="editCustomer(customer.customer_id)"
              >
                <td>
                  <span
                    class="w-3 h-3 self-center inline-block rounded-[50%]"
                    :class="
                      !customer.employee ||
                      !customer.customer_fullname ||
                      !customer.customer_field
                        ? 'bg-yellow-300'
                        : ''
                    "
                  ></span>
                </td>
                <td>{{ customer.customer_name }}</td>
                <td>{{ customer.customer_fullname }}</td>
                <td>{{ customer.customer_field }}</td>
                <td>{{ customer.employee }}</td>
                <td>
                  <button
                    class="bg-red-600 p-2 rounded-md text-white"
                    onclick="event.stopPropagation()"
                    v-on:click="deleteCustomer(customer.customer_id)"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="w-full">
            <div class="flex justify-end mt-2">
              <span
                class="w-4 h-4 bg-yellow-300 rounded-[50%] self-center mr-1 inline-block"
              ></span>
              <h4 class="text-xs text-gray-400">
                Data Entry <span class="font-semibold">Incomplete</span>
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75"
    v-if="showModal"
  >
    <div class="bg-white rounded-lg p-8 min-w-[400px] max-w-md">
      <div class="flex justify-end">
        <button class="pi pi-times" v-on:click="addCustomer"></button>
      </div>
      <h1
        v-if="customerForm.customer_id == ''"
        class="text-center mt-4 text-[#908c13] font-semibold text-2xl mb-4"
      >
        Add Customer
      </h1>
      <h1
        v-else
        class="text-center mt-4 text-[#908c13] font-semibold text-2xl mb-4"
      >
        Edit Customer
      </h1>
      <div class="py-2">
        <label class="block"
          >Customer Name<span class="text-red-600">*</span></label
        >
        <input
          type="text"
          class="inputBox"
          v-model="customerForm.customer_name"
        />
      </div>
      <div class="py-2">
        <label class="block"
          >Customer Full Name<span class="text-red-600">*</span></label
        >
        <input
          type="text"
          class="inputBox"
          v-model="customerForm.customer_fullname"
        />
      </div>
      <div class="py-2">
        <label class="block"
          >Customer Field<span class="text-red-600">*</span></label
        >
        <input
          type="text"
          class="inputBox"
          v-model="customerForm.customer_field"
        />
      </div>
      <div class="py-2">
        <label class="block"
          >Customer Employee Count<span class="text-red-600">*</span></label
        >
        <Dropdown
          v-model="customerForm.employee"
          filter
          :options="employeeList"
          placeholder=""
          id="dropdown"
          pt:input:class="p-0 text-sm"
          pt:clearIcon:class="text-black"
          pt:trigger:class="text-black"
          class="inputBox"
        />
      </div>

      <div class="flex justify-end">
        <button
          class="bg-[#908c13] text-white px-2 py-1 rounded-md"
          v-on:click="submitCustomer"
        >
          submit
        </button>
      </div>
    </div>
  </div>
  <Transition>
    <div class="fixed top-0 left-1/2 translate-x-[-50%] my-2" v-if="showToast">
      <div
        class="bg-white rounded-lg p-4 min-w-48 max-w-md flex justify-center"
      >
        invalid or empty input
      </div>
    </div>
  </Transition>
  <Toast />
</template>

<script setup>
import { onMounted } from "vue";
import { ref, watch } from "vue";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";
import { useToast } from "primevue/usetoast";
import Dropdown from "primevue/dropdown";
import _ from "lodash";
import "primeicons/primeicons.css";
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";

const searchInput = ref("");
const searchTypeList = ["Name", "Full Name"];
const searchType = ref("Name");
const currList = ref([{}]);
let searchList;

const toast = useToast();
const route = useRoute();
const router = useRouter();

let customerList = ref([{}]);
let loading = true;

var customerForm = ref({
  customer_id: "",
  customer_name: "",
  customer_fullname: "",
  customer_field: "",
  employee: "",
});

const employeeList = [
  "1-50 Employees",
  "51-100 Employees",
  "101-500 Employees",
  "501-1000 Employees",
  "1001-5000 Employees",
  "5000+ Employees",
];

const showModal = ref(false);
const showToast = ref(false);
const test = ref(false);
var valid = false;

watch(searchType, (x) => {
  searchInput.value = "";
});
watch(searchInput, (x) => {
  if (searchInput.value == "") {
    searchList = customerList.value;

    currList.value = _.cloneDeep(searchList.value);
  } else {
    if (searchType.value == "Name") {
      searchList = customerList.value.filter((list) =>
        list.customer_name
          .toLowerCase()
          .includes(searchInput.value.toLowerCase()),
      );
    } else {
      searchList = customerList.value.filter((list) =>
        list.customer_fullname
          .toLowerCase()
          .includes(searchInput.value.toLowerCase()),
      );
    }
  }
  currList.value = _.cloneDeep(searchList);
});

const addCustomer = () => {
  customerForm.value.customer_id = "";
  customerForm.value.customer_name = "";
  customerForm.value.customer_fullname = "";
  customerForm.value.customer_field = "";
  customerForm.value.employee = "";
  showModal.value = !showModal.value;
};

const editCustomer = async (customer_id) => {
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `customer/${customer_id}`)
    .then((data) => {
      customerForm.value = data.data.data;
      showModal.value = !showModal.value;
    })
    .catch((error) => {
      console.error("Error fetching data: ", error);
    });
};

const deleteCustomer = async (customer_id) => {
  let text = "Are you sure you want to delete data?";
  if (confirm(text) == true) {
    try {
      const customerId = { id: customer_id };
      const response = await axios.delete(
        import.meta.env.VITE_API_URL + `customer/${customer_id}`,
        {
          headers: {
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      toast.add({
        severity: "success",
        summary: "Success Message",
        detail: "Data successfully deleted!",
        life: 5000,
      });
    } catch (error) {
      console.log(error);
      toast.add({
        severity: "error",
        summary: "Error Message",
        detail: "Data cannot be deleted because it is used in another field!",
        life: 5000,
      });
    }

    fetchCustomer();
  }
};

const fetchCustomer = async () => {
  const response = await axios
    .get(import.meta.env.VITE_API_URL + "customer")
    .then((data) => {
      customerList.value = data.data.data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
  searchList = customerList;
  currList.value = _.cloneDeep(searchList.value);
  searchInput.value = "";
};

const validate = () => {
  valid = false;
  if (
    customerForm.value.customer_name == "" ||
    customerForm.value.customer_fullname == "" ||
    customerForm.value.customer_field == "" ||
    customerForm.value.employee == ""
  ) {
    valid = false;
  } else {
    valid = true;
  }
};

const submitCustomer = async () => {
  validate();
  if (valid == false) {
    toast.add({
      severity: "warn",
      summary: "Warn Message",
      detail: "Please fill all the required field!",
      life: 5000,
    });
    return;
  }
  if (customerForm.value.customer_id == "") {
    try {
      const response = await axios.post(
        import.meta.env.VITE_API_URL + "customer",
        customerForm.value,
        {
          headers: {
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      toast.add({
        severity: "success",
        summary: "Success Message",
        detail: "Data successfully added!",
        life: 5000,
      });
    } catch (error) {
      console.log(error);
    }
  } else {
    try {
      const response = await axios.patch(
        import.meta.env.VITE_API_URL +
          `customer/${customerForm.value.customer_id}`,
        customerForm.value,
        {
          headers: {
            "user-token": JSON.parse(localStorage.getItem("pocketbase_auth"))
              .token,
          },
        },
      );
    } catch (error) {
      console.log(error);
    }
  }

  showModal.value = false;
  fetchCustomer();
};

onMounted(async () => {
  await fetchCustomer();
});
</script>

<style scoped>
table td {
  @apply py-2 px-6;
}

.asd {
  @apply border-red-500;
}

h1 {
  @apply text-[#908c13] font-semibold text-2xl mb-4;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.25s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.complete {
  @apply bg-[hsl(58,46%,75%)];
}
</style>
