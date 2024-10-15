<template>
    <div>
        <h4 class="text-2xl font-semibold mb-3 text-[#908c13]">User Management</h4>
        <Accordion :multiple="true" :activeIndex="[0]">
            <AccordionTab header="Add User">
                <AddUser/>
            </AccordionTab>
            <AccordionTab header="User List">
                <UserList/>
            </AccordionTab>
        </Accordion>

    </div>
</template>

<script setup>
import UserList from '../components/User/UserList.vue';
import AddUser from '../components/User/AddUser.vue';
</script>