<template>
  <div>
    <h2>Corrective Maintenance</h2>
    <div class="pb-2">
      <label for="" class="block"
        >Maintenance By<span class="text-red-600">*</span></label
      >
      <Dropdown
        v-model="cmObj"
        :options="CMList.data"
        optionLabel="name"
        placeholder=""
        id="dropdown"
        pt:input:class="p-0 text-sm"
        pt:clearIcon:class="text-black"
        pt:trigger:class="text-black"
        class="inputBox"
      />
    </div>
    <div v-if="cm.cm_by != 'None' && cm.cm_by != ''">
      <div class="flex gap-4">
        <div class="w-full pb-2">
          <label for="" class="block"
            >Start Date<span class="text-red-600">*</span></label
          >
          <input type="date" class="inputBox" v-model="cm.start_date" />
        </div>
        <div class="w-full pb-2">
          <label for="" class="block"
            >End Date<span class="text-red-600">*</span></label
          >
          <input type="date" class="inputBox" v-model="cm.end_date" />
        </div>
      </div>
      <div class="w-full flex-none">
        <label for="" class="block">Quantity</label>
        <QuantityInput v-model:quantity="cm.quantity" />
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

const cm = defineModel("cm");
const cmObj = ref({});
const CMList = ref([{}]);
let initList = [];
const periodList = [
  "Monthly",
  "Bimonthly",
  "Quarterly",
  "Semesterly",
  "Yearly",
];

onMounted(async () => {
  const response = await axios
    .get(import.meta.env.VITE_API_URL + `cm_by`)
    .then((data) => {
      initList = data.data.data;
      CMList.value.data = initList;
      cmObj.value = CMList.value.data.find(
        ({ name }) => name === cm.value.cm_by,
      );
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});

watch(cmObj, async () => {
  if (cmObj.value != undefined) {
    cm.value.cm_by = cmObj.value.name;
  }
});
</script>

<style lang="scss" scoped></style>
