<script setup lang="ts">
import axios from "axios";
import Table from "../components/TableComp.vue";
import { onMounted, ref } from "vue";

const tempData = ref();
const data = [
  "#",
  "Customer",
  "Cost Sheet",
  "Sales",
  "Project",
  "Products",
  "Details",
];
onMounted(async () => {
  try {
    const response = await axios.get(
      import.meta.env.VITE_API_URL + "project/status/Pending",
    );
    if (response.data.data.length > 0) {
      tempData.value = response.data.data.map((contract: any) =>
        Object.values(contract),
      );
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});
</script>

<template>
  <div v-if="tempData">
    <div class="">
      <h1 class="text-[#908c13] font-semibold text-3xl mb-12">Pending List</h1>
      <Table :data="data" :row_data="tempData"></Table>
    </div>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>
