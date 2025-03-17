import { createRouter, createWebHistory } from "vue-router";
import { useCookies } from "vue3-cookies";
import Home from "../views/Home.vue";
import AddContract from "../views/AddContract.vue";
import ContractList from "../views/ContractList.vue";
import ContractDetail from "../views/ContractDetail.vue";
import Login from "../views/Login.vue";
import AuditLog from "../views/AuditLog.vue";
import EditContract from "../views/EditContract.vue";
import PrincipalList from "../views/masterData/PrincipalList.vue";
import PeriodList from "../views/masterData/PeriodList.vue";
import ProductCategory from "../views/masterData/ProductCategory.vue";
import CustomerList from "../views/masterData/CustomerList.vue";
import CMList from "../views/masterData/CMList.vue";
import PMList from "../views/masterData/PMList.vue";
import UserManagementPages from "../views/UserManagement.vue";
import UserDetails from "../views/UserDetails.vue";
import UploadFile from "../views/UploadFile.vue";
import TestDropDown from "../views/TestDropDown.vue";
import { userManagement } from "../pinia";
import UserProfile from "../views/UserProfile.vue";
import TestAuth from "../views/TestAuth.vue";
import ImplementationList from "../views/masterData/Implementation.vue";

const { cookies } = useCookies();
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { roles: ["Sales Admin", "Sales", "Super Admin", "Helpdesk"] },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/addcontract",
    name: "AddContract",
    component: AddContract,
    meta: { roles: ["Sales Admin"] },
  },
  {
    path: "/contracts/:id/edit",
    name: "EditContract",
    component: EditContract,
    meta: { roles: ["Sales Admin", "Sales"] },
  },
  {
    path: "/contracts",
    name: "Contracts",
    component: ContractList,
    meta: { roles: ["Sales Admin", "Sales", "Helpdesk", "Super Admin"] },
  },
  {
    path: "/contracts/:id",
    name: "ContractDetail",
    component: ContractDetail,
    meta: { roles: ["Sales Admin", "Sales", "Helpdesk", "Super Admin"] },
  },
  {
    path: "/audit-log",
    name: "AuditLog",
    component: AuditLog,
    meta: { roles: ["Sales Admin", "Sales", "Helpdesk", "Super Admin"] },
  },
  {
    path: "/uploadTest/",
    name: "UploadFile",
    component: UploadFile,
  },
  {
    path: "/brand",
    name: "Brand",
    component: PrincipalList,
    meta: { roles: ["Sales Admin"] },
  },
  {
    path: "/periode",
    name: "Periode",
    component: PeriodList,
    meta: { roles: ["Sales Admin"] },
  },
  {
    path: "/category",
    name: "Category",
    component: ProductCategory,
    meta: { roles: ["Sales Admin"] },
  },
  {
    path: "/customer",
    name: "Customer",
    component: CustomerList,
    meta: { roles: ["Sales Admin"] },
  },
  {
    path: "/cm_by",
    name: "CM_By",
    component: CMList,
    meta: { roles: ["Sales Admin"] },
  },
  {
    path: "/implementation_by",
    name: "Implementation_By",
    component: ImplementationList,
    meta: { roles: ["Sales Admin"] },
  },
  {
    path: "/auth",
    name: "Auth Test",
    component: TestAuth,
  },
  {
    path: "/pm_by",
    name: "PM_By",
    component: PMList,
    meta: { roles: ["Sales Admin"] },
  },
  {
    path: "/user",
    name: "List User",
    component: UserManagementPages,
    meta: { roles: ["Super Admin"] },
  },
  {
    path: "/user/:id",
    name: "User Details",
    component: UserDetails,
    meta: { roles: ["Super Admin"] },
  },
  {
    path: "/profile/:id",
    name: "User Profile",
    component: UserProfile,
  },
  {
    path: "/dropdown",
    name: "Dropdown",
    component: TestDropDown,
  },
  {
    path: "/logout",
    name: "logout",
    beforeEnter: () => {
      const store = userManagement();
      cookies.remove("auth_token");
      store.setValue({
        pb_id: null,
        db_id: null,
        name: null,
        role: null,
      });
      localStorage.removeItem("pocketbase_auth");
      router.push("/login");
    },
  },
];
const router = createRouter({
  history: createWebHistory(),
  // @ts-ignore
  routes,
});

router.beforeEach((to, from, next) => {
  const store = userManagement();
  const temp_from = from;
  const authToken = cookies.get("auth_token");

  if (to.name === "Login") {
    next();
    return;
  }

  // if (!authToken) {
  //   next("/login");
  //   return;
  // }

  const userRole = store.role;
  const routeRoles = to.meta.roles;

  if (routeRoles == "Helpdesk") {
    next("/ContractList");
    return;
  }

  if (Array.isArray(routeRoles) && !routeRoles.includes(userRole)) {
    next("/");
    return;
  }
  next();
});

export default router;
