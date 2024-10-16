from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, timedelta

class ProjectType(str, Enum):
    contract = "Contract"
    purchase_order = "Purchase Order"
    spk = "SPK"
    other = "Other"

class Project(BaseModel):
    cost_sheets: str = Field(description="Reference number for the cost sheets.", example='123/2003/09')
    project_name: str = Field(description="Name of the project.", example='Membuat Aplikasi Contract Manangement')
    project_type: str = Field(description="Type of the project.", example=ProjectType.contract)
    description: str = Field(description="Detailed description of the project.")
    contract_number: str = Field(description="Contract number associated with the project.", example='08/XX/19/2023')
    internal_cost: int = Field(description="Internal cost incurred for the project.", example=120000000)
    selling_prices: int = Field(description="Selling price of the project.", example=500000000)
    customer_id: str = Field(description="Unique identifier for the customer.", example='71629acd-7e45-403f-ae1b-1ac65fa9575a')
    created_by: str = Field(description="Identifier of the user who created the project.", example='vph3cnfmwdkzr57')
    sales_person: str = Field(description="Identifier of the sales person responsible for the project.", example='zqazvowi0f5dskt')
    on_site_engineer: bool = Field(description="Indicates if an on-site engineer is required for the project.", example=False)
    project_status: str = Field(description="Current status of the project.", example='Pending')

class UpdateProject(BaseModel):
    cost_sheets: str = Field(description="Updated reference number for the cost sheets.", example='123/2043/09')
    project_name: str = Field(description="Updated name of the project.", example='Change Name')
    project_type: str = Field(description="Updated type of the project.", example=ProjectType.contract)
    description: str = Field(description="Updated detailed description of the project.")
    contract_number: str = Field(description="Updated contract number associated with the project.", example='08/XX/19/2023')
    internal_cost: int = Field(description="Updated internal cost incurred for the project.", example=120000000)
    selling_prices: int = Field(description="Updated selling price of the project.", example=500000000)
    customer_id: str = Field(description="Updated unique identifier for the customer.", example='71629acd-7e45-403f-ae1b-1ac65fa9575a')
    sales_person: str = Field(description="Updated identifier of the sales person responsible for the project.", example='zqazvowi0f5dskt')
    on_site_engineer: bool = Field(description="Indicates if an on-site engineer is still required for the project.", example=False)
    project_status: str = Field(description="Updated current status of the project.", example='Pending')
