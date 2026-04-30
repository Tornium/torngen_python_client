import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .application_status_enum import ApplicationStatusEnum
from .company_application_player import CompanyApplicationPlayer


@dataclass
class CompanyApplication(BaseSchema):
    """
    JSON object of `CompanyApplication`.
    """

    status: ApplicationStatusEnum
    player: CompanyApplicationPlayer
    message: None | str
    expires_at: int

    @staticmethod
    def parse(data):
        return CompanyApplication(
            status=BaseSchema.parse(data.get("status"), ApplicationStatusEnum),
            player=BaseSchema.parse(data.get("player"), CompanyApplicationPlayer),
            message=BaseSchema.parse(data.get("message"), None | str),
            expires_at=BaseSchema.parse(data.get("expires_at"), int),
        )
