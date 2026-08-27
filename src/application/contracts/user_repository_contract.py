from abc import ABC, abstractmethod
from src.domain.entities.user_entity import UserEntity

class UserRepositoryContract(ABC):
    @abstractmethod
    def get_all(self) -> list[UserEntity]:
        raise NotImplementedError

    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError