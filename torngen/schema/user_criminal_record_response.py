import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_criminal_record_v1 import UserCriminalRecordV1
from .user_criminal_record_v2 import UserCriminalRecordV2


@dataclass
class UserCriminalRecordResponse(BaseSchema):
    """
    JSON object of `UserCriminalRecordResponse`.
    """

    criminalrecord: UserCriminalRecordV1 | UserCriminalRecordV2

    @staticmethod
    def parse(data):
        return UserCriminalRecordResponse(
            criminalrecord=BaseSchema.parse(
                data.get("criminalrecord"), UserCriminalRecordV1 | UserCriminalRecordV2
            ),
        )
