<template>
  <div>
    <h2>SLA</h2>
    <div class="col-span-2">
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
              class="inputBox"
              v-model="sla.severity_1_response_time"
            />
          </div>
          <div class="">
            <label for="" class="block"
              >Resolution Time<span class="text-red-600">*</span></label
            >
            <input
              type="text"
              class="inputBox"
              v-model="sla.severity_1_resolution_time"
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
              class="inputBox"
              v-model="sla.severity_2_response_time"
            />
          </div>
          <div class="">
            <label for="" class="block"
              >Resolution Time<span class="text-red-600">*</span></label
            >
            <input
              type="text"
              class="inputBox"
              v-model="sla.severity_2_resolution_time"
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
              class="inputBox"
              v-model="sla.severity_3_response_time"
            />
          </div>
          <div class="">
            <label for="" class="block"
              >Resolution Time<span class="text-red-600">*</span></label
            >
            <input
              type="text"
              class="inputBox"
              v-model="sla.severity_3_resolution_time"
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
              class="inputBox"
              v-model="sla.severity_4_response_time"
            />
          </div>
          <div class="">
            <label for="" class="block"
              >Resolution Time<span class="text-red-600">*</span></label
            >
            <input
              type="text"
              class="inputBox"
              v-model="sla.severity_4_resolution_time"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { ref } from "vue";
import axios from "axios";
import DurationInput from "../components/DurationInput.vue";

const sla = defineModel("sla");
const PMList = ["None", "ICT", "Others"];
const periodList = [
  "Monthly",
  "Bimonthly",
  "Quarterly",
  "Semesterly",
  "Yearly",
];
</script>

<style lang="scss" scoped></style>
