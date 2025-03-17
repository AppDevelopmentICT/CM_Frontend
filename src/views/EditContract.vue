<template>
  <div>
    <div class="group">
      <div class="flex justify-between items-center mb-4">
        <h1>Contract Edit</h1>
      </div>
      <div class="grid grid-cols-2 gap-x-4">
        <div class="subgroup">
          <h2>Project Information</h2>
          <div class="mb-2">
            <label for="" class="block"
              >Customer Name<span class="text-red-600">*</span></label
            >
            <Dropdown
              v-model="customerObj"
              editable
              filter
              :options="customerList.data"
              optionLabel="customer_name"
              placeholder=""
              id="dropdown"
              pt:input:class="p-0 text-sm"
              pt:clearIcon:class="text-black"
              pt:trigger:class="text-black"
              class="inputBox"
              v-on:blur="addCustomer"
            />
          </div>

          <div class="">
            <label for="" class="block"
              >Sales Person<span class="text-red-600">*</span></label
            >
            <Dropdown
              v-model="salesObj"
              filter
              :options="salesList.data"
              optionLabel="username"
              placeholder=""
              id="dropdown"
              pt:input:class="p-0 text-sm"
              pt:clearIcon:class="text-black"
              pt:trigger:class="text-black"
              class="inputBox"
            />
          </div>

          <div class="">
            <label for="" class="block"
              >Cost Sheet<span class="text-red-600">*</span></label
            >
            <input
              type="text"
              class="inputBox"
              v-model="projectDetail.cost_sheets"
            />
          </div>

          <div class="">
            <label for="" class="block"
              >Project Name<span class="text-red-600">*</span></label
            >
            <input
              type="text"
              class="inputBox"
              :autofocus="isDuplicate"
              v-model="projectDetail.project_name"
            />
          </div>
        </div>
        <div>
          <div class="subgroup">
            <h2>Contract Description</h2>
            <div class="grid grid-cols-2 gap-x-6">
              <div class="">
                <label for="" class="block"
                  >Type<span class="text-red-600">*</span></label
                >
                <Dropdown
                  v-model="projectDetail.project_type"
                  :options="contractTypeList"
                  placeholder=""
                  id="dropdown"
                  pt:input:class="p-0 text-sm"
                  pt:clearIcon:class="text-black"
                  pt:trigger:class="text-black"
                  class="inputBox"
                />
              </div>
              <div class="">
                <label for="" class="block"
                  >PO/Contract Number<span class="text-red-600">*</span></label
                >
                <input
                  type="text"
                  class="inputBox"
                  v-model="projectDetail.contract_number"
                />
              </div>
              <div>
                <label for="onSiteEngineer"
                  >Managed Service<span class="text-red-600"></span
                ></label>
                <br />
                <input
                  id="onSiteEngineer"
                  type="checkbox"
                  v-model="projectDetail.on_site_engineer"
                />
              </div>
              <!-- <div v-for="file in finalFileList" :key="file" >{{file.name}}</div> -->
            </div>
          </div>
          <div class="subgroup">
            <h2>Cost Information</h2>
            <div class="">
              <div class="">
                <label for="" class="block"
                  >Amount Reserve for Internal Cost<span class="text-red-600"
                    >*</span
                  ></label
                >
                <div class="flex">
                  <span class="bg-gray-400 text-gray-200 rounded-sm p-2 my-2"
                    >Rp.</span
                  >
                  <InputNumber
                    class="w-full p-0 self-center focus:outline-none rounded-none text-sm"
                    v-model="projectDetail.internal_cost"
                    inputId="integeronly"
                  />
                </div>
              </div>

              <div class="">
                <label for="" class="block"
                  >Selling Price<span class="text-red-600">*</span></label
                >
                <div class="flex">
                  <span class="bg-gray-400 text-gray-200 rounded-sm p-2 my-2"
                    >Rp.</span
                  >
                  <InputNumber
                    class="w-full p-0 self-center focus:outline-none rounded-none text-sm"
                    v-model="projectDetail.selling_prices"
                    inputId="integeronly"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="subgroup w-full h-fit">
          <PM v-model:pm="pm" v-if="!loadingPM" />
        </div>
        <div class="subgroup w-full h-fit">
          <CM v-model:cm="cm" v-if="!loadingCM" />
        </div>
      </div>
      <div class="flex gap-4">
        <div class="subgroup w-1/3 h-fit">
          <Implementation
            v-model:implementation="implementation"
            v-if="!loadingImple"
          />
        </div>
        <div class="subgroup w-full">
          <SLA v-model:sla="sla" />
        </div>
      </div>
      <div class="subgroup">
        <div class="flex justify-between pb-4">
          <h2>Product Info</h2>
          <button
            class="bg-[#908c13] text-white py-2 px-4 rounded-xl"
            v-on:click="showProductDetail('')"
          >
            <i class="pi pi-plus pr-2"></i>Add New Product
          </button>
        </div>
        <table class="min-w-full" v-if="productInfo.length != 0">
          <thead class="w-full table table-fixed">
            <tr>
              <th>Product</th>
              <th>Principal</th>
              <th>Product Name</th>
              <th>Serial Number</th>
              <th>SI Number</th>
              <th>Quantity</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tbody class="min-w-full overflow-y-auto block max-h-96">
            <tr
              v-for="(product, index) in productInfo"
              v-on:click="showProductDetail(product.product_id)"
              :key="product.product_id"
              class="bg-white border-b cursor-pointer transition duration-300 ease-in-out hover:bg-gray-200 w-full table table-fixed"
              :class="{
                'bg-yellow-300 hover:bg-yellow-400':
                  product.serial_number == '' || product.si_number == '',
              }"
            >
              <td>{{ product.product_category }}</td>
              <td class="truncate text-ellipsis">
                {{ product.principal_name }}
              </td>
              <td class="truncate text-ellipsis">{{ product.product_name }}</td>
              <td>{{ product.serial_number }}</td>
              <td>{{ product.si_number }}</td>
              <td>{{ product.quantity }}</td>
              <td>
                <button
                  class="pi pi-trash"
                  v-on:click="deleteProduct(product.product_id)"
                ></button>
              </td>
            </tr>
          </tbody>
        </table>
        <div v-else class="flex justify-center">
          <h3 class="text-[#a1a1a1] font-semibold text-xl">
            NO PRODUCTS ADDED
          </h3>
        </div>
      </div>

      <div class="subgroup">
        <h2>Additional Information</h2>
        <div class="grid grid-cols-2 gap-x-4">
          <div class="">
            <label for="" class="block">Description</label>
            <textarea
              name=""
              id=""
              class="border border-slate-200 rounded-sm my-2 w-full min-h-24 p-2 text-sm"
              v-model="projectDetail.description"
            ></textarea>
          </div>
          <div class="">
            <label for="" class="block">Attachment File</label>
            <div
              class="fileUpload"
              @dragenter.prevent="toggleActive"
              @dragleave.prevent="toggleActive"
              @dragover.prevent
              @drop.prevent="drop"
              :class="{ 'active-dropzone': active }"
            >
              <label for="upload" class="">
                <p
                  class="text-lg font-normal bg-[#bbbbbb2d] p-4 rounded-lg hover:bg-[#908c13] hover:text-white transition ease-in-out duration-200"
                >
                  Add New File (Max 5 files)
                </p>
              </label>
              <input
                type="file"
                id="upload"
                class="testFile"
                multiple
                v-on:change="uploadFile"
                accept=".doc,.docx,.pdf,.pptx,.xlsx,.jpg,.jpeg,.png"
              />
              <div
                id="fileList"
                class="flex flex-col items-center justify-center w-full min-h-16 text-gray-500 rounded-xl"
                v-show="finalFileList.length != 0"
              >
                <pre class="output">Selected files:</pre>
                <ul>
                  <li
                    v-for="test in finalFileList"
                    class="text-base font-normal pb-2 pl-4"
                    :key="test.name"
                  >
                    <div @click.stop="" class="flex flex-row">
                      <p class="text-wrap break-words break-all basis-5/6">
                        {{ test.name }}
                      </p>
                      <div class="basis-1/6 content-center">
                        <button
                          class="rounded-md bg-red-600 text-white px-2 mx-4"
                          @click.self="deleteFile(test)"
                        >
                          delete
                        </button>
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
    </div>
    <div class="w-full flex justify-end gap-2">
      <button
        v-if="projectDetail.project_status == 'Draft'"
        class="bg-[#908c13] p-2 w-32 text-white rounded-md"
        @click="saveContract((status = 'Draft'))"
      >
        Save Draft
      </button>
      <button
        class="bg-green-500 p-2 w-24 text-white rounded-md"
        @click="saveContract((status = 'Pending'))"
      >
        Submit
      </button>
    </div>
  </div>

  <div>
    <AddProduct
      v-model:showAddProduct="showAddProduct"
      v-model:productDetail="productDetail"
      v-if="showAddProduct"
      v-model:successAdd="successAdd"
      v-model:reopen="reopen"
    />
  </div>
  <div>
    <ProductDetail
      v-model:productDetail="productDetail"
      v-model:showDetail="showDetail"
    />
  </div>
  <Toast />
  <div
    class="fixed inset-0 flex flex-col items-center justify-center bg-gray-500 bg-opacity-30"
    v-if="loading"
  >
    <ProgressSpinner class="w-[200px] h-[200px]" />
    <p class="!text-[#908c13] !text-3xl !font-bold">Loading</p>
  </div>
</template>

<script setup>
import ProgressSpinner from "primevue/progressspinner";
import { useRoute, useRouter } from "vue-router";
import { onMounted, onUpdated, watch, computed } from "vue";
import { ref } from "vue";
import axios from "axios";
import jsonData from "../assets/data.json";
import InputNumber from "primevue/inputnumber";
import ProductDetail from "../components/ProductDetail.vue";
import Implementation from "../components/Implementation.vue";
import SLA from "../components/SLA.vue";
import PocketBase from "pocketbase";
import { userManagement } from "../pinia";
import { useToast } from "primevue/usetoast";
import Dropdown from "primevue/dropdown";
import { defineAsyncComponent } from "vue";

var status = "";
var valid = false;

const AddProduct = defineAsyncComponent(
  () => import("../components/AddProduct.vue"),
);
const CM = defineAsyncComponent(
  () => import("../components/CorrectiveMaintenance.vue"),
);
const PM = defineAsyncComponent(
  () => import("../components/PreventiveMaintenance.vue"),
);

const toast = useToast();
const loadingPM = ref(true);
const loadingCM = ref(true);
const loadingImple = ref(true);
const loading = ref(false);
const isDuplicate = ref(false);

var pm = ref({});
var cm = ref({});
var sla = ref({});
var implementation = ref({});

const pb = new PocketBase(import.meta.env.VITE_PB_BASEURL);
const userStore = userManagement();

const route = useRoute();
const router = useRouter();

var dupe = false;
var fileUpload = [];
var finalFileList = ref([]);
const active = ref(false);

var projectDetail = ref({});

var productInfo = ref([{}]);
let showAddProduct = ref(false);
let successAdd = ref(false);
let reopen = ref(false);

let productModal = ref(false);
let productDetail = ref({});
let showDetail = ref(false);

let brandList = ref([{}]);
let customerList = ref([{}]);
let salesList = ref([{}]);

let customerObj = ref({});
let salesObj = ref({});

const contractTypeList = ["Contract", "Purchase Order", "SPK", "Other"];

const deleteProduct = async (product_id) => {
  try {
    const response = await axios.delete(
      import.meta.env.VITE_API_URL + `product/${product_id}`,
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
      detail: "Success delete product",
      life: 5000,
    });
    showAddProduct.value = !showAddProduct.value;
    location.reload();
  } catch (error) {
    toast.add({
      severity: "Error",
      summary: "Failed Message",
      detail: "Failed delete product",
      life: 5000,
    });
  }
};

const addCustomer = async () => {
  if (typeof customerObj.value == "string" && customerObj.value != "") {
    var checkExist = customerList.value.data.find(
      ({ customer_name }) =>
        customer_name.toLowerCase() === customerObj.value.toLowerCase(),
    );
    if (checkExist != undefined) {
      console.log("ada");
      customerObj.value = checkExist;
    } else {
      let text = "New entry!\nDo you want to create new data?";
      if (confirm(text) == true) {
        const testCustomer = {
          customer_name: customerObj.value,
          customer_fullname: "",
          customer_field: "",
          employee: "",
        };
        try {
          const response = await axios.post(
            import.meta.env.VITE_API_URL + "customer",
            testCustomer,
            {
              headers: {
                "user-token": JSON.parse(
                  localStorage.getItem("new_token"),
                ).token,
              },
            },
          );
          getCustomer();
        } catch (error) {}
      } else {
        customerObj.value = customerList.value.data.find(
          ({ customer_id }) => customer_id === projectDetail.value.customer_id,
        );
      }
    }
  }
};

const toggleAddProduct = () => {
  showAddProduct.value = !showAddProduct.value;
};

const showProductDetail = (id) => {
  const newProduct = {
    product_id: "",
    project_id: "",
    product_category: "",
    product_name: "",
    principal_id: "",
    serial_number: "",
    si_number: "",
    quantity: "",
    isImplementation: false,
    start_date: "",
    end_date: "",
    corrective_maintenance: {
      cm_by: "",
      start_date: new Date(0),
      end_date: new Date(0),
      quantity: "",
    },
    preventive_maintenance: {
      pm_by: "",
      start_date: new Date(0),
      end_date: new Date(0),
      pm_periode: "",
      quantity: "",
    },
    sla: {
      sla_id: "",
      severity_1_resolution_time: "",
      severity_1_response_time: "",
      severity_2_resolution_time: "",
      severity_2_response_time: "",
      severity_3_resolution_time: "",
      severity_3_response_time: "",
      severity_4_resolution_time: "",
      severity_4_response_time: "",
    },
    implementation: {
      implementation_id: "",
      implementation_type: "",
      start_date: new Date(0),
      end_date: new Date(0),
    },
  };

  if (id == "") {
    productDetail.value = newProduct;
    productDetail.value.project_id = projectDetail.value.project_id;
  } else {
    productDetail.value = productInfo.value.find(
      ({ product_id }) => product_id === id,
    );
    productDetail.value.project_id = route.params.id;
    if (productDetail.value.corrective_maintenance.start_date == "1970-01-01") {
      productDetail.value.corrective_maintenance.start_date = new Date(0);
    }
    if (productDetail.value.corrective_maintenance.end_date == "1970-01-01") {
      productDetail.value.corrective_maintenance.end_date = new Date(0);
    }
    if (productDetail.value.preventive_maintenance.start_date == "1970-01-01") {
      productDetail.value.preventive_maintenance.start_date = new Date(0);
    }
    if (productDetail.value.preventive_maintenance.end_date == "1970-01-01") {
      productDetail.value.preventive_maintenance.end_date = new Date(0);
    }
  }
  // productModal.value=true
  showAddProduct.value = true;
};

const toggleActive = () => {
  active.value = !active.value;
};

const drop = (e) => {
  fileUpload = e.dataTransfer.files;
  pushFile(fileUpload);
  toggleActive();
};

const uploadFile = async (e) => {
  e.preventDefault();

  fileUpload = document.querySelector(".testFile").files;
  pushFile(fileUpload);
};

const allowedExt = [
  "pdf",
  "xls",
  "xlsx",
  "png",
  "jpg",
  "jpeg",
  "doc",
  "docx",
  "ppt",
  "pptx",
  "csv",
];

const pushFile = (fileUpload) => {
  for (const file of fileUpload) {
    const extension = file.name.split(".").pop().toLowerCase();
    if (!allowedExt.includes(extension)) {
      alert("file type invalid");
      continue;
    }
    if (finalFileList.value.length >= 5) {
      alert("max file number reached");
      break;
    }
    for (const test of finalFileList.value) {
      if (test.name == file.name) {
        dupe = true;
        break;
      }
    }
    if (dupe == false) {
      finalFileList.value.push(file);

      // output.innerText += `\n${file.name}`
    }
    dupe = false;
  }
};

const deleteFile = async (file, e) => {
  let text =
    "Are you sure you want to delete this file?\n Action cannot be reversed";
  if (confirm(text) == true) {
    finalFileList.value.splice(finalFileList.value.indexOf(file), 1);
    await pb.collection("files").delete(file.id);
  }
};

const closeProductModal = () => {
  productModal.value = false;
};

watch(successAdd, async () => {
  const result = [{}];
  var response = await axios
    .get(import.meta.env.VITE_API_URL + `project/${route.params.id}`)
    .then((data) => {
      result.value = data.data;
      projectDetail.value = result.value.data;
      productInfo.value = result.value.data.product_info;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      // Handle errors appropriately
    });
});

watch(reopen, () => {
  console.log(reopen.value);

  if (reopen.value == true) {
    setTimeout(() => {
      showProductDetail("");
    }, 300);
  }
});

const getFile = async () => {
  const record = await pb
    .collection("files")
    .getList(1, 5, {
      filter: `project_id="${route.params.id}"`,
    })
    .then((data) => {
      for (let i in data.items) {
        let test = {
          name: data.items[i].contract_file[0],
          id: data.items[i].id,
        };
        finalFileList.value.push(test);
      }
    });
};

const getSLA = async () => {
  const result = [{}];
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `maintenance/sla`, {
      headers: {
        "project-id": route.params.id,
      },
    })
    .then((data) => {
      result.value = data.data;
      sla.value = result.value.data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
};

const getPM = async () => {
  const result = [{}];
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `maintenance/pm`, {
      headers: {
        "project-id": route.params.id,
      },
    })
    .then((data) => {
      result.value = data.data;
      pm.value = result.value.data;
      loadingPM.value = false;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
};
const getImple = async () => {
  const result = [{}];
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `maintenance/implementation`, {
      headers: {
        "project-id": route.params.id,
      },
    })
    .then((data) => {
      result.value = data.data;
      implementation.value = result.value.data;
      loadingImple.value = false;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
};
const getCM = async () => {
  const result = [{}];
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `maintenance/cm`, {
      headers: {
        "project-id": route.params.id,
      },
    })
    .then((data) => {
      result.value = data.data;
      cm.value = result.value.data;
      loadingCM.value = false;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
};

const getCustomer = async () => {
  try {
    const response = await axios.get(import.meta.env.VITE_API_URL + `customer`);
    customerList.value = response.data;
    customerObj.value = customerList.value.data.find(
      ({ customer_id }) => customer_id === projectDetail.value.customer_id,
    );
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const fetchProjectDetails = async () => {
  try {
    const response = await axios.get(
      import.meta.env.VITE_API_URL + `project/${route.params.id}`,
    );
    const result = response.data;
    projectDetail.value = result.data;

    // Format numbers with dot as thousand separator
    const formatNumber = (number) => {
      return new Intl.NumberFormat("de-DE").format(number);
    };

    projectDetail.value.internal_cost_formatted = formatNumber(
      projectDetail.value.internal_cost,
    );
    projectDetail.value.selling_prices_formatted = formatNumber(
      projectDetail.value.selling_prices,
    );
    productInfo.value = result.data.product_info;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const getSales = async () => {
  try {
    const response = await axios.get(import.meta.env.VITE_API_URL + `user`);
    salesList.value = response.data;
    salesObj.value = salesList.value.data.find(
      ({ id }) => id === projectDetail.value.sales_person_id,
    );
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

onMounted(async () => {
  await fetchProjectDetails();
  await getSales();
  await getCustomer();
  await getFile();
  await getSLA();
  await getPM();
  await getCM();
  await getImple();
  await showToast();
});

const showToast = async () => {
  const temp = projectDetail.value.project_name.split("-");
  const isCopy = temp[temp.length - 1];
  if (isCopy === "copy") {
    toast.add({
      severity: "info",
      summary:
        "Please make sure to update your: \n- Project Name\n- Contract Number\n- Cost Sheet",
      detail:
        "Note: Information will disappear after complete the following information",
    });
    isDuplicate.value = true;
    return;
  }
};

const validate = () => {
  console.log(pm.value);
  // console.log(cm.value)
  // console.log(implementation.value)
  var checkPmQuantity = pm.value.quantity.split(" ");
  var checkCmQuantity = cm.value.quantity.split(" ");
  if (
    projectDetail.value.customer_name != "" &&
    projectDetail.value.cost_sheets != "" &&
    projectDetail.value.project_name != "" &&
    projectDetail.value.internal_cost != "" &&
    projectDetail.value.selling_prices != "" &&
    projectDetail.value.sales_person != "" &&
    projectDetail.value.project_type != "" &&
    projectDetail.value.contract_number != "" &&
    cm.value.cm_by != "" &&
    pm.value.pm_by != "" &&
    implementation.value.implementation_type != "" &&
    Object.values(sla.value).every((x) => x != "")
  ) {
    if (
      (cm.value.cm_by == "None" ||
        (cm.value.cm_by != "None" &&
          cm.value.start_date != "" &&
          cm.value.end_date != "" &&
          (cm.value.quantity.includes("Ticket") ||
            cm.value.quantity.includes("Man Days")))) &&
      (pm.value.pm_by == "None" ||
        (pm.value.pm_by != "None" &&
          pm.value.start_date != "" &&
          pm.value.end_date != "" &&
          pm.value.quantity != "" &&
          (pm.value.quantity.includes("Ticket") ||
            pm.value.quantity.includes("Man Days")))) &&
      (implementation.value.implementation_type == "None" ||
        (implementation.value.implementation_type != "None" &&
          implementation.value.start_date != "" &&
          implementation.value.end_date != "string"))
    ) {
      if (
        (cm.value.cm_by == "None" ||
          (checkCmQuantity.length > 1 && checkCmQuantity[1] != "")) &&
        (pm.value.pm_by == "None" ||
          (checkPmQuantity.length > 1 && checkPmQuantity[1] != ""))
      ) {
        valid = true;
      }
    }
  } else {
    valid = false;
  }
};

const saveContract = async (status) => {
  loading.value = true;
  valid = false;
  validate();
  if (valid == false) {
    loading.value = false;
    toast.add({
      severity: "error",
      summary: "Error Message",
      detail: "Data incomplete",
      life: 3000,
    });
    return;
  }
  projectDetail.value.customer_id = customerObj.value.customer_id;
  projectDetail.value.sales_person_id = salesObj.value.id;
  const maintenance = {
    preventive_maintenance: pm.value,
    corrective_maintenance: cm.value,
    sla: sla.value,
    implementation: implementation.value,
  };
  try {
    projectDetail.value.project_status = status;
    projectDetail.value.sales_person = projectDetail.value.sales_person_id;
    console.log("asd");
    const projectResponse = await axios.patch(
      import.meta.env.VITE_API_URL + `project/${route.params.id}`,
      projectDetail.value,
      {
        headers: {
          "user-token": JSON.parse(localStorage.getItem("new_token"))
            .token,
        },
      },
    );
    console.log("asd");
    const maintenanceResponse = await axios.patch(
      import.meta.env.VITE_API_URL + "parent-maintenance",
      maintenance,
      {
        headers: {
          "user-token": JSON.parse(localStorage.getItem("new_token"))
            .token,
          "project-id": route.params.id,
        },
      },
    );
    console.log("asd");
    for (let i in finalFileList.value) {
      if (finalFileList.value[i].id == undefined) {
        const formData = new FormData();
        formData.append("contract_file", finalFileList._rawValue[i]);
        formData.append("project_id", route.params.id);
        try {
          const createdRecord = await pb.collection("files").create(formData);
        } catch (error) {
          toast.add({
            severity: "error",
            summary: "Error Message",
            detail: e.response.data.message,
            life: 5000,
          });
          loading.value = false;
          return;
        }
      }
    }
    loading.value = false;
    toast.add({
      severity: "success",
      summary: "Success Message",
      detail: "Data successfully added!",
      life: 5000,
    });
    setTimeout(() => {
      router.push(`/contracts/${route.params.id}`);
    }, 1000);
  } catch (e) {
    toast.add({
      severity: "error",
      summary: "Error Message",
      detail: e.response.data.message,
      life: 5000,
    });
    loading.value = false;
    return;
  }
};
</script>

<style lang="scss" scoped>
input[type="file"] {
  @apply hidden;
}
.inputNum::-webkit-outer-spin-button,
.inputNum::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
