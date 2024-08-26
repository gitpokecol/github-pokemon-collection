from enum import Enum


class Gender(str, Enum):
    FEMALE = "female"
    MALE = "male"
    GENDERLESS = "genderless"

    def __str__(self) -> str:
        return self.value
