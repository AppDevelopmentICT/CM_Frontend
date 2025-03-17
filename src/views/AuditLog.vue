<template>
  <div class="card">
    <DataTable
      :value="tableData"
      paginator
      :rows="20"
      :rowsPerPageOptions="[5, 10, 20, 50]"
    >
      <Column field="username" header="User" style="width: 20%"></Column>
      <Column field="roles" header="Role" style="width: 10%"></Column>
      <Column field="action" header="Action" style="width: 15%"></Column>
      <Column field="action_detail" header="Detail" style="width: 35%"></Column>
      <Column field="time" header="Time" style="width: 20%"></Column>
    </DataTable>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import axios from "axios";
import DataTable from "primevue/datatable";
import Column from "primevue/column";

const rawData = ref();
const tableData = ref();

const getUserAudit = async () => {
  let roles;
  const jwt = JSON.parse(localStorage.getItem("new_token")).token;
  try {
    const response = await axios.get(import.meta.env.VITE_API_URL + "profile", {
      headers: {
        auhtorization: jwt,
      },
    });
    roles = response.data.roles;
  } catch (e) {
    console.error(e);
  } finally {
    if (roles == "Super Admin") {
      const response = await axios.get(import.meta.env.VITE_API_URL + "audit", {
        headers: {
          "user-token": jwt,
        },
      });
      return response.data;
    } else {
      const response = await axios.get(
        import.meta.env.VITE_API_URL + "audit/user",
        {
          headers: {
            "user-token": jwt,
          },
        },
      );
      return response.data;
    }
  }
};

onMounted(async () => {
  rawData.value = await getUserAudit();
  tableData.value = rawData.value.data;
  console.log(rawData.value.data);
  console.log(tableData.value);
});
</script>
