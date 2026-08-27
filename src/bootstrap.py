from fastapi import Depends
from src.application.use_cases.get_users import GetUsersUseCase
from src.application.contracts.user_repository_contract import UserRepositoryContract
from src.domain.repositories.user_repository import UserRepository
from src.presentation.controllers.user_controller import UserController

def get_db_session():
    return "db_session_instance"

def get_user_repository(db = Depends(get_db_session)) -> UserRepositoryContract:
    return UserRepository(db)

user_controller = None

def get_user_controller(repository: UserRepositoryContract = Depends(get_user_repository)) -> UserController:
    global user_controller

    if user_controller is None:
        user_controller = UserController(repository)

    return user_controller

def get_user_use_case(repo: UserRepositoryContract = Depends(get_user_repository)) -> GetUsersUseCase:
    return GetUsersUseCase(repo)