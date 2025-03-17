<script setup lang="ts">
const props = defineProps({
  data: Array,
  row_data: Object,
});
</script>

<template>
  <div class="flex flex-col">
    <div class="overflow-x-auto">
      <div class="py-2 inline-block min-w-full">
        <div class="overflow-hidden">
          <table class="min-w-full">
            <thead class="bg-[#908c13] border-b">
              <tr>
                <th
                  v-for="element in props.data"
                  scope="col"
                  class="text-sm font-medium text-white px-6 py-4 text-left"
                >
                  {{ element }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(row, rowIndex) in props.row_data"
                :key="rowIndex"
                class="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100"
              >
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
                >
                  {{ rowIndex + 1 }}
                </td>
                <td
                  v-for="(cell, cellIndex) in row"
                  v-show="cellIndex != 0"
                  :key="cellIndex"
                  class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                >
                  {{ cell }}
                </td>
                <td
                  class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                >
                  <router-link :to="{ path: `/contracts/${row[0]}` }">
                    <button
                      class="p-2 rounded-md bg-[#908c13] text-white font-semibold"
                    >
                      View Data
                    </button>
                  </router-link>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
