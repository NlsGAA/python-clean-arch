from fastapi import APIRouter, Depends
from src.bootstrap import get_user_controller
from src.application.dtos.create_user_dto import CreateUserDto
from src.presentation.controllers.user_controller import UserController

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users(
    user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.get_all()

@router.post("/")
def read_users(
    user_dto: CreateUserDto,
    user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.create(user_dto)
