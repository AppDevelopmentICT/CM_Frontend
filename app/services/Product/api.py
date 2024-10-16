from fastapi import APIRouter, Header
from . import schema, service as ProductService
from typing import Annotated, Optional

product_router = APIRouter()

@product_router.post('/product/project/{project_id}', tags=['Product'])
async def add_product(
    request: schema.Product, 
    project_id: str,
    project_name: Annotated[str, Header()],
    user_token: Annotated[str, Header()],
    pm_id: Annotated[Optional[str], Header()] = None,
    cm_id: Annotated[Optional[str], Header()] = None,
    sla_id: Annotated[Optional[str], Header()] = None,
    implementation_id: Annotated[Optional[str], Header()] = None,
    ):
    add_product_response = ProductService.add_product(request, project_id, project_name, user_token, 
                                                      pm_id, cm_id, sla_id, 
                                                      implementation_id)
    return add_product_response

@product_router.patch('/product/{product_id}', tags=['Product'])
async def edit_product(request: schema.Product, product_id: str, user_token: Annotated[str, Header()]):
    edit_product_response = ProductService.edit_product(request, product_id, user_token)
    return edit_product_response

@product_router.delete('/product/{product_id}', tags=['Product'])
async def delete_product(product_id: str, user_token: Annotated[str, Header()]):
    delete_product_response = ProductService.delete_product(product_id, user_token)
    return delete_product_response

@product_router.get('/product', tags=['Product'])
async def get_all_product():
    get_all_product_response = ProductService.get_all_product()
    return get_all_product_response