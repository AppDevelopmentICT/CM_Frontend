<template>
  <div>
    <div class="flex justify-between mb-4 items-center">
      <h4 class="text-2xl font-semibold text-[#908c13]">User Management</h4>
      <button
        class="bg-[#908c13] p-2 text-white rounded-md mx-4"
        v-on:click="getUserList"
      >
        Sync to PocketBase
      </button>
    </div>

    <Accordion :multiple="true" :activeIndex="[0]">
      <AccordionTab header="Add User">
        <AddUser />
      </AccordionTab>
      <AccordionTab header="User List">
        <UserList />
      </AccordionTab>
    </Accordion>
    <div
      class="fixed inset-0 flex flex-col items-center justify-center bg-gray-500 bg-opacity-30"
      v-if="loading"
    >
      <ProgressSpinner class="w-[200px] h-[200px]" />
      <p class="!text-[#908c13] !text-3xl !font-bold">Loading</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import UserList from "../components/User/UserList.vue";
import AddUser from "../components/User/AddUser.vue";
import axios from "axios";
import { userManagement } from "../pinia";
import ProgressSpinner from "primevue/progressspinner";
import PocketBase from "pocketbase";

const loading = ref(false);

const userStore = userManagement();
const pb = new PocketBase("http://172.16.100.210:8090");

let userList;
let userpb;
const getUserList = async () => {
  loading.value = true;
  const response = await axios
    .get(import.meta.env.VITE_API_URL + "all_user", {
      headers: {
        "user-id": userStore.db_id,
      },
    })
    .then((data) => {
      userList = data.data.data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });

  for (const user of userList) {
    const record = await pb
      .collection("users")
      .getFirstListItem('email="' + user.email + '"')
      .then((data) => {})
      .catch((error) => {
        console.error("error", error);
        const response = axios
          .get(import.meta.env.VITE_API_URL + "user/" + user.id)
          .then((data) => {
            userpb = data.data.data;
            let cut = userpb.username.indexOf("@");
            let fixedUsername = userpb.username.substring(0, cut);
            fixedUsername = fixedUsername.replaceAll(" ", "_");
            fixedUsername = fixedUsername.replaceAll(".", "_");
            const temp = {
              uuid: userpb.user_id,
              username: fixedUsername,
              email: userpb.email,
              emailVisibility: true,
              password: userpb.password,
              passwordConfirm: userpb.password,
              name: userpb.username,
              isAdmin: false,
              loginAccount: true,
              secret_key: "",
            };
            if (userpb.user_roles == "Super Admin") {
              temp.isAdmin = true;
            }

            const record = pb.collection("users").create(temp);
          })
          .catch((error) => {
            console.error("Error fetching data:", error);
          });
      });
  }

  loading.value = false;
};
</script>
