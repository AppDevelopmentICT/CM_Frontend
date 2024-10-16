from fastapi import APIRouter, Header
from . import schema, service as MaintenanceService
from typing import Annotated, Optional

maintenance_router = APIRouter()

@maintenance_router.post('/maintenance', tags=['Maintenance'])
async def add_maintenance_data(request: schema.AddMaintenance, project_id: Annotated[str, Header()]):
    get_add_maintenance_data_response = MaintenanceService.add_maintenance_data(request, project_id)
    return get_add_maintenance_data_response

@maintenance_router.patch('/maintenance', tags=['Maintenance'])
async def update_maintenance_data(
    request: schema.AddMaintenance, 
    project_id: Annotated[str, Header()],
    pm_id: Annotated[Optional[str], Header()] = None,
    cm_id: Annotated[Optional[str], Header()] = None,
    sla_id: Annotated[Optional[str], Header()] = None,
    implementation_id: Annotated[Optional[str], Header()] = None
    ):
    get_update_maintenance_data_response = MaintenanceService.update_maintenance_data(request, project_id, pm_id, cm_id, sla_id, implementation_id)
    return get_update_maintenance_data_response

@maintenance_router.patch('/parent-maintenance', tags=['Maintenance'])
async def update_maintenance_data(request: schema.AddMaintenance, project_id: Annotated[str, Header()]):
    get_update_maintenance_data_response = MaintenanceService.update_parent_maintenance(request, project_id)
    return get_update_maintenance_data_response

@maintenance_router.post('/maintenance/pm', tags=['Maintenance'])
async def create_pm(request: schema.PreventiveMaintenance, project_id: Annotated[str, Header()]):
    get_create_pm_response = MaintenanceService.create_pm(request, project_id)
    return get_create_pm_response

@maintenance_router.post('/maintenance/cm', tags=['Maintenance'])
async def create_cm(request: schema.CorrectiveMaintenance, project_id: Annotated[str, Header()]):
    get_create_cm_response = MaintenanceService.create_cm(request, project_id)
    return get_create_cm_response

@maintenance_router.post('/maintenance/sla', tags=['Maintenance'])
async def create_sla(request: schema.SLA, project_id: Annotated[str, Header()]):
    get_create_sla_response = MaintenanceService.create_sla(request, project_id)
    return get_create_sla_response

@maintenance_router.post('/maintenance/implementation', tags=['Maintenance'])
async def create_implementation(request: schema.Implementation, project_id: Annotated[str, Header()]):
    get_create_implementation_response = MaintenanceService.create_implementation(request, project_id)
    return get_create_implementation_response

@maintenance_router.get('/maintenance/pm', tags=['Maintenance'])
async def get_parent_pm(project_id: Annotated[str, Header()]):
    get_get_parent_pm_response = MaintenanceService.get_parent_pm(project_id)
    return get_get_parent_pm_response

@maintenance_router.get('/maintenance/cm', tags=['Maintenance'])
async def get_parent_cm(project_id: Annotated[str, Header()]):
    get_get_parent_cm_response = MaintenanceService.get_parent_cm(project_id)
    return get_get_parent_cm_response

@maintenance_router.get('/maintenance/sla', tags=['Maintenance'])
async def get_parent_sla(project_id: Annotated[str, Header()]):
    get_get_parent_sla_response = MaintenanceService.get_parent_sla(project_id)
    return get_get_parent_sla_response

@maintenance_router.get('/maintenance/implementation', tags=['Maintenance'])
async def get_parent_implementation(project_id: Annotated[str, Header()]):
    get_get_parent_implementation_response = MaintenanceService.get_parent_implementation(project_id)
    return get_get_parent_implementation_response

@maintenance_router.patch('/maintenance/pm', tags=['Maintenance'])
async def update_pm(request: schema.PreventiveMaintenance, id: Annotated[str, Header()]):
    get_update_pm_response = MaintenanceService.update_pm(request, id)
    return get_update_pm_response

@maintenance_router.patch('/maintenance/cm', tags=['Maintenance'])
async def update_cm(request: schema.CorrectiveMaintenance, id: Annotated[str, Header()]):
    get_update_cm_response = MaintenanceService.update_cm(request, id)
    return get_update_cm_response

@maintenance_router.patch('/maintenance/sla', tags=['Maintenance'])
async def update_sla(request: schema.SLA, id: Annotated[str, Header()]):
    get_update_sla_response = MaintenanceService.update_sla(request, id)
    return get_update_sla_response

@maintenance_router.patch('/maintenance/implementation', tags=['Maintenance'])
async def update_implementation(request: schema.Implementation, id: Annotated[str, Header()]):
    get_update_implementation_response = MaintenanceService.update_implementation(request, id)
    return get_update_implementation_response

@maintenance_router.get('/maintenance/pm/{project_id}', tags=['Maintenance'])
async def get_list_pm_by_project(project_id: str):
    get_get_list_pm_by_project_response = MaintenanceService.get_list_pm_by_project(project_id)
    return get_get_list_pm_by_project_response

@maintenance_router.get('/maintenance/cm/{project_id}', tags=['Maintenance'])
async def get_list_cm_by_project(project_id: str):
    get_get_list_cm_by_project_response = MaintenanceService.get_list_cm_by_project(project_id)
    return get_get_list_cm_by_project_response

@maintenance_router.get('/maintenance/sla/{project_id}', tags=['Maintenance'])
async def get_list_sla_by_project(project_id: str):
    get_get_list_sla_by_project_response = MaintenanceService.get_list_sla_by_project(project_id)
    return get_get_list_sla_by_project_response

@maintenance_router.get('/maintenance/implementation/{project_id}', tags=['Maintenance'])
async def get_list_implementation_by_project(project_id: str):
    get_get_list_implementation_by_project_response = MaintenanceService.get_list_implementation_by_project(project_id)
    return get_get_list_implementation_by_project_response