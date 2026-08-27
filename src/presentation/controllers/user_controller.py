
from src.application.dtos.create_user_dto import CreateUserDto
from src.application.use_cases.get_users import GetUsersUseCase
from src.application.use_cases.create_user import CreateUserUseCase
from src.application.contracts.user_repository_contract import UserRepositoryContract

class UserController:
    def __init__(self, repository: UserRepositoryContract):
        self.repository = repository

    def get_all(self):
        try:
            use_case = GetUsersUseCase(self.repository)
            return use_case.execute()
        except Exception as e:
            raise e

    def create(self, user_dto: CreateUserDto):
        try:
            use_case = CreateUserUseCase(self.repository)
            return use_case.execute(user_dto)
        except Exception as e:
            raise e