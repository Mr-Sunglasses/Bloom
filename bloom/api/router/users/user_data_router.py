from fastapi import APIRouter, status, Depends, Request
from ....services.security.hash_password import oauth2_scheme
from ....models.schemas.user_response_schema import UserResponse

router = APIRouter(
    prefix="/bloom/v1/info/user",
    tags=["users"],
    responses={404: {"description": "Not Found"}},
    dependencies=[Depends(oauth2_scheme)],
)


@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
def get_user_details(request: Request):
    return request.user
