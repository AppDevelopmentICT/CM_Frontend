from fastapi import APIRouter, Header
from . import schema, service as ProjectService
from typing import Annotated, Union

project_router = APIRouter()

@project_router.post('/project', tags=['Project'])
async def add_project(request: schema.Project, user_token: Annotated[str, Header()]):
    add_project_response = await ProjectService.add_project(request, user_token)
    return add_project_response

@project_router.post('/project/submit/{id}', tags=['Project'])
async def submit_project(id: str, user_token: Annotated[str, Header()]):
    submit_project_response = await ProjectService.submit_project(id, user_token)
    return submit_project_response

@project_router.patch('/project/{id}', tags=['Project'])
async def update_project(request: schema.UpdateProject, id: str, user_token: Annotated[str, Header()]):
    update_project_response = await ProjectService.update_project(request, id, user_token)
    return update_project_response

@project_router.patch('/project/approve/{id}', tags=['Project'])
async def approve_project(id: str, user_id: Annotated[str, Header()]):
    approve_project_response = await ProjectService.approve_project(id, user_id)
    return approve_project_response

@project_router.patch('/project/reject/{id}', tags=['Project'])
async def reject_project(id: str, user_id: Annotated[str, Header()]):
    reject_project_response = await ProjectService.reject_project(id, user_id)
    return reject_project_response

@project_router.get('/project', tags=['Project'])
async def get_project_list(user: Annotated[Union[str, None], Header()] = None):
    get_project_list_response = ProjectService.get_project_list(user)
    return get_project_list_response

@project_router.get('/project/{id}', tags=['Project'])
async def get_project_by_id(id: str):
    get_project_by_id_response = ProjectService.get_project_by_id(id)
    return get_project_by_id_response

@project_router.get('/project/status/{status}', tags=['Project'])
async def get_pending_project(status: str):
    get_pending_project_response = ProjectService.get_pending_project(status)
    return get_pending_project_response

@project_router.get('/isApprover', tags=['Project'])
async def check_is_approver(user_id: Annotated[str, Header()], project_id: Annotated[str, Header()]):
    check_is_approver_response = ProjectService.check_is_approver(user_id, project_id)
    return check_is_approver_response