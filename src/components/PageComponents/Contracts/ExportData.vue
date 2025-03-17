<template>
  <button :disabled="disabled" class="primary-button" @click="exportData">
    <div v-if="disabled" class="flex items-center gap-4">
      Exporting Data
      <LoaderCircle class="h-5 w-5 text-white animate-spin" />
    </div>
    <div v-else>Export Data</div>
  </button>
</template>

<script lang="ts" setup>
import ExcelJS from "exceljs";
import { ExportData } from "../../../types/export-data";
import { saveAs } from "file-saver";
import axios from "axios";
import { ref } from "vue";
import { LoaderCircle } from "lucide-vue-next";
import ENDPOINTS from "../../../constant/endpoint";

let disabled = ref(false);

interface ExportDataResponse {
  data: ExportData[];
}

const getExportData = async () => {
  try {
    const response = await axios.get<ExportDataResponse>(
      `${import.meta.env.VITE_API_URL}${ENDPOINTS.GET_EXPORT_PROJECT_LIST}`,
    );
    const data = response.data.data;

    return data;
  } catch (error: any) {
    console.log(error.message);
  }
};

const formatCreatedDate = (dateString: string): string => {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0"); // Months are zero-based
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
};

const formatDate = (date: Date) => {
  const formatter = new Intl.DateTimeFormat("id-ID", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });

  return formatter.format(date);
};

const exportData = async () => {
  try {
    disabled.value = true;

    const excelData = await getExportData();

    if (!excelData.length) {
      throw new Error("Data not found");
    }

    const workbook = new ExcelJS.Workbook();
    const worksheet = workbook.addWorksheet("Contract List");

    // Define headers
    const headers = [
      // project information
      "Customer Name",
      "Sales Name",
      "Cost Sheet",
      "Project Name",

      // contract desc
      "Project Type",
      "Contract Number",
      "Internal Cost",
      "Selling Cost",
      "Managed Service",

      // Product 
      "Product Type",
      "Product Brand",
      "Product Name",
      "Serial Number",
      "SI Number",
      "Product Quantity",
      "Start Date Product",
      "End Date Product",

      // pm
      "PM By",
      "PM Start Date",
      "PM End Date",
      "Periode PM",
      "PM Qty",

      // cm
      "CM By",
      "CM Start Date",
      "CM End Date",
      "CM Qty",

      // implementation
      "Implementation By",
      "Implementation Start Date",
      "Implementation End Date",

      "Severity 1 Response Time",
      "Severity 1 Resolution Time",
      "Severity 2 Response Time",
      "Severity 2 Resolution Time",
      "Severity 3 Response Time",
      "Severity 3 Resolution Time",
      "Severity 4 Response Time",
      "Severity 4 Resolution Time",
     
      "Description",
      "Created Date",
    ];

    // Add headers as the first row
    worksheet.addRow(headers).font = { bold: true };

    // Map and add data rows
    excelData.forEach((row) => {
      worksheet.addRow([
        row.customer_name,
        row.sales_name,
        row.cost_sheet,
        row.project_name,
        row.project_type,
        row.contract_number,
        row.internal_cost,
        row.selling_cost,
        row.managed_service ? 'Yes' : 'No',
        row.product_type,
        row.product_brand,
        row.product_name,
        row.serial_number,
        row.si_number,
        row.product_quantity,
        row.product_start_date,
        row.product_end_date,
        row.pm_by,
        row.pm_start_date,
        row.pm_end_date,
        row.maintenance_period,
        row.pm_quantity,
        row.cm_by,
        row.cm_start_date,
        row.cm_end_date,
        row.cm_quantity,
        row.i_by,
        row.i_start_date,
        row.i_end_date,
        row.severity1_response_time,
        row.severity1_resolution_time,
        row.severity2_response_time,
        row.severity2_resolution_time,
        row.severity3_response_time,
        row.severity3_resolution_time,
        row.severity4_response_time,
        row.severity4_resolution_time,
        row.project_description,
        formatCreatedDate(row.created_date),
      ]);
    });

    const mergeColumnsBasedOnFirstColumn = (columnsToMerge: number[]) => {
    let startRow = 2; // Start after the header row
    let currentValue = worksheet.getCell(startRow, 1).value; // Get the value of the first column (Customer)

    for (let rowIndex = 3; rowIndex <= worksheet.rowCount; rowIndex++) {
      const firstColumnValue = worksheet.getCell(rowIndex, 1).value; // Value in the first column

      if (firstColumnValue !== currentValue) {
        // Merge specified columns if the value in the first column changes
        if (rowIndex - startRow > 1) {
          columnsToMerge.forEach((colIndex) => {
            worksheet.mergeCells(startRow, colIndex, rowIndex - 1, colIndex);
          });
        }
        startRow = rowIndex; // Update start row
        currentValue = firstColumnValue; // Update current value
      }
    }

    // Handle the last group of merges
    if (worksheet.rowCount - startRow > 0) {
      columnsToMerge.forEach((colIndex) => {
        worksheet.mergeCells(startRow, colIndex, worksheet.rowCount, colIndex);
      });
    }
  };

  const columnsToMerge = [1, 2, 3, 4, 5, 6, 7, 8, 9, 40, 41];
  mergeColumnsBasedOnFirstColumn(columnsToMerge);

    // Add border to all cells
    worksheet.eachRow({ includeEmpty: true }, (row) => {
      row.eachCell({ includeEmpty: true }, (cell) => {
        const borderStyle: Partial<ExcelJS.Borders> = {
          top: { style: "thin" as ExcelJS.BorderStyle },
          left: { style: "thin" as ExcelJS.BorderStyle },
          bottom: { style: "thin" as ExcelJS.BorderStyle },
          right: { style: "thin" as ExcelJS.BorderStyle },
        };
        cell.border = borderStyle;
        cell.alignment = {
          horizontal: "left",
          vertical: "top",
          wrapText: true,
        };
      });
    });

    worksheet.columns.forEach((column) => {
      column.width = 20;
    });

    
    // Export workbook
    const buffer = await workbook.xlsx.writeBuffer();
    const blob = new Blob([buffer], {
      type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    });
    const fileName = `Contract List ${formatDate(new Date())}`;

    saveAs(blob, fileName);
    disabled.value = false;
  } catch (error: any) {
    disabled.value = false;
    console.error(error.message);
  }
};
</script>
