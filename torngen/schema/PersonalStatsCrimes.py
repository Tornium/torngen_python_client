import typing

from PersonalStatsCrimesV1 import PersonalStatsCrimesV1
from PersonalStatsCrimesV2 import PersonalStatsCrimesV2

from ..base_schema import BaseSchema


class PersonalStatsCrimes(BaseSchema):

    crimes: PersonalStatsCrimesV2 | PersonalStatsCrimesV1
