from uuid import uuid4


class User:
    def __init__(self, email: str, hashed_password: str):
        self.id = str(uuid4())
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = True
        self.is_superuser = False
        self.is_verified = False
