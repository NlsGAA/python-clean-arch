from src.domain.entities.user_entity import UserEntity
from src.application.contracts.user_repository_contract import UserRepositoryContract

class UserRepository(UserRepositoryContract):
    def __init__(self, db):
        self.users = []

    def get_all(self) -> list[UserEntity]:
        return self.users

    def create(self, user: UserEntity) -> UserEntity:
        self.users.append(user)
        return user