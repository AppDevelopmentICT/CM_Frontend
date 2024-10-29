<template>
    <Transition>
        <div class="fixed top-0 left-1/2 translate-x-[-50%] my-2  " v-if="showToast">
            <div class="bg-[#ecececce] rounded-lg p-4 min-w-48 max-w-md flex justify-center">
                <p :class="messageType">
                    {{props.toastMessage}}
                </p>
                
            </div>
        </div>
    </Transition>
</template>

<script setup>
import { onUpdated } from 'vue';

const showToast = defineModel('showToast')
const props = defineProps({
    toastMessage : String,
    messageType : String
})

onUpdated(() => {
    setTimeout(() => {
            showToast.value = false;
        }, 3000);
})




</script>

<style lang="scss" scoped>
.info{
    @apply text-black
}
.warning{
    @apply text-yellow-600
}
.danger{
    @apply text-red-600
}
</style>