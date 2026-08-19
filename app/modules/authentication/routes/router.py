from fastapi import APIRouter
from app.modules.authentication.schemas.sign_up_schema import SignUpRequest, SignUpResponse
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/auth")

@router.post('/sign-up')
async def auth_sign_up(signup_request : SignUpRequest):
    return JSONResponse(
        status_code=200,
        content={
            "success" : True,
            "message" : None,
            "data" : []
        }
    )