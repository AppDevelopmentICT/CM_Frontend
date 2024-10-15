<template>
    <div class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-60 z-20" v-if="showDetail">
        <div class="bg-gray-200 rounded-lg p-10 w-[90%] h-[90%] overflow-auto">
            
                <h1>Product Detail</h1>
                <div class="subgroup">
                    <div class="grid grid-cols-2 gap-x-4 gap-y-4 ">
                        <div class="">
                            <label for="" class="block">Product</label>
                            <p>{{productDetail.product_category}}</p>
                        </div>

                        <div class="">
                            <label for="" class="block">Brand</label>
                            <p>{{ productDetail.principal_name }}</p>
                        </div>
                        
                        <div class="">
                            <label for="" class="block" >Product Name</label>
                            <p>{{ productDetail.product_name }}</p>
                        </div>

                        <div class="">
                            <div class="flex items-center">
                                <label for="" class="block">Serial Number
                                    <span v-show="productDetail.serial_number==''">
                                        <i class="pi pi-exclamation-circle text-[#908c13]"></i>
                                    </span>
                                </label>
                            </div>
                            <p v-if="productDetail.serial_number==''">-</p>
                            <p v-else>{{ productDetail.serial_number }}</p>
                        </div>
                        
                        <div class="">
                            <div class="flex items-center">
                                <label for="" class="block">SI Number
                                    <span v-show="productDetail.si_number==''">
                                        <i class="pi pi-exclamation-circle text-[#908c13]"></i>
                                    </span>
                                </label>
                            </div>
                            <p v-if="productDetail.si_number==''">-</p>
                            <p v-else>{{ productDetail.si_number }}</p>
                        </div>
                        
                        <div class="">
                            <label for="" class="block">Quantity</label>
                            <p>{{ productDetail.quantity }}</p>
                        </div>

                        <div class="">
                            <label for="" class="block">Start Date</label>
                            <p>{{ productDetail.start_date }}</p>
                        </div>

                        <div class="">
                            <label for="" class="block">End Date</label>
                            <p>{{ productDetail.end_date }}</p>
                        </div>            
                    </div>
                </div>
                 <div class="grid grid-cols-2 gap-x-4 gap-y-4">
                    <div class="subgroup">
                        <h2>Preventive Maintenance</h2>
                         
                        <div >
                            <div class="pb-4">
                                <label for="" class="block">Maintenance By</label>
                                <p>{{ productDetail.preventive_maintenance.pm_by }}</p>
                            </div> 
                            <div v-if="productDetail.preventive_maintenance.pm_by != 'None'" class="grid grid-cols-2 gap-4">
                                <div class="">
                                    <label for="" class="block">Start Date</label>
                                    <p>{{ productDetail.preventive_maintenance.start_date }}</p>
                                </div> 
                                <div class="">
                                    <label for="" class="block">End Date</label>
                                    <p>{{ productDetail.preventive_maintenance.end_date }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Maintenance Period</label>
                                    <p>{{ productDetail.preventive_maintenance.pm_periode }}</p>
                                </div>
                                <div class="">
                                    <label for="" class="block">Quantity</label>
                                    <p>{{ productDetail.preventive_maintenance.quantity }}</p>
                                </div>
                            </div>
                                  
                        </div>
                    </div>  
                    <div class="subgroup">
                        <h2>Corrective Maintenance</h2>
                        <div>
                            <div class="pb-4">
                                <label for="" class="block">Maintenance By</label>
                                <p>{{ productDetail.corrective_maintenance.cm_by }}</p>
                            </div>
                            <div v-if="productDetail.corrective_maintenance.cm_by != 'None'"  class="grid grid-cols-2 gap-4">
                                <div class="">
                                    <label for="" class="block">Start Date</label>
                                    <p>{{ productDetail.corrective_maintenance.start_date }}</p>
                                </div> 
                                <div class="">
                                    <label for="" class="block">End Date</label>
                                    <p>{{ productDetail.corrective_maintenance.end_date }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Quantity</label>
                                    <p>{{ productDetail.corrective_maintenance.quantity }}</p>
                                </div> 
                            </div> 
                                
                        </div> 
                    </div> 
                 </div> 
                 <div class="flex gap-4">
                    <div class="subgroup w-1/3">
                        <h2>Implementation</h2>
                        <div class="flex flex-col">
                            <div class="pb-4">
                                <label for="" class="block">Implementation</label>
                                <p>{{ productDetail.implementation.implementation_type }}</p>
                            </div>
                            <div v-show="productDetail.implementation.implementation_type!='None'" class="grid grid-cols-2 gap-4">
                                <div>
                                    <label for="" class="block">Start Date</label>
                                    <p >{{ productDetail.implementation.start_date }}</p>
                                </div>
                                <div>
                                    <label for="" class="block">end Date</label>
                                    <p >{{ productDetail.implementation.end_date }}</p>
                                </div>
                                
                            </div>    
                        </div>
                    </div>
                    <div class="subgroup w-full">
                        <h2>SLA</h2>
                            <div class="grid grid-cols-4">  
                                <div class="">
                                    <label for="" class="block">Severity 1 Response Time</label>
                                    <p v-show="productDetail.sla.severity_1_response_time==''">-</p>
                                    <p>{{ productDetail.sla.severity_1_response_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 1 Resolution Time</label>
                                    <p v-show="productDetail.sla.severity_1_resolution_time==''">-</p>
                                    <p>{{ productDetail.sla.severity_1_resolution_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 2 Response Time</label>
                                    <p v-show="productDetail.sla.severity_2_response_time==''">-</p>
                                    <p>{{ productDetail.sla.severity_2_response_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 2 Resolution Time</label>
                                    <p v-show="productDetail.sla.severity_2_resolution_time==''">-</p>
                                    <p>{{ productDetail.sla.severity_2_resolution_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 3 Response Time</label>
                                    <p v-show="productDetail.sla.severity_3_response_time==''">-</p>
                                    <p>{{ productDetail.sla.severity_3_response_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 3 Resolution Time</label>
                                    <p v-show="productDetail.sla.severity_3_resolution_time==''">-</p>
                                    <p>{{ productDetail.sla.severity_3_resolution_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 4 Response Time</label>
                                    <p v-show="productDetail.sla.severity_4_response_time==''">-</p>
                                    <p>{{ productDetail.sla.severity_4_response_time }}</p>
                                </div>  
                                <div class="">
                                    <label for="" class="block">Severity 4 Resolution Time</label>
                                    <p v-show="productDetail.sla.severity_4_resolution_time==''">-</p>
                                    <p>{{ productDetail.sla.severity_4_resolution_time }}</p>
                                </div>   
                            </div>
                        </div>
                 </div>
            <div>
                <button class="bg-red-600 text-white p-2 rounded-md " v-on:click="closeProductDetail">close</button>
            </div>
           
        </div>
    </div>
</template>

<script setup>
    let productDetail = defineModel('productDetail')
    let showDetail = defineModel('showDetail')


    const closeProductDetail = () => {
        showDetail.value=false
    }
</script>

<style lang="scss" scoped>

</style>