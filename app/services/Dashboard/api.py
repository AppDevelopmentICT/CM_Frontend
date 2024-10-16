from fastapi import APIRouter, Header
from . import schema, service as DashboardService
from typing import Annotated, Union

dashboard_router = APIRouter()

@dashboard_router.get('/dashboard/customer', tags=['Dasboard'])
async def get_total_customer():
    get_total_customer_response = DashboardService.get_total_customer()
    return get_total_customer_response

@dashboard_router.get('/dashboard/project', tags=['Dasboard'])
async def get_project(user: Annotated[Union[str, None], Header()] = None):
    get_project_response = DashboardService.get_project(user)
    return get_project_response

@dashboard_router.get('/dashboard/pending-project', tags=['Dasboard'])
async def get_pending_project(user: Annotated[Union[str, None], Header()] = None):
    get_pending_project_response = DashboardService.get_pending_project(user)
    return get_pending_project_response

@dashboard_router.get('/dashboard/total-created', tags=['Dasboard'])
async def get_total_created_project(user: Annotated[str, Header()]):
    get_total_created_project_response = DashboardService.get_total_created_project(user)
    return get_total_created_project_response

@dashboard_router.get('/dashboard/top-customers', tags=['Dasboard'])
async def get_top_customer_project():
    get_top_customer_project_response = DashboardService.get_top_customer_project()
    return get_top_customer_project_response

@dashboard_router.get('/dashboard/created-by/{id}', tags=['Dasboard'])
async def get_project_by_sales(id: str):
    get_project_by_sales_response = DashboardService.get_project_by_sales(id)
    return get_project_by_sales_response

@dashboard_router.get('/dashboard/project-run', tags=['Dasboard'])
async def get_running_project(user_id: Annotated[Union[str, None], Header()] = None):
    get_running_project_response = DashboardService.get_running_project(user_id)
    return get_running_project_response

@dashboard_router.get('/dashboard/dashboard-diff', tags=['Dasboard'])
async def get_dashboard_diff(user_id: Annotated[Union[str, None], Header()] = None):
    get_dashboard_diff_response = DashboardService.get_dashboard_diff(user_id)
    return get_dashboard_diff_response

@dashboard_router.get('/user-dashboard/project', tags=['Dashboard - User'])
async def get_user_total_project(user: Annotated[str, Header()]):
    get_user_total_project_response = DashboardService.get_user_total_project(user)
    return get_user_total_project_response

@dashboard_router.get('/user-dashboard/approved', tags=['Dashboard - User'])
async def get_total_approve(user: Annotated[str, Header()]):
    get_total_approve_response = DashboardService.get_total_approve(user)
    return get_total_approve_response