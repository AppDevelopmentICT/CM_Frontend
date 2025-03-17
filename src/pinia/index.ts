import { defineStore } from "pinia";

export const userManagement = defineStore("user", {
  state: () => {
    return {
      pb_id: null,
      db_id: null,
      name: null,
      role: null,
    };
  },
  actions: {
    setValue(newValues: { pb_id?: any; db_id?: any; name?: any; role?: any }) {
      if (newValues.pb_id !== undefined) this.pb_id = newValues.pb_id;
      if (newValues.db_id !== undefined) this.db_id = newValues.db_id;
      if (newValues.name !== undefined) this.name = newValues.name;
      if (newValues.role !== undefined) this.role = newValues.role;
    },
    removeValue() {
      this.db_id = null;
      this.pb_id = null;
      this.role = null;
      this.name = null;
    },
  },
  persist: true,
});
