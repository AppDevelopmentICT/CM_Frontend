from fastapi import APIRouter, Header, status
from fastapi.responses import JSONResponse
from . import services as AuditServices
from utils.utils import decode_jwt, check_is_user_admin
from typing import Annotated

audit_route = APIRouter()

@audit_route.get("/audit", tags=['Audit Log'])
def get_all_audit_information(user_token: Annotated[str | None, Header(description="For authorization (Only Admin)")]):
    user_id = decode_jwt(user_token)
    if check_is_user_admin(user_id):
        return AuditServices.get_all_log()
    else:
        return JSONResponse({"message": "You're not authorize user"}, status_code=status.HTTP_401_UNAUTHORIZED)

@audit_route.get("/audit/user", tags=['Audit Log'])
def get_audit_information_by_user(user_token: Annotated[str | None, Header(description="For authorization")]):
    user_id = decode_jwt(user_token)
    return AuditServices.get_log_by_id(user_id)
    