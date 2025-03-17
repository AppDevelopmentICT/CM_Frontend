<template>
    <button
        class="bg-red-600 p-2 w-48 text-white rounded-md text-sm"
        @click="openModal()"
        v-if="userStore.role == 'Sales Admin'"
    >
        Delete Contract
    </button>

    <!-- Modal -->
    <Transition
        name="modal"
        enter-active-class="ease-out duration-300"
        enter-from-class="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
        enter-to-class="opacity-100 translate-y-0 sm:scale-100"
        leave-active-class="ease-in duration-200"
        leave-from-class="opacity-100 translate-y-0 sm:scale-100"
        leave-to-class="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
    >
        <div
            v-if="isModalOpen"
            class="fixed inset-0 z-10 w-screen overflow-y-auto"
            aria-labelledby="modal-title"
            role="dialog"
            aria-modal="true"
        >
            <!-- Background backdrop -->
            <div
                class="fixed inset-0 bg-gray-500/75 transition-opacity"
                @click="closeModal"
                aria-hidden="true"
            ></div>

            <!-- Modal content -->
            <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                    <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                        <div class="sm:flex sm:items-start">
                            <div
                                class="mx-auto flex size-12 shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:size-10"
                            >
                                <svg
                                    class="size-6 text-red-600"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke-width="1.5"
                                    stroke="currentColor"
                                    aria-hidden="true"
                                    data-slot="icon"
                                >
                                    <path
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z"
                                    />
                                </svg>
                            </div>
                            <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                                <h3
                                    class="text-base font-semibold text-gray-900"
                                    id="modal-title"
                                >
                                    Delete Contract
                                </h3>
                                <div class="mt-2">
                                    <p class="text-sm text-gray-500">
                                        Are you sure you want to delete this contract? This action cannot
                                        be undone.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                        <button
                            type="button"
                            class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto"
                            @click="confirmDelete()"
                        >
                            Delete
                        </button>
                        <button
                            type="button"
                            class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                            @click="closeModal"
                        >
                            Cancel
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </Transition>
</template>

<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";
import { userManagement } from "../../../pinia";
import ENDPOINTS from "../../../constant/endpoint";
import { useToast } from "primevue/usetoast";
import { useRouter } from "vue-router";

const props = defineProps<{
  id: string
}>()

const toast = useToast();
const router = useRouter();
const isModalOpen = ref(false);
const userStore = userManagement();

const openModal = () => {
    isModalOpen.value = true;
};

const closeModal = () => {
    isModalOpen.value = false;
};

const deleteContract = async (id: string) => {
    try {
        await axios.delete(`${import.meta.env.VITE_API_URL}${ENDPOINTS.DELETE_PROJECT_BY_ID(id)}`)

        closeModal();

        toast.add({
        severity: "success",
        summary: "Success Message",
        detail: 'Project Deleted Successfull',
        life: 5000,
        });

        setTimeout(() => {
        router.push('/contracts');
        }, 1000);
    } catch (error: any) {
        closeModal()

        toast.add({
            severity: "error",
            summary: "Delete Error",
            detail: error.message,
            life: 3000,
        });
    }

};

const confirmDelete = () => {
    deleteContract(props.id);
};
</script>

<style scoped>
.modal-enter-active {
    transition: all 0.3s ease-out;
}
.modal-leave-active {
    transition: all 0.2s ease-in;
}
.modal-enter-from {
    opacity: 0;
    transform: translateY(10px);
}
.modal-enter-to {
    opacity: 1;
    transform: translateY(0);
}
.modal-leave-from {
    opacity: 1;
    transform: translateY(0);
}
.modal-leave-to {
    opacity: 0;
    transform: translateY(10px);
}
</style>