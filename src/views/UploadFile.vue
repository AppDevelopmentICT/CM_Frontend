<template>
    <div class="">
        <label class="block" for="fileInput">File</label>
        <input type="file" id="fileInput" multiple v-on:change="getFile()"> <br>
        <button @click=uploadFile() class="bg-black text-white p-1 mt-2">Add Form</button>

        <a href="https://pocketbase.ictincub.my.id/api/files/nh8a6wpfc1smgyp/bhrma1ohs1rjjt1/932_article_text_1711_2_10_20201002_SCcNJ97QIj.pdf?token="><i class="pi pi-file"></i></a>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import PocketBase from 'pocketbase';

const pb = new PocketBase(import.meta.env.VITE_PB_BASEURL);
const formData = new FormData();

const getFile = () => {
    for (let file of fileInput.files) {
        formData.append('contract_file', file);
    }
    formData.append('project_id', "test2")
}

const uploadFile = async () => {
    const createdRecord = await pb.collection('files').create(formData);
}

onMounted(async () => {
    const record = await pb.collection('files').getFirstListItem('project_id="test2"')
})
</script>