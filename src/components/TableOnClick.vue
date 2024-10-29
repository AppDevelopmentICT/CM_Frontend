<script setup lang="ts">

const props = defineProps({
    data: Array,
    row_data: Object,
});


</script>

<template>
    <table class="min-w-full block">
        <thead class="bg-[#908c13] border-b w-full table table-fixed">
            <tr>
                <th scope="col" class="w-10 text-sm font-medium text-white px-6 py-4 text-left">
                    #
                </th>
                <th v-for="element in props.data" scope="col" class="text-sm font-medium text-white px-6 py-4 text-left">
                    {{ element }}
                </th>
            </tr>
        </thead>
        <tbody class="overflow-y-auto max-h-80 block">
            <tr v-for="(row, rowIndex) in props.row_data" :key="rowIndex" class="w-full table table-fixed bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100">
                <td class="w-10 px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ rowIndex + 1 }}</td>
                <td v-for="(cell, cellIndex) in row" v-show="cellIndex!=0" :key="cellIndex" class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap text-ellipsis overflow-hidden">
                    {{ cell }}
                </td>
                <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                    <router-link :to="{path: `/contracts/${row[0]}`}">
                        <button class="p-2 rounded-md bg-[#908c13] text-white font-semibold">View Data</button>
                    </router-link>
                </td>
            </tr>
        </tbody>
    </table>
</template>