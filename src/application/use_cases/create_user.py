from src.domain.entities.user_entity import UserEntity
from src.application.dtos.create_user_dto import CreateUserDto
from src.application.contracts.user_repository_contract import UserRepositoryContract

class CreateUserUseCase:
    def __init__(self, repository: UserRepositoryContract):
        self.repository = repository

    def execute(self, user: CreateUserDto) -> UserEntity:
        user_entity = UserEntity(
            username=user.username,
            email=user.email,
            password=user.password
        )

        self.repository.create(user_entity)
        return user_entity