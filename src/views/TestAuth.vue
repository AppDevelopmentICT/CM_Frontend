<template>
<h1>Halo</h1>
<img :src="data">
</template>

<script setup lang="ts">
import QRCode from 'qrcode'
import { onMounted, ref } from 'vue';

const data = ref()

const uri = "otpauth://totp/CM%20App:string?secret=string&issuer=CM%20App";
const generateQR = async () => {
    try {
        return await QRCode.toDataURL(uri)
    } catch (err) {
        console.error(err)
    }
}
onMounted(async () => {
    data.value = await generateQR()
})

</script>