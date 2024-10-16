from pydantic import BaseModel, Field

class RegisterRequest(BaseModel):
    id: str = Field(description="Unique identifier for the user.")
    username: str = Field(description="Username for the user.")
    password: str = Field(description="Password for the user's account.")
    email: str = Field(description="Email address of the user.")
    user_roles: str = Field(description="Roles assigned to the user.")
    isApprover: bool = Field(description="Indicates if the user has approver rights.", example=False)

class LoginResponse(BaseModel):
    access_token: str = Field(description="JWT token issued upon successful login.")

class LoginRequest(BaseModel):
    email: str = Field(description="Email address of the user.")
    password: str = Field(description="Password for the user's account.")

class GetProfile(BaseModel):
    user_id: str = Field(description="Unique identifier of the user whose profile is being requested.")

class RequestOTP(BaseModel):
    input_otp: int = Field(description="User input otp")