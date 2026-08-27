from src.application.contracts.user_repository_contract import UserRepositoryContract

class GetUsersUseCase:
    def __init__(self, repository: UserRepositoryContract):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()