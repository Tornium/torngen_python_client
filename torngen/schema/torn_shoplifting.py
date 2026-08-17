import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_shoplifting_security_status import TornShopliftingSecurityStatus
from .torn_sub_crime_id import TornSubCrimeId


@dataclass
class TornShoplifting(BaseSchema):
    """
    JSON object of `TornShoplifting`.
    """

    status: typing.List[TornShopliftingSecurityStatus]
    id: TornSubCrimeId

    @staticmethod
    def parse(data):
        return TornShoplifting(
            status=BaseSchema.parse(
                data.get("status"), typing.List[TornShopliftingSecurityStatus]
            ),
            id=BaseSchema.parse(data.get("id"), TornSubCrimeId),
        )
