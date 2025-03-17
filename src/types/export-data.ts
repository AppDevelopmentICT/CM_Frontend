export type ExportData = {
  // project information
  customer_name: string;
  sales_name: string;
  cost_sheet: string;
  project_name: string;

  // contract desc
  project_type: string;
  contract_number: string;
  managed_service: boolean;
  internal_cost: number;
  selling_cost: number;

  // pm
  pm_by: string;
  maintenance_period: string;
  pm_quantity: number;
  pm_start_date: string;
  pm_end_date: string;

  // cm
  cm_by: string;
  cm_quantity: string;
  cm_start_date: string;
  cm_end_date: string;

  // implementation
  i_by: string;
  i_start_date: string;
  i_end_date: string;

  // product
  product_brand: string;
  product_type: string;
  product_name: string;
  serial_number: string;
  si_number: string;
  product_quantity: string;
  product_start_date: string;
  product_end_date: string;

  // sla
  severity1_response_time: string;
  severity1_resolution_time: string;
  severity2_response_time: string;
  severity2_resolution_time: string;
  severity3_response_time: string;
  severity3_resolution_time: string;
  severity4_response_time: string;
  severity4_resolution_time: string;

  project_description: string;
  created_date: string;
};
