import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .organized_crime_name import OrganizedCrimeName
from .torn_organized_crime_scope import TornOrganizedCrimeScope
from .torn_organized_crime_slot import TornOrganizedCrimeSlot
from .torn_organized_crime_spawn import TornOrganizedCrimeSpawn


@dataclass
class TornOrganizedCrime(BaseSchema):
    """
    JSON object of `TornOrganizedCrime`.
    """

    spawn: TornOrganizedCrimeSpawn
    slots: typing.List[TornOrganizedCrimeSlot]
    scope: TornOrganizedCrimeScope
    prerequisite: None | OrganizedCrimeName
    name: OrganizedCrimeName
    difficulty: int
    description: str

    @staticmethod
    def parse(data):
        return TornOrganizedCrime(
            spawn=BaseSchema.parse(data.get("spawn"), TornOrganizedCrimeSpawn),
            slots=BaseSchema.parse(
                data.get("slots"), typing.List[TornOrganizedCrimeSlot]
            ),
            scope=BaseSchema.parse(data.get("scope"), TornOrganizedCrimeScope),
            prerequisite=BaseSchema.parse(
                data.get("prerequisite"), None | OrganizedCrimeName
            ),
            name=BaseSchema.parse(data.get("name"), OrganizedCrimeName),
            difficulty=BaseSchema.parse(data.get("difficulty"), int),
            description=BaseSchema.parse(data.get("description"), str),
        )
