from src.models.user import User


def create_user(*, username: str = "username") -> User:
    return User(username=username)
