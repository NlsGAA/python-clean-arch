import re
from dataclasses import dataclass
from src.domain.exceptions.invalid_email_error import InvalidEmailError

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

@dataclass
class UserEntity:
    username: str
    email: str
    password: str

    def __post_init__(self):
        if not EMAIL_REGEX.match(self.email):
            raise InvalidEmailError(self.email)