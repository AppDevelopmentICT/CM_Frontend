<template>
  <div class="flex flex-row justify-between px-8">
    <h1>PM</h1>
    <button
      v-on:click="addPM"
      class="bg-[#908c13] p-2 text-white flex items-center rounded-md"
    >
      <i class="pi pi-plus pr-2"></i>
      Add New PM
    </button>
  </div>
  <div class="flex items-center gap-4 justify-end px-8">
    <div class="flex w-1/4">
      <IconField iconPosition="right" class="w-full">
        <InputIcon>
          <i class="pi pi-search" />
        </InputIcon>
        <input type="text" class="inputBox" v-model="searchInput" />
      </IconField>
    </div>
  </div>
  <div class="flex flex-col">
    <div class="overflow-x-auto sm:mx-0.5 lg:mx-0.5">
      <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
        <div class="overflow-hidden">
          <table class="min-w-full">
            <thead class="bg-[#908c13] border-b">
              <tr>
                <th class="text-sm font-medium text-white px-6 py-4 text-left">
                  PM Name
                </th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="PM in currList"
                :key="PM.name"
                class="flex justify-between px-4"
              >
                <td class="text-sm text-gray-900 font-light whitespace-nowrap">
                  {{ PM.name }}
                </td>
                <button
                  class="bg-red-600 m-2 px-2 rounded-md text-white"
                  v-on:click="deletePM(PM.name)"
                >
                  Delete
                </button>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <div
    class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75"
    v-if="showModal"
  >
    <div class="bg-white rounded-lg p-8 max-w-md">
      <div class="flex justify-end">
        <button class="pi pi-times" v-on:click="addPM"></button>
      </div>
      <h1 class="text-center mt-4 text-[#908c13] font-semibold text-2xl mb-4">
        Add PM
      </h1>
      <div class="py-2">
        <label class="block">PM Name<span class="text-red-600">*</span></label>
        <input type="text" class="inputBox" v-model="PMName" />
      </div>

      <div class="flex justify-end">
        <button
          class="bg-[#908c13] text-white px-2 py-1 rounded-md"
          v-on:click="submitPM"
        >
          submit
        </button>
      </div>
    </div>
  </div>
  <Toast />
</template>

<script setup>
import { onMounted } from "vue";
import { ref, watch } from "vue";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";
import { useToast } from "primevue/usetoast";
import _ from "lodash";
import "primeicons/primeicons.css";
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";

const searchInput = ref("");
const currList = ref([{}]);
let searchList;

const toast = useToast();
const route = useRoute();
const router = useRouter();

let pmList = ref([{}]);
const PMName = ref("");

const showModal = ref(false);
const showToast = ref(false);
const test = ref(false);

watch(searchInput, (x) => {
  if (searchInput.value == "") {
    searchList = pmList.value;

    currList.value = _.cloneDeep(searchList.value);
  } else {
    searchList = pmList.value.filter((list) =>
      list.name.toLowerCase().includes(searchInput.value.toLowerCase()),
    );
  }
  currList.value = _.cloneDeep(searchList);
});

const addPM = () => {
  PMName.value = "";
  test.value = false;
  showModal.value = !showModal.value;
};

const deletePM = async (PM_id) => {
  let text = "Are you sure you want to delete data?";
  if (confirm(text) == true) {
    try {
      const PMId = { id: PM_id };
      const response = await axios.delete(
        import.meta.env.VITE_API_URL + `pm_by/${PM_id}`,
        {
          headers: {
            "user-token": JSON.parse(localStorage.getItem("new_token"))
              .token,
          },
        },
      );
      toast.add({
        severity: "success",
        summary: "Success Message",
        detail: "Data successfully deleted!",
        life: 5000,
      });
    } catch (error) {
      console.log(error);
    }

    fetchPM();
  }
};

const fetchPM = async () => {
  const response = await axios
    .get(import.meta.env.VITE_API_URL + "pm_by")
    .then((data) => {
      pmList.value = data.data.data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
  searchList = pmList;
  currList.value = _.cloneDeep(searchList.value);
  searchInput.value = "";
};

const submitPM = async () => {
  if (PMName.value == "") {
    toast.add({
      severity: "warn",
      summary: "Warn Message",
      detail: "Please fill all the required field!",
      life: 5000,
    });
    return;
  }
  const testPM = { name: PMName.value };
  try {
    const response = await axios.post(
      import.meta.env.VITE_API_URL + "pm_by",
      testPM,
      {
        headers: {
          "user-token": JSON.parse(localStorage.getItem("new_token"))
            .token,
        },
      },
    );
  } catch (error) {
    console.log(error);
  }
  toast.add({
    severity: "success",
    summary: "Success Message",
    detail: "Data successfully added!",
    life: 5000,
  });
  showModal.value = false;
  fetchPM();
};

onMounted(async () => {
  fetchPM();
});
</script>

<style scoped>
.asd {
  @apply border-red-500;
}

h1 {
  @apply text-[#908c13] font-semibold text-2xl mb-4;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.25s ease;
}

table tbody tr {
  @apply bg-white;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
