from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Optional

class PreventiveMaintenance(BaseModel):
    pm_by: str = Field(description="Entity responsible for conducting preventive maintenance.", example='ICT')
    start_date: datetime = Field(description="Start date of the preventive maintenance period.", example=datetime.now())
    end_date: datetime = Field(description="End date of the preventive maintenance period.", example=datetime.now() + timedelta(days=365 * 2))
    pm_periode: str = Field(description="Periodicity of the preventive maintenance, e.g., Monthly, Quarterly, Semester.", example='Semester')
    quantity: str = Field(description="Duration or frequency of the preventive maintenance activities.", example="7 Days")
    
class CorrectiveMaintenance(BaseModel):
    cm_by: str = Field(description="Entity responsible for conducting corrective maintenance.", example='Other')
    start_date: datetime = Field(description="Start date of the corrective maintenance period.", example=datetime.now())
    end_date: datetime = Field(description="End date of the corrective maintenance period.", example=datetime.now() + timedelta(days=365 * 2))
    quantity: str = Field(description="Duration or frequency of the corrective maintenance activities.", example="7 Days")

class Implementation(BaseModel):
    implementation_type: str = Field(description="Type or method of implementation, e.g., By PMO, By Vendor.", example="By PMO")
    start_date: datetime = Field(description="Start date of the implementation.", example=datetime.now())
    end_date: datetime = Field(description="End date of the implementation.", example=datetime.now())
    
class SLA(BaseModel):
    severity_1_response_time: Optional[str] = Field(description="Response time for severity level 1 issues.", default=None)
    severity_1_resolution_time: Optional[str] = Field(description="Resolution time for severity level 1 issues.", default=None)
    severity_2_response_time: Optional[str] = Field(description="Response time for severity level 2 issues.", default=None)
    severity_2_resolution_time: Optional[str] = Field(description="Resolution time for severity level 2 issues.", default=None)
    severity_3_response_time: Optional[str] = Field(description="Response time for severity level 3 issues.", default=None)
    severity_3_resolution_time: Optional[str] = Field(description="Resolution time for severity level 3 issues.", default=None)
    severity_4_response_time: Optional[str] = Field(description="Response time for severity level 4 issues.", default=None)
    severity_4_resolution_time: Optional[str] = Field(description="Resolution time for severity level 4 issues.", default=None)

class AddMaintenance(BaseModel):
    preventive_maintenance: Optional[PreventiveMaintenance] = Field(description="Details of preventive maintenance activities.", default=None, example=None)
    corrective_maintenance: Optional[CorrectiveMaintenance] = Field(description="Details of corrective maintenance activities.", default=None, example=None)
    sla: Optional[SLA] = Field(description="Service Level Agreement details.", default=None, example=None)
    implementation: Optional[Implementation] = Field(description="Details of implementation activities.", default=None, example=None)
