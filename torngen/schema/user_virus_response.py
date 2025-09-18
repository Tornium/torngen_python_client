import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_virus import UserVirus


@dataclass
class UserVirusResponse(BaseSchema):
    """
    JSON object of `UserVirusResponse`.
    """

    virus: None | UserVirus

    @staticmethod
    def parse(data):
        return UserVirusResponse(
            virus=BaseSchema.parse(data.get("virus"), None | UserVirus),
        )
