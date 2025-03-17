<template>
  <div class="flex flex-row justify-between px-8">
    <h1>PERIODE</h1>
    <button
      v-on:click="addPeriode"
      class="bg-[#908c13] p-2 text-white flex items-center rounded-md"
    >
      <i class="pi pi-plus pr-2"></i>
      Add New Periode
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
                  Periode
                </th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="periode in currList"
                :key="periode.periode"
                class="flex justify-between px-4 bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100"
              >
                <td class="text-sm text-gray-900 font-light whitespace-nowrap">
                  {{ periode.periode }}
                </td>
                <button
                  class="bg-red-600 px-2 m-2 rounded-md text-white"
                  v-on:click="deletePeriode(periode.periode)"
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
        <button class="pi pi-times" v-on:click="addPeriode"></button>
      </div>
      <h1 class="text-center mt-4 text-[#908c13] font-semibold text-2xl mb-4">
        Add Periode
      </h1>
      <div class="py-2">
        <label class="block">Periode<span class="text-red-600">*</span></label>
        <input type="text" class="inputBox" v-model="periodeName" />
      </div>

      <div class="flex justify-end">
        <button
          class="bg-[#908c13] text-white px-2 py-1 rounded-md"
          v-on:click="submitPeriode"
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

let periodeList = ref([{}]);
const periodeName = ref("");

const showModal = ref(false);
const test = ref(false);

watch(searchInput, (x) => {
  if (searchInput.value == "") {
    searchList = periodeList.value;

    currList.value = _.cloneDeep(searchList.value);
  } else {
    searchList = periodeList.value.filter((list) =>
      list.periode.toLowerCase().includes(searchInput.value.toLowerCase()),
    );
  }
  currList.value = _.cloneDeep(searchList);
});

const addPeriode = () => {
  periodeName.value = "";
  test.value = false;
  showModal.value = !showModal.value;
};

const deletePeriode = async (periodeName) => {
  let text = "Are you sure you want to delete data?";
  if (confirm(text) == true) {
    try {
      const response = await axios.delete(
        import.meta.env.VITE_API_URL + `periode/${periodeName}`,
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
      toast.add({
        severity: "error",
        summary: "Error Message",
        detail: "Data cannot be deleted because it is used in another field!",
        life: 5000,
      });
    }

    fetchPeriode();
  }
};

const fetchPeriode = async () => {
  const response = await axios
    .get(import.meta.env.VITE_API_URL + "periode")
    .then((data) => {
      periodeList.value = data.data.data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
  searchList = periodeList;
  currList.value = _.cloneDeep(searchList.value);
  searchInput.value = "";
};

const submitPeriode = async () => {
  if (periodeName.value == "") {
    toast.add({
      severity: "warn",
      summary: "Warn Message",
      detail: "Please fill all the required field!",
      life: 5000,
    });
    return;
  }
  const testPeriode = { periodic: periodeName.value };
  try {
    const response = await axios.post(
      import.meta.env.VITE_API_URL + "periode",
      testPeriode,
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
  fetchPeriode();
};

onMounted(async () => {
  fetchPeriode();
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

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
