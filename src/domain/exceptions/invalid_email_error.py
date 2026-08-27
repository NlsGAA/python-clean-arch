class InvalidEmailError(ValueError):
    def __init__(self, email: str):
        super().__init__(f"E-mail inválido: {email}")