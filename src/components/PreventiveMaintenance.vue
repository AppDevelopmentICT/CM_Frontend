<template>
  <div>
    <h2>Preventive Maintenance</h2>
    <div class="pb-2">
      <label for="" class="block"
        >Maintenance By<span class="text-red-600">*</span></label
      >
      <Dropdown
        v-model="pmObj"
        :options="PMList.data"
        optionLabel="name"
        placeholder=""
        id="dropdown"
        pt:input:class="p-0 text-sm"
        pt:clearIcon:class="text-black"
        pt:trigger:class="text-black"
        class="inputBox"
      />
    </div>
    <div v-show="pm.pm_by != 'None' && pm.pm_by != ''">
      <div class="flex w-full gap-4">
        <div class="w-full pb-2">
          <label for="" class="block"
            >Start Date<span class="text-red-600">*</span></label
          >
          <input type="date" class="inputBox" v-model="pm.start_date" />
        </div>
        <div class="w-full pb-2">
          <label for="" class="block"
            >End Date<span class="text-red-600">*</span></label
          >
          <input type="date" class="inputBox" v-model="pm.end_date" />
        </div>
      </div>
      <div class="flex gap-4">
        <div class="w-full">
          <label for="" class="block"
            >Maintenance Period<span class="text-red-600">*</span></label
          >
          <Dropdown
            v-model="periodeObj"
            :options="periodeList"
            optionLabel="periode"
            placeholder=""
            id="dropdown"
            pt:input:class="p-0 text-sm"
            pt:clearIcon:class="text-black"
            pt:trigger:class="text-black"
            class="inputBox"
          />
        </div>
        <div class="w-full">
          <label for="" class="block">Quantity</label>
          <QuantityInput v-model:quantity="pm.quantity" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Dropdown from "primevue/dropdown";
import { onMounted, watch } from "vue";
import { ref } from "vue";
import axios from "axios";
import { defineAsyncComponent } from "vue";

const QuantityInput = defineAsyncComponent(() => import("./QuantityInput.vue"));

const pm = defineModel("pm");
const pmObj = ref({});
const periodeObj = ref({});
const PMList = ref([{ data: [] }]);
let initList = [];
const periodeList = ref([{}]);
// const periodList = ['Monthly', 'Bimonthly', 'Quarterly', 'Semesterly', 'Yearly']

const getPeriode = async () => {
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `periode`)
    .then((data) => {
      periodeList.value = data.data.data;
      periodeObj.value = periodeList.value.find(
        ({ periode }) => periode === pm.value.pm_periode,
      );
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
};

onMounted(async () => {
  await getPeriode();
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `pm_by`)
    .then((data) => {
      initList = data.data.data;
      PMList.value.data = initList;
      pmObj.value = PMList.value.data.find(
        ({ name }) => name === pm.value.pm_by,
      );
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});

watch(pmObj, async () => {
  if (pmObj.value != undefined) {
    pm.value.pm_by = pmObj.value.name;
  }
});
watch(periodeObj, async () => {
  if (periodeObj.value != undefined) {
    pm.value.pm_periode = periodeObj.value.periode;
    console.log(pm.value.pm_periode);
  }
});
</script>

<style lang="scss" scoped></style>
