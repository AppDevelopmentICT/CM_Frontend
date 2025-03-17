<script setup>
import { useRouter } from "vue-router";
import { ref, watch } from "vue";
import axios from "axios";
import PocketBase from "pocketbase";
import { useCookies } from "vue3-cookies";
import { userManagement } from "../pinia";
import { useToast } from "primevue/usetoast";
import { SignJWT } from "jose";
 
const toast = useToast();
const { cookies } = useCookies();
const router = useRouter();
const pb = new PocketBase(import.meta.env.VITE_PB_BASEURL);
const sawPassword = ref(false);

const userStore = userManagement();
const secret_key = ref();
const cookiesToken = ref();
const isPasswordVerify = ref(true);
const otpInput = ref();

const user = {
  email: ref(""),
  password: ref(""),
};

const checkNull = (userData) => {
  if (!userData.email.value || !userData.password.value) {
    toast.add({
      severity: "warn",
      summary: "Warning Message",
      detail: "Fill required input",
      life: 5000,
    });

    return false;
  }
  
  return true;
};

const loginGoogle = async () => {
  var authData;
  try {
    authData = await pb.collection("users").authWithOAuth2({
      provider: "google",
    });
    const isLogin = await pb.collection("users").getOne(authData.record.id);
    if (!isLogin.loginAccount)
      return toast.add({
        severity: "error",
        summary: "Invalid Message",
        detail:
          "Your Account has no login access, contact Super Admin to proceed",
        life: 5000,
      });
    if (pb.authStore.isValid) {
      if (authData.meta) {
        cookies.set("auth_token", authData.meta.accessToken);
        const response = await axios.get(
          import.meta.env.VITE_API_URL + `user/pb/${authData.meta.email}`,
        );
        userStore.setValue({
          pb_id: authData.meta.id,
          db_id: response.data.data.user_id,
          name: authData.meta.name,
          role: response.data.data.user_roles,
        });
      }
      await router.push("/");
    }
  } catch (e) {
    toast.add({
      severity: "error",
      summary: "Invalid Message",
      detail: "The credentials did not match our records!",
      life: 5000,
    });
  }
};

const loginEmail = async (userData) => {
  if (checkNull(userData)) {
    let authData;
    let responseToken;

    try {
      authData = await pb
        .collection("users")
        .authWithPassword(userData.email.value, userData.password.value);

      const isLogin = await pb.collection("users").getOne(authData.record.id);

      cookiesToken.value = authData.token;
      cookies.set("auth_token", authData.token);

      if (!isLogin.loginAccount)
        return toast.add({
          severity: "error",
          summary: "Invalid Message",
          detail:
            "Your Account has no login access, contact Super Admin to proceed",
          life: 5000,
        });

      if (pb.authStore.isValid) {
        if (authData) {
          const response = await axios.get(
            import.meta.env.VITE_API_URL + `user/pb/${authData.record.email}`,
          );

          responseToken = response.data.data.user_token

          userStore.setValue({
            pb_id: response.data.data.user_id,
            db_id: response.data.data.user_id,
            name: authData.record.name,
            role: response.data.data.user_roles,
          });
        }

        // isPasswordVerify.value = false
        // secret_key.value = await getKey(authData.record.id)

        localStorage.setItem('new_token', JSON.stringify({
          token: responseToken,
        }));
        await router.push('/');
      }
    } catch (e) {
      userStore.removeValue();
      toast.add({
        severity: "error",
        summary: "Invalid Message",
        detail: "The credentials did not match our records!",
        life: 5000,
      });
    }
  }
};

const verifyOTP = async (secret_key) => {
  try {
    const response = await axios.post(
      import.meta.env.VITE_API_URL + "verify-otp",
      {
        input_otp: otpInput.value,
      },
      {
        headers: {
          "secret-key": secret_key,
        },
      },
    );
    if (response.status == 200) {
      cookies.set("auth_token", cookiesToken.value);
      await router.push("/");
    }
  } catch (error) {
    toast.add({
      severity: "error",
      summary: "Invalid Message",
      detail: error.response?.data.message,
      life: 5000,
    });
  }
};

const getKey = async (id) => {
  let temp_data;
  try {
    const response = await axios.get(
      import.meta.env.VITE_API_URL + "get-user-secret",
      {
        headers: {
          id: id,
        },
      },
    );
    temp_data = response.data;
  } catch (e) {
    console.error(e);
  } finally {
    return await temp_data;
  }
};
</script>

<template>
  <div class="flex justify-center h-dvh bg-[#908c13]">
    <div
      class="self-center bg-slate-100 rounded-md p-12 w-1/3"
      v-if="isPasswordVerify"
    >
      <div class="flex justify-center mg-3">
        <NuxtImg src="../public/img/logo.png" class="w-16 mb-2" />
      </div>
      <h1 class="font-bold text-2xl mb-5 text-center">
        Contract Management App
      </h1>
      <section class="">
        <label class="font-semibold tracking-wide text-black" for="email"
          >Email</label
        >
        <br />
        <input
          autofocus
          autocomplete="off"
          class="w-full p-2 py-3 mt-1 border-b-2 bg-transparent focus:outline-none"
          type="text"
          id="email"
          placeholder="Ex. admin@gmail.com"
          v-model="user.email.value"
        />
      </section>
      <section class="mt-3">
        <label class="font-semibold tracking-wide text-black" for="password"
          >Password</label
        >
        <br />
        <div class="relative">
          <input
            autocomplete="off"
            class="w-full p-2 py-3 mt-1 border-b-2 bg-transparent focus:outline-none"
            :type="sawPassword ? 'text' : 'password'"
            id="password"
            placeholder="Password"
            v-model="user.password.value"
          />
          <span
            class="pi absolute right-0 inset-y-1/2 cursor-pointer"
            :class="{ 'pi-eye': sawPassword, 'pi-eye-slash': !sawPassword }"
            @click="sawPassword = !sawPassword"
          ></span>
        </div>
      </section>
      <button
        class="p-2 w-full bg-[#908c13] text-white rounded-md mt-5"
        v-on:click="loginEmail(user)"
      >
        Login
      </button>
      <div class="flex mt-2">
        <hr class="w-full m-auto text-black" />
        <span class="px-2">or</span>
        <hr class="w-full m-auto text-black" />
      </div>
      <button
        class="p-2 w-full bg-white rounded-md text-left px-4 flex hover:bg-slate-200 transition-all"
        v-on:click="loginGoogle"
      >
        <img src="../assets/google-icon.webp" class="w-10" />
        <span class="text-gray-600 self-center pl-2">Login with Google</span>
      </button>
    </div>
    <div
      class="self-center bg-slate-100 rounded-md py-6 w-1/3"
      v-if="!isPasswordVerify"
    >
      <h1 class="font-bold text-2xl mb-5 text-center flex flex-col">
        Google 2FA Setup
      </h1>

      <!-- Step 1: Provide Setup Key -->
      <div class="self-center py-2 px-6">
        <h5 class="text-center font-semibold">Step 1: Copy the Setup Key</h5>
        <p class="mt-2 text-center">
          Enter this key in your Google Authenticator app:
        </p>
        <div
          class="mt-4 p-2 bg-white border rounded-md text-center font-mono text-lg"
        >
          {{ secret_key }}
        </div>
      </div>

      <!-- Step 2: Fill the require otp description -->
      <div class="self-center py-2 px-6">
        <h5 class="text-center font-semibold">Step 2: Enter Account Name</h5>
        <p class="mt-2 text-center">Account name can be filled anything</p>
      </div>

      <!-- Step 3: Verify OTP -->
      <div class="m-auto w-1/2 p-2 mt-5 flex flex-col">
        <h5 class="text-center font-semibold">Step 3: Enter OTP</h5>
        <input
          type="number"
          id="otp_number"
          v-model="otpInput"
          class="inputBox inputNum mt-2 p-2 border rounded-sm"
          placeholder="Your OTP Code"
        />
        <button
          @click="verifyOTP(secret_key)"
          class="bg-[#918c13] mt-5 p-2 text-white rounded-lg"
        >
          Verify OTP
        </button>
      </div>
    </div>
  </div>
  <Toast />
</template>
