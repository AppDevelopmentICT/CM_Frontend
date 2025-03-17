<template>
  <div class="flex flex-col items-center">
    <button
      class="primary-button"
      @click="triggerFileInput"
      :disabled="disabled"
    >
      {{ disabled ? "Importing Data..." : "Import Data" }}
    </button>
    <input
      ref="fileInput"
      type="file"
      class="hidden"
      @change="importData"
      accept=".xlsx, .xls"
    />
  </div>
</template>

<script lang="ts" setup>
import ExcelJS from "exceljs";
import { ref } from "vue";

let disabled = ref(false);
const fileInput = ref<HTMLInputElement | null>(null);
const jsonData = ref<any[]>([]); // Store the processed JSON data here

const triggerFileInput = () => {
  fileInput.value?.click();
};

const importData = async (event: Event) => {
  const file = (event.target as HTMLInputElement).files?.[0];
  if (!file) return;

  disabled.value = true;

  try {
    const workbook = new ExcelJS.Workbook();
    const arrayBuffer = await file.arrayBuffer();

    await workbook.xlsx.load(arrayBuffer);
    const worksheet = workbook.getWorksheet(1);

    const rows: any[] = [];
    worksheet.eachRow((row, rowNumber) => {
      if (rowNumber === 1) return; // Skip the header row

      const rowData: Record<string, any> = {};
      row.eachCell((cell, colNumber) => {
        rowData[`column_${colNumber}`] = cell.value;
      });

      rows.push(rowData);
    });

    jsonData.value = rows;
    console.log("Processed Data:", jsonData.value);
  } catch (error: any) {
    console.error("Error importing data:", error.message);
  } finally {
    disabled.value = false;
  }
};
</script>
