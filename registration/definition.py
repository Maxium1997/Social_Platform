from enum import Enum


class Gender(Enum):
    Unset = (0b0, 'Unset')
    Male = (0b1, 'Male')
    Female = (0b10, 'Female')
    Privacy = (0b100, 'Privacy')
