<template>
  <div class="w-full">
    <h1 class="text-[#908c13] font-semibold text-3xl mb-12">Contract List</h1>

    <div class="flex justify-between items-start">
      <div class="flex gap-4">
        <ExportData />
        <!-- <ImportData /> -->
      </div>

      <div class="flex items-start gap-4">
        <div v-show="filterBox" class="text-sm flex flex-col">
          <div class="flex flex-col min-w-[275px] items-start">
            <Dropdown
              filter
              v-model="salesPerson"
              showClear
              :options="salesList.data"
              optionLabel="username"
              class="inputBox py-2"
              placeholder="Sales Person"
              id="dropdown"
              pt:input:class="p-0 text-sm text-gray-500"
              pt:clearIcon:class="text-gray-500"
              pt:trigger:class="text-black"
              v-on:change="filterSales"
            />
          </div>
          <div class="flex flex-col items-start">
            <Dropdown
              v-model="status"
              showClear
              :options="statusList"
              placeholder="Status"
              i
              d="dropdown"
              pt:input:class="p-0 text-sm text-gray-500"
              pt:clearIcon:class="text-gray-500 "
              pt:trigger:class="text-black"
              class="inputBox py-2"
              v-on:change="filterStatus"
            />
          </div>
        </div>

        <div class="flex gap-4 items-center">
          <i
            class="pi pi-filter text-[#908c13] text-xl cursor-pointer"
            v-on:click="showFilter"
          ></i>

          <div class="flex gap-2">
            <Dropdown
              v-model="searchType"
              :options="searchTypeList"
              placeholder="Search Category"
              pt:input:class="p-0 text-sm"
              pt:clearIcon:class="text-black"
              pt:trigger:class="text-black"
              class="inputBox min-w-[200px]"
            />
            <IconField iconPosition="right" class="min-w-[250px]">
              <InputIcon>
                <i class="pi pi-search" />
              </InputIcon>
              <input
                type="text"
                class="inputBox"
                placeholder="Search..."
                v-model="searchInput"
              />
            </IconField>
          </div>
        </div>
      </div>
    </div>

    <div
      class="h-[250px] bg-slate-100 flex items-center gap-4 justify-center"
      v-if="loading"
    >
      <LoaderCircle class="h-8 w-8 text-[#908c13] animate-spin" />
      Loading Data
    </div>

    <div class="card" v-if="userStore.role == 'Helpdesk'">
      <DataTable
        :value="contractList"
        tableStyle="min-width: 100%"
        removableSort
        paginator
        :rows="10"
        :rowsPerPageOptions="[10, 25, 50, 100]"
      >
        <template #empty>
          <div
            class="h-[250px] flex items-center justify-center text-slate-400"
          >
            No contracts found...
          </div>
        </template>

        <Column>
          <template #body="slotProps">
            <span
              class="w-3 h-3 self-center inline-block rounded-[50%]"
              :class="{
                'bg-green-500': slotProps.data.status === 'Ongoing',
                'bg-red-500': slotProps.data.status === 'Expired',
              }"
            ></span>
          </template>
        </Column>
        <Column
          field="customer_name"
          header="Customer Name"
          sortable
          pt:sortIcon:class="text-white"
        />
        <Column field="product_name" header="Product Name" sortable></Column>
        <Column field="project_name" header="Project Name" sortable></Column>
        <Column field="sales_person" header="Sales Person" sortable></Column>
        <Column field="status" header="Status" sortable></Column>
        <Column header="">
          <template #body="slotProps">
            <div class="flex">
              <router-link
                :to="{ path: `contracts/${slotProps.data.project_id}` }"
              >
                <div class="flex gap-4 justify-center cursor-pointer">
                  <i
                    class="pi pi-info-circle text-[#908c13]"
                    v-tooltip.left="{
                      value: 'Contract Detail',
                      showDelay: 500,
                      hideDelay: 200,
                    }"
                  ></i>
                </div>
              </router-link>
            </div>
          </template>
        </Column>
      </DataTable>
    </div>

    <div class="card w-full" v-else>
      <DataTable
        :value="contractList"
        resizableColumns
        removableSort
        paginator
        :class="{ hidden: loading, block: !loading }"
        :rows="10"
        :rowsPerPageOptions="[10, 25, 50, 100]"
      >
        <template #empty>
          <div
            class="h-[250px] flex items-center justify-center text-slate-400"
          >
            No contracts found...
          </div>
        </template>

        <Column>
          <template #body="slotProps">
            <span
              class="w-3 h-3 self-center inline-block rounded-[50%]"
              :class="{
                'bg-gray-400': slotProps.data.project_status === 'Draft',
                'bg-yellow-500': slotProps.data.project_status === 'Pending',
                'bg-green-500': slotProps.data.project_status === 'Approved',
                'bg-red-500': slotProps.data.project_status === 'Rejected',
              }"
            ></span>
          </template>
        </Column>
        <Column
          field="customer_name"
          header="Customer Name"
          sortable
          pt:sortIcon:class="text-white"
        ></Column>
        <Column field="costsheet" header="Cost Sheet" sortable></Column>
        <Column field="sales_person" header="Sales Person" sortable></Column>
        <Column field="project_name" header="Project Name" sortable></Column>
        <Column field="product" header="Products" sortable></Column>
        <Column field="project_status" header="Status" sortable></Column>
        <Column header="">
          <template #body="slotProps">
            <div class="flex">
              <router-link
                :to="{ path: `contracts/${slotProps.data.project_id}` }"
              >
                <div class="flex gap-4 justify-center cursor-pointer">
                  <i
                    class="pi pi-info-circle text-[#908c13]"
                    v-tooltip.left="{
                      value: 'Contract Detail',
                      showDelay: 500,
                      hideDelay: 200,
                    }"
                  ></i>
                </div>
              </router-link>
              <!-- <div class="flex gap-4 justify-center cursor-pointer">
                <i class="pi pi-clone text-[#908c13]"></i>
              </div> -->
            </div>
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
</template>

<script setup>
import _ from "lodash";
import axios from "axios";
import { onMounted } from "vue";
import { ref, watch } from "vue";
import "primeicons/primeicons.css";
import Column from "primevue/column";
import Dropdown from "primevue/dropdown";
import { userManagement } from "../pinia";
import DataTable from "primevue/datatable";
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";
import ExportData from "../components/PageComponents/Contracts/ExportData.vue";
import ImportData from "../components/PageComponents/Contracts/ImportData.vue";
import { LoaderCircle } from "lucide-vue-next";

const userStore = userManagement();

const searchInput = ref("");
const searchType = ref("Customer Name");
const statusList = ["Approved", "Draft", "Pending", "Rejected"];
const searchTypeList = ["Customer Name", "Cost Sheet", "Project Name"];

const status = ref();
const salesPerson = ref();

let contracts;
let searchList;
let loading = true;
let filterSalesList;
let filterStatusList;
let salesList = ref([{}]);
let filterBox = ref(false);
let contractList = ref([{}]);

const showFilter = () => {
  filterBox.value = !filterBox.value;
};

const filterSales = () => {
  if (salesPerson.value == null) {
    filterSalesList = contracts;
    contractList.value = _.cloneDeep(filterSalesList);
  } else {
    filterSalesList = contracts.filter((contract) =>
      contract.sales_person.includes(salesPerson.value.username),
    );
  }
  const intersection = _.intersection(
    searchList,
    filterSalesList,
    filterStatusList,
  );
  contractList.value = _.cloneDeep(intersection);
};

const filterStatus = () => {
  if (status.value == null) {
    filterStatusList = contracts;
    contractList.value = _.cloneDeep(filterStatusList);
  } else {
    filterStatusList = contracts.filter((contract) =>
      contract.project_status.includes(status.value),
    );
  }
  const intersection = _.intersection(
    searchList,
    filterSalesList,
    filterStatusList,
  );
  contractList.value = _.cloneDeep(intersection);
};

watch(searchType, (x) => {
  searchInput.value = "";
});

watch(searchInput, (x) => {
  if (searchInput.value == "") {
    searchList = contracts;
    contractList.value = _.cloneDeep(searchList);
  } else {
    if (searchType.value == "Customer Name") {
      searchList = contracts.filter((contract) =>
        contract.customer_name
          .toLowerCase()
          .includes(searchInput.value.toLowerCase()),
      );
    } else if (searchType.value == "Cost Sheet") {
      searchList = contracts.filter((contract) =>
        contract.costsheet
          .toLowerCase()
          .includes(searchInput.value.toLowerCase()),
      );
    } else {
      searchList = contracts.filter((contract) =>
        contract.project_name
          .toLowerCase()
          .includes(searchInput.value.toLowerCase()),
      );
    }
  }
  const intersection = _.intersection(
    searchList,
    filterSalesList,
    filterStatusList,
  );
  contractList.value = _.cloneDeep(intersection);
});

const getSales = async () => {
  await axios
    .get(import.meta.env.VITE_API_URL + `user`)
    .then((data) => {
      salesList.value = data.data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
};

const getProjectList = async () => {
  try {
    const response = await axios.get(import.meta.env.VITE_API_URL + "project", {
      headers: {
        user: userStore.db_id,
      },
    });

    contracts = response.data.data;
    searchList = contracts;
    filterSalesList = contracts;
    filterStatusList = contracts;
    contractList.value = _.cloneDeep(contracts);
    loading = false;
  } catch (e) {
    console.error("Error fetching data:", error);
  }
};

const getProductList = async () => {
  try {
    const response = await axios.get(import.meta.env.VITE_API_URL + "product");
    contracts = response.data.data;
    searchList = contracts;
    filterSalesList = contracts;
    filterStatusList = contracts;
    contractList.value = _.cloneDeep(contracts);
    loading = false;
  } catch (e) {
    console.log(e);
  }
};

const getListDec = async () => {
  if (userStore.role == "Helpdesk") {
    await getProductList();
    return;
  } else {
    await getProjectList();
    return;
  }
};

onMounted(async () => {
  await getSales();
  await getListDec();
});
</script>
