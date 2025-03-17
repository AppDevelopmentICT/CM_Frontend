<template>
  <div>
    <div
      class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-60 z-20"
      v-if="showAddProduct"
    >
      <div class="bg-white rounded-sm p-12 w-[90%] h-[90%] overflow-auto group">
        <div class="group">
          <div class="flex justify-between items-center">
            <h1 class="">Add Product</h1>
            <button
              class="pi pi-times text-[#908c13] text-xl"
              v-on:click="closeForm"
            ></button>
          </div>

          <div class="subgroup">
            <h2>Product Detail</h2>
            <div class="grid grid-cols-2 gap-x-6 gap-y-4">
              <div class="">
                <label for="productType" class="block"
                  >Product Type<span class="text-red-600">*</span></label
                >
                <Dropdown
                  v-model="productObj"
                  editable
                  filter
                  :options="productList.data"
                  optionLabel="category"
                  placeholder=""
                  id="dropdown"
                  pt:input:class="p-0 text-sm"
                  pt:clearIcon:class="text-black"
                  pt:trigger:class="text-black"
                  class="inputBox"
                  v-on:blur="addType"
                />
              </div>

              <div class="">
                <label for="principal" class="block"
                  >Brand<span class="text-red-600">*</span></label
                >
                <Dropdown
                  v-model="principalObj"
                  editable
                  filter
                  :options="principalList.data"
                  optionLabel="principal_name"
                  placeholder=""
                  id="dropdown"
                  pt:input:class="p-0 text-sm"
                  pt:clearIcon:class="text-black"
                  pt:trigger:class="text-black"
                  class="inputBox"
                  v-on:blur="addPrincipal"
                />
              </div>

              <div class="">
                <label for="product_name" class="block"
                  >Product Name<span class="text-red-600">*</span></label
                >
                <input
                  type="text"
                  id="product_name"
                  class="inputBox"
                  v-model="productDetail.product_name"
                />
              </div>

              <div class="">
                <label for="serial_number" class="block"
                  >Serial Number<span class="text-red-600">*</span></label
                >
                <input
                  type="text"
                  id="serial_number"
                  autocomplete="off"
                  class="inputBox"
                  v-model="productDetail.serial_number"
                />
              </div>

              <div class="">
                <label for="si_number" class="block">SI Number</label>
                <input
                  type="text"
                  id="si_number"
                  class="inputBox"
                  autocomplete="off"
                  v-model="productDetail.si_number"
                />
              </div>

              <div class="">
                <label for="quantity" class="block"
                  >Quantity<span class="text-red-600">*</span></label
                >
                <input
                  type="number"
                  id="quantity"
                  autocomplete="off"
                  class="inputBox"
                  v-model="productDetail.quantity"
                />
              </div>

              <div class="">
                <label class="block"
                  >Start Date<span class="text-red-600">*</span></label
                >
                <input
                  type="date"
                  class="inputBox"
                  v-model="productDetail.start_date"
                />
              </div>

              <div class="">
                <label class="block"
                  >End Date<span class="text-red-600">*</span></label
                >
                <input
                  type="date"
                  class="inputBox"
                  v-model="productDetail.end_date"
                />
              </div>
            </div>
          </div>

          <div class="w-full gap-4 flex flex-row-reverse">
            <div class="subgroup w-full flex flex-col h-fit">
              <div class="flex justify-between">
                <h2 class="self-center">Corrective Maintenance</h2>
                <div class="flex flex-col cursor-pointer">
                  <label for="isCMParent">Same as contract</label>
                  <input
                    type="checkbox"
                    class="self-end"
                    id="isCMParent"
                    v-model="isCMParent"
                  />
                </div>
              </div>
              <div :class="{ 'readonly-container': isCMParent }">
                <label for="maintenanceBy" class="block"
                  >Maintenance By<span class="text-red-600">*</span></label
                >
                <Dropdown
                  v-model="CM.cm_by"
                  :options="CMList"
                  placeholder=""
                  id="dropdown"
                  pt:input:class="p-0 text-sm"
                  pt:clearIcon:class="text-black"
                  pt:trigger:class="text-black"
                  class="inputBox"
                />
              </div>
              <div
                v-if="
                  CM.cm_by != undefined && CM.cm_by != '' && CM.cm_by != 'None'
                "
                :class="{ 'readonly-container': isCMParent }"
              >
                <div class="flex justify-between w-full gap-2">
                  <div class="w-full">
                    <label class="block"
                      >Start Date<span class="text-red-600">*</span></label
                    >
                    <input
                      type="date"
                      class="inputBox"
                      v-model="CM.start_date"
                      :readonly="isCMParent"
                    />
                  </div>
                  <div class="w-full">
                    <label class="block"
                      >End Date<span class="text-red-600">*</span></label
                    >
                    <input
                      type="date"
                      class="inputBox"
                      v-model="CM.end_date"
                      :readonly="isCMParent"
                    />
                  </div>
                </div>
                <div class="flex flex-col w-full">
                  <label for="Quantity Input" class="block">Quantity</label>
                  <QuantityInput v-model:quantity="CM.quantity" />
                </div>
              </div>
            </div>

            <div class="subgroup w-full h-fit">
              <div class="flex justify-between">
                <h2 class="self-center">Preventive Maintenance</h2>
                <div class="flex flex-col cursor-pointer">
                  <label for="isPMParent">Same as contract</label>
                  <input
                    type="checkbox"
                    class="self-end"
                    id="isPMParent"
                    v-model="isPMParent"
                  />
                </div>
              </div>
              <div class="" :class="{ 'readonly-container': isPMParent }">
                <label for="maintenanceBy" class="block"
                  >Maintenance By<span class="text-red-600">*</span></label
                >
                <Dropdown
                  v-model="PM.pm_by"
                  :options="PMList"
                  placeholder=""
                  id="dropdown"
                  pt:input:class="p-0 text-sm"
                  pt:clearIcon:class="text-black"
                  pt:trigger:class="text-black"
                  class="inputBox"
                />
              </div>
              <div
                v-if="
                  PM.pm_by != undefined && PM.pm_by != '' && PM.pm_by != 'None'
                "
                :class="{ 'readonly-container': isPMParent }"
              >
                <div class="flex justify-between gap-2">
                  <div class="w-full">
                    <label for="" class="block"
                      >Start Date<span class="text-red-600">*</span></label
                    >
                    <input
                      type="date"
                      class="inputBox w-full"
                      :readonly="isPMParent"
                      v-model="PM.start_date"
                    />
                  </div>
                  <div class="w-full">
                    <label for="" class="block"
                      >End Date<span class="text-red-600">*</span></label
                    >
                    <input
                      type="date"
                      class="inputBox w-full"
                      :readonly="isPMParent"
                      v-model="PM.end_date"
                    />
                  </div>
                </div>
                <div class="flex gap-2 w-full">
                  <div class="flex flex-col w-full">
                    <label for="maintenancePeriod" class="block"
                      >Maintenance Period</label
                    >
                    <Dropdown
                      v-model="PM.pm_periode"
                      editable
                      filter
                      :options="periodList"
                      placeholder=""
                      id="dropdown"
                      pt:input:class="p-0 text-sm"
                      pt:clearIcon:class="text-black"
                      pt:trigger:class="text-black"
                      class="inputBox"
                    />
                  </div>
                  <div class="flex flex-col w-full">
                    <label for="Quantity Input" class="block">Quantity</label>
                    <QuantityInput v-model:quantity="PM.quantity" />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="subgroup">
            <div class="flex justify-between mb-3">
              <h2 class="self-center">SLA</h2>
              <div class="flex flex-col cursor-pointer">
                <label for="isSlaParent">Same as contract</label>
                <input
                  type="checkbox"
                  class="self-end"
                  id="isSlaParent"
                  v-model="isSlaParent"
                />
              </div>
            </div>
            <div
              class="flex flex-col gap-2"
              :class="{ 'readonly-container': isSlaParent }"
            >
              <div class="flex gap-4 items-center">
                <p class="text-gray-500 font-sans font-semibold text-base">
                  Severity 1
                </p>
                <div class="grid grid-cols-2 gap-4 flex-auto">
                  <div class="">
                    <label for="" class="block"
                      >Response Time<span class="text-red-600">*</span></label
                    >
                    <input
                      type="text"
                      :readonly="isSlaParent"
                      class="inputBox"
                      v-model="slaData.severity_1_response_time"
                    />
                  </div>
                  <div class="">
                    <label for="" class="block"
                      >Resolution Time<span class="text-red-600">*</span></label
                    >
                    <input
                      type="text"
                      :readonly="isSlaParent"
                      class="inputBox"
                      v-model="slaData.severity_1_resolution_time"
                    />
                  </div>
                </div>
              </div>
              <div class="flex gap-4 items-center">
                <p class="text-gray-500 font-sans font-semibold text-base">
                  Severity 2
                </p>
                <div class="grid grid-cols-2 gap-4 flex-auto">
                  <div class="">
                    <label for="" class="block"
                      >Response Time<span class="text-red-600">*</span></label
                    >
                    <input
                      type="text"
                      :readonly="isSlaParent"
                      class="inputBox"
                      v-model="slaData.severity_2_response_time"
                    />
                  </div>
                  <div class="">
                    <label for="" class="block"
                      >Resolution Time<span class="text-red-600">*</span></label
                    >
                    <input
                      type="text"
                      :readonly="isSlaParent"
                      class="inputBox"
                      v-model="slaData.severity_2_resolution_time"
                    />
                  </div>
                </div>
              </div>
              <div class="flex gap-4 items-center">
                <p class="text-gray-500 font-sans font-semibold text-base">
                  Severity 3
                </p>
                <div class="grid grid-cols-2 gap-4 flex-auto">
                  <div class="">
                    <label for="" class="block"
                      >Response Time<span class="text-red-600">*</span></label
                    >
                    <input
                      type="text"
                      :readonly="isSlaParent"
                      class="inputBox"
                      v-model="slaData.severity_3_response_time"
                    />
                  </div>
                  <div class="">
                    <label for="" class="block"
                      >Resolution Time<span class="text-red-600">*</span></label
                    >
                    <input
                      type="text"
                      :readonly="isSlaParent"
                      class="inputBox"
                      v-model="slaData.severity_3_resolution_time"
                    />
                  </div>
                </div>
              </div>
              <div class="flex gap-4 items-center">
                <p class="text-gray-500 font-sans font-semibold text-base">
                  Severity 4
                </p>
                <div class="grid grid-cols-2 gap-4 flex-auto">
                  <div class="">
                    <label for="" class="block"
                      >Response Time<span class="text-red-600">*</span></label
                    >
                    <input
                      type="text"
                      :readonly="isSlaParent"
                      class="inputBox"
                      v-model="slaData.severity_4_response_time"
                    />
                  </div>
                  <div class="">
                    <label for="" class="block"
                      >Resolution Time<span class="text-red-600">*</span></label
                    >
                    <input
                      type="text"
                      :readonly="isSlaParent"
                      class="inputBox"
                      v-model="slaData.severity_4_resolution_time"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="subgroup">
            <div class="float-right flex flex-col">
              <label for="isImlpementationParent">Same as contract</label>
              <input
                type="checkbox"
                class="self-end"
                id="isImlpementationParent"
                v-model="isImlpementationParent"
              />
            </div>
            <div :class="{ 'readonly-container': isImlpementationParent }">
              <Implementation
                v-model:implementation="implementation"
                v-if="!loadingImple"
              />
            </div>
          </div>
          <div class="flex gap-3">
            <button
              class="bg-orange-400 text-white p-2 rounded-md"
              v-on:click="saveNewProduct"
            >
              Save and New
            </button>
            <button
              class="bg-[#908c13] text-white p-2 rounded-md"
              v-on:click="saveProduct"
            >
              Save Product
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Toast />
</template>

<script setup>
import { onMounted, watch } from "vue";
import { ref } from "vue";
import axios from "axios";
import DurationInput from "../components/DurationInput.vue";
import { useToast } from "primevue/usetoast";
import { useRoute } from "vue-router";
import Dropdown from "primevue/dropdown";
import Implementation from "./Implementation.vue";
import { defineAsyncComponent } from "vue";

const QuantityInput = defineAsyncComponent(() => import("./QuantityInput.vue"));

const loadingImple = ref(true);

const route = useRoute();
const header = {
  headers: {
    "project-id": `${route.params.id}`,
    "user-token": JSON.parse(localStorage.getItem("new_token")).token,
  },
};
const toast = useToast();
const showAddProduct = defineModel("showAddProduct");
const productDetail = defineModel("productDetail");
const successAdd = defineModel("successAdd");
const reopen = defineModel("reopen");
var valid = false;

let productObj = ref();
let principalObj = ref();
let maintenanceProduct = ref();

const isPMParent = ref(false);
const isCMParent = ref(false);
const isSlaParent = ref(false);
const isImlpementationParent = ref(false);
const periodList = ref();

const getPeriode = async () => {
  try {
    const response = await axios.get(import.meta.env.VITE_API_URL + "periode");
    const periodeTemp = response.data.data;
    periodList.value = periodeTemp.map((periode, i) => periode.periode);
  } catch (e) {
    console.error(e);
  }
};

const addType = async () => {
  if (typeof productObj.value == "string" && productObj.value != "") {
    var checkExist = productList.value.data.find(
      ({ category }) =>
        category.toLowerCase() === productObj.value.toLowerCase(),
    );
    if (checkExist != undefined) {
      productObj.value = checkExist;
    } else {
      let text = "New entry!\nDo you want to create new data?";
      if (confirm(text) == true) {
        const testType = {
          category: productObj.value,
        };
        try {
          const response = await axios.post(
            import.meta.env.VITE_API_URL + "category",
            testType,
            {
              headers: {
                "user-token": JSON.parse(
                  localStorage.getItem("new_token"),
                ).token,
              },
            },
          );
          getProductCategory();
        } catch (error) {
          console.log(error);
        }
      } else {
        productObj.value = productList.value.data.find(
          ({ category }) => category === productDetail.value.product_category,
        );
      }
    }
  }
};

const addPrincipal = async () => {
  if (typeof principalObj.value == "string" && principalObj.value != "") {
    var checkExist = principalList.value.data.find(
      ({ principal_name }) =>
        principal_name.toLowerCase() === principalObj.value.toLowerCase(),
    );
    if (checkExist != undefined) {
      principalObj.value = checkExist;
    } else {
      let text = "New entry!\nDo you want to create new data?";
      if (confirm(text) == true) {
        const testPrincipal = {
          principal_name: principalObj.value,
        };
        try {
          const response = await axios.post(
            import.meta.env.VITE_API_URL + "principal",
            testPrincipal,
            {
              headers: {
                "user-token": JSON.parse(
                  localStorage.getItem("new_token"),
                ).token,
              },
            },
          );
          getPrincipal();
        } catch (error) {
          console.log(error);
        }
      } else {
        principalObj.value = principalList.value.data.find(
          ({ principal_id }) =>
            principal_id === productDetail.value.principal_id,
        );
      }
    }
  }
};

const closeForm = () => {
  showAddProduct.value = false;
  reopen.value = false;
};

const validate = () => {
  console.log(principalObj.value);
  if (
    productObj.value != undefined &&
    principalObj.value != undefined &&
    productDetail.value.product_name != "" &&
    productDetail.value.quantity != "" &&
    productDetail.value.start_date != "" &&
    productDetail.value.end_date != "" &&
    Object.values(slaData.value).every((x) => x != "")
  ) {
    if (
      (CM.value.cm_by == "None" ||
        (CM.value.cm_by != "None" &&
          CM.value.start_date != "" &&
          CM.value.end_date != "" &&
          (CM.value.quantity.includes("Ticket") ||
            CM.value.quantity.includes("Man Days")))) &&
      (PM.value.pm_by == "None" ||
        (PM.value.pm_by != "None" &&
          PM.value.start_date != "" &&
          PM.value.end_date != "" &&
          PM.value.pm_periode != "" &&
          (PM.value.quantity.includes("Ticket") ||
            PM.value.quantity.includes("Man Days")))) &&
      (implementation.value.implementation_type == "None" ||
        (implementation.value.implementation_type != "None" &&
          implementation.value.start_date != "" &&
          implementation.value.end_date != "string"))
    ) {
      valid = true;
      return;
    }
  }
  toast.add({
    severity: "warn",
    summary: "Warn Message",
    detail: "Please fill all the required field!",
    life: 5000,
  });
  valid = false;
  return;
};

const insertMaintenance = async () => {
  try {
    if (
      !isPMParent.value &&
      Object.values(PM.value).some(
        (key) => key !== "pm_id" && PM.value[key] !== "",
      )
    ) {
      productDetail.value.preventive_maintenance.is_parent = false;
      const pmResponse = await axios.post(
        import.meta.env.VITE_API_URL + "maintenance/pm",
        PM.value,
        header,
      );
      PM.value.pm_id = pmResponse.data.id;
    }

    if (
      !isCMParent.value &&
      Object.values(CM.value).some(
        (key) => key !== "cm_id" && CM.value[key] !== "",
      )
    ) {
      productDetail.value.corrective_maintenance.is_parent = false;
      const cmResponse = await axios.post(
        import.meta.env.VITE_API_URL + "maintenance/cm",
        CM.value,
        header,
      );
      CM.value.cm_id = cmResponse.data.id;
    }

    if (
      !isSlaParent.value &&
      Object.values(slaData.value).some(
        (key) => key !== "sla_id" && slaData.value[key] !== "",
      )
    ) {
      productDetail.value.sla.is_parent = false;
      const slaResponse = await axios.post(
        import.meta.env.VITE_API_URL + "maintenance/sla",
        slaData.value,
        header,
      );
      slaData.value.sla_id = slaResponse.data.id;
    }

    if (
      !isImlpementationParent.value &&
      Object.values(implementation.value).some(
        (key) =>
          key !== "implementation_id" && implementation.value[key] !== "",
      )
    ) {
      productDetail.value.implementation.is_parent = false;
      const implementationResponse = await axios.post(
        import.meta.env.VITE_API_URL + "maintenance/implementation",
        implementation.value,
        header,
      );
      implementation.value.implementation_id = implementationResponse.data.id;
    }
    return {
      pm_id: PM.value.pm_id,
      cm_id: CM.value.cm_id,
      sla_id: slaData.value.sla_id,
      implementation_id: implementation.value.implementation_id,
    };
  } catch (error) {
    console.log(error);
  }
};

const updateMaintenance = async () => {
  try {
    if (!isPMParent.value && PM.value.pm_id == parentPM.value.pm_id) {
      productDetail.value.preventive_maintenance.is_parent = false;
      const pmResponse = await axios.post(
        import.meta.env.VITE_API_URL + "maintenance/pm",
        PM.value,
        header,
      );
      PM.value.pm_id = pmResponse.data.id;
    }

    if (!isCMParent.value && CM.value.cm_id == parentCM.value.cm_id) {
      productDetail.value.corrective_maintenance.is_parent = false;
      const cmResponse = await axios.post(
        import.meta.env.VITE_API_URL + "maintenance/cm",
        CM.value,
        header,
      );
      CM.value.cm_id = cmResponse.data.id;
    }

    if (
      !isSlaParent.value &&
      slaData.value.sla_id == slaParentData.value.sla_id
    ) {
      productDetail.value.sla.is_parent = false;
      const slaResponse = await axios.post(
        import.meta.env.VITE_API_URL + "maintenance/sla",
        slaData.value,
        header,
      );
      slaData.value.sla_id = slaResponse.data.id;
    }

    if (
      !isImlpementationParent.value &&
      implementation.value.implementation_id ==
        implementationParent.value.implementation_id
    ) {
      productDetail.value.implementation.is_parent = false;
      const implementationResponse = await axios.post(
        import.meta.env.VITE_API_URL + "maintenance/implementation",
        implementation.value,
        header,
      );
      implementation.value.implementation_id = implementationResponse.data.id;
    }
    return {
      pm_id: PM.value.pm_id,
      cm_id: CM.value.cm_id,
      sla_id: slaData.value.sla_id,
      implementation_id: implementation.value.implementation_id,
    };
  } catch (error) {
    console.log(error);
  }
};

const saveProduct = async () => {
  reopen.value = false;
  validate();

  let toastMessage = "";
  if (valid == false) {
    return;
  }
  productDetail.value.product_category = productObj.value.category;
  productDetail.value.principal_id = principalObj.value.principal_id;
  if (productDetail.value.product_id == "") {
    await insertMaintenance();
    const projectId = productDetail.value.project_id;
    try {
      const response = await axios.post(
        import.meta.env.VITE_API_URL + `product/project/${projectId}`,
        productDetail.value,
        {
          headers: {
            "project-id": `${route.params.id}`,
            "project-name": `${route.params.id}`,
            "pm-id": `${PM.value.pm_id}`,
            "cm-id": `${CM.value.cm_id}`,
            "sla-id": `${slaData.value.sla_id}`,
            "implementation-id": `${implementation.value.implementation_id}`,
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      toastMessage = response.data.message;
    } catch (error) {
      toast.add({
        severity: "Error",
        summary: "Failed Message",
        detail: "Failed add product",
        life: 5000,
      });
    }
    toast.add({
      severity: "success",
      summary: "Success Message",
      detail: toastMessage,
      life: 5000,
    });
  } else {
    const maintenance_id = await updateMaintenance();
    productDetail.value.start_date = productDetail.value.start_date;
    productDetail.value.end_date = productDetail.value.end_date;
    productDetail.value.preventive_maintenance = PM.value;
    productDetail.value.corrective_maintenance = CM.value;
    productDetail.value.implementation = implementation.value;
    productDetail.value.sla = slaData.value;

    maintenanceProduct.value = {
      preventive_maintenance: PM.value,
      corrective_maintenance: CM.value,
      sla: slaData.value,
      implementation: implementation.value,
    };
    try {
      const response = await axios.patch(
        import.meta.env.VITE_API_URL +
          `product/${productDetail.value.product_id}`,
        productDetail.value,
        {
          headers: {
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      const maintenenaceResponse = await axios.patch(
        import.meta.env.VITE_API_URL + "maintenance",
        maintenanceProduct.value,
        {
          headers: {
            "project-id": `${route.params.id}`,
            "pm-id": `${maintenance_id.pm_id}`,
            "cm-id": `${maintenance_id.cm_id}`,
            "sla-id": `${maintenance_id.sla_id}`,
            "implementation-id": `${maintenance_id.implementation_id}`,
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      toastMessage = response.data.message;
    } catch (error) {
      console.log(error);
      toast.add({
        severity: "warn",
        summary: "Warn Message",
        detail: "Failed update product",
        life: 5000,
      });
    }
    toast.add({
      severity: "info",
      summary: "Info Message",
      detail: toastMessage,
      life: 5000,
    });
  }
  successAdd.value = !successAdd.value;
  reopen.value = false;
  showAddProduct.value = !showAddProduct.value;
};

const saveNewProduct = async () => {
  validate();

  let toastMessage = "";
  if (valid == false) {
    return;
  }
  productDetail.value.product_category = productObj.value.category;
  productDetail.value.principal_id = principalObj.value.principal_id;

  if (productDetail.value.product_id == "") {
    await insertMaintenance();
    const projectId = productDetail.value.project_id;
    try {
      const response = await axios.post(
        import.meta.env.VITE_API_URL + `product/project/${projectId}`,
        productDetail.value,
        {
          headers: {
            "project-id": `${route.params.id}`,
            "project-name": `${route.params.id}`,
            "pm-id": `${PM.value.pm_id}`,
            "cm-id": `${CM.value.cm_id}`,
            "sla-id": `${slaData.value.sla_id}`,
            "implementation-id": `${implementation.value.implementation_id}`,
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      toastMessage = response.data.message;
    } catch (error) {
      console.log(error);
      toast.add({
        severity: "Error",
        summary: "Failed Message",
        detail: "Failed add product",
        life: 5000,
      });
    }
    toast.add({
      severity: "success",
      summary: "Success Message",
      detail: toastMessage,
      life: 5000,
    });
  } else {
    const maintenance_id = await updateMaintenance();
    productDetail.value.start_date = productDetail.value.start_date;
    productDetail.value.end_date = productDetail.value.end_date;
    productDetail.value.preventive_maintenance = PM.value;
    productDetail.value.corrective_maintenance = CM.value;
    productDetail.value.implementation = implementation.value;
    productDetail.value.sla = slaData.value;

    maintenanceProduct.value = {
      preventive_maintenance: PM.value,
      corrective_maintenance: CM.value,
      sla: slaData.value,
      implementation: implementation.value,
    };
    try {
      const response = await axios.patch(
        import.meta.env.VITE_API_URL +
          `product/${productDetail.value.product_id}`,
        productDetail.value,
        {
          headers: {
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      const maintenenaceResponse = await axios.patch(
        import.meta.env.VITE_API_URL + "maintenance",
        maintenanceProduct.value,
        {
          headers: {
            "project-id": `${route.params.id}`,
            "pm-id": `${maintenance_id.pm_id}`,
            "cm-id": `${maintenance_id.cm_id}`,
            "sla-id": `${maintenance_id.sla_id}`,
            "implementation-id": `${maintenance_id.implementation_id}`,
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      toastMessage = response.data.message;
    } catch (error) {
      console.log(error);
      toast.add({
        severity: "warn",
        summary: "Warn Message",
        detail: "Failed update product",
        life: 5000,
      });
    }
    toast.add({
      severity: "info",
      summary: "Info Message",
      detail: toastMessage,
      life: 5000,
    });
  }

  successAdd.value = !successAdd.value;
  showAddProduct.value = !showAddProduct.value;
  reopen.value = true;
};

const clearForm = () => {
  productDetail.value = "";
};

// const CMList = ['None', 'ICT', 'Others']
// const PMList = ['None', 'ICT', 'Others']

const CM = ref({});
const parentCM = ref({});

const PM = ref({});
const parentPM = ref({});

const slaData = ref({});
const slaParentData = ref({});

const implementation = ref({});
const implementationParent = ref({});

const getParentCM = async () => {
  const response = await axios.get(
    import.meta.env.VITE_API_URL + "maintenance/cm",
    header,
  );
  return (parentCM.value = response.data.data);
};

const getParentPM = async () => {
  const response = await axios.get(
    import.meta.env.VITE_API_URL + "maintenance/pm",
    header,
  );
  return (parentPM.value = response.data.data);
};

const getParentSLA = async () => {
  const response = await axios.get(
    import.meta.env.VITE_API_URL + "maintenance/sla",
    header,
  );
  return (slaParentData.value = response.data.data);
};

const getParentImplementation = async () => {
  const response = await axios.get(
    import.meta.env.VITE_API_URL + "maintenance/implementation",
    header,
  );
  return (implementationParent.value = response.data.data);
};

let principalList = ref([{}]);
let productList = ref([{}]);
const PMList = ref([]);
let initPMList = [];
let CMList = ref([]);
let initCMList = [];

const getProductCategory = async () => {
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `category`)
    .then((data) => {
      productList.value = data.data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      // Handle errors appropriately
    });
};
const getPrincipal = async () => {
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `principal`)
    .then((data) => {
      principalList.value = data.data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      // Handle errors appropriately
    });
};

const getPMList = async () => {
  let pmObj = [{}];
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `pm_by`)
    .then((data) => {
      pmObj = data.data.data;
      initPMList = initPMList.concat(pmObj.map((item) => item.name));
      PMList.value = initPMList;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      // Handle errors appropriately
    });
};
const getCMList = async () => {
  let cmObj = [{}];
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `cm_by`)
    .then((data) => {
      cmObj = data.data.data;
      initCMList = initCMList.concat(cmObj.map((item) => item.name));
      CMList.value = initCMList;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      // Handle errors appropriately
    });
};

onMounted(async () => {
  await getProductCategory();
  await getPrincipal();
  await getParentCM();
  await getParentPM();
  await getParentSLA();
  await getParentImplementation();
  await getPMList();
  await getCMList();
  await getPeriode();

  productObj.value = productList.value.data.find(
    ({ category }) => category === productDetail.value.product_category,
  );
  principalObj.value = principalList.value.data.find(
    ({ principal_id }) => principal_id === productDetail.value.principal_id,
  );

  CM.value = productDetail.value.corrective_maintenance;
  isCMParent.value =
    CM.value.cm_by == ""
      ? true
      : productDetail.value.corrective_maintenance.is_parent;

  PM.value = productDetail.value.preventive_maintenance;
  isPMParent.value =
    PM.value.pm_by == ""
      ? true
      : productDetail.value.preventive_maintenance.is_parent;

  slaData.value = productDetail.value.sla;
  isSlaParent.value =
    slaData.value.sla_id == "" ? true : productDetail.value.sla.is_parent;

  implementation.value = productDetail.value.implementation;
  loadingImple.value = false;
  isImlpementationParent.value =
    implementation.value.implementation_id == ""
      ? true
      : productDetail.value.implementation.is_parent;
});

watch(isCMParent, (x) => {
  if (x) {
    CM.value = parentCM.value;
  } else {
    CM.value = productDetail.value.corrective_maintenance;
    if (CM.value.quantity == undefined) {
      CM.value.quantity = "";
    }
  }
});

watch(isPMParent, (x) => {
  if (x) {
    PM.value = parentPM.value;
  } else {
    if (PM.value.quantity == undefined) {
      PM.value.quantity = "";
    }
    PM.value = productDetail.value.preventive_maintenance;
  }
});

watch(isSlaParent, (x) => {
  if (x) {
    slaData.value = slaParentData.value;
  } else {
    slaData.value = productDetail.value.sla;
  }
});

watch(isImlpementationParent, (x, y) => {
  if (x) {
    implementation.value = implementationParent.value;
  } else {
    implementation.value = productDetail.value.implementation;
  }
});
</script>

<style lang="scss">
.readonly-container {
  @apply pointer-events-none text-gray-400;
}
.readonly-container .p-dropdown-label,
.readonly-container .p-dropdown-trigger {
  @apply text-gray-400;
}
</style>
