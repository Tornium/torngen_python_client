import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeDetailsCracking(BaseSchema):
    """
    JSON object of `UserCrimeDetailsCracking`.
    """

    highest_mips: int
    encryption_layers_broken: int
    chars_guessed_total: int
    chars_guessed: int
    brute_force_cycles: int

    @staticmethod
    def parse(data):
        return UserCrimeDetailsCracking(
            highest_mips=BaseSchema.parse(data.get("highest_mips"), int),
            encryption_layers_broken=BaseSchema.parse(
                data.get("encryption_layers_broken"), int
            ),
            chars_guessed_total=BaseSchema.parse(data.get("chars_guessed_total"), int),
            chars_guessed=BaseSchema.parse(data.get("chars_guessed"), int),
            brute_force_cycles=BaseSchema.parse(data.get("brute_force_cycles"), int),
        )
