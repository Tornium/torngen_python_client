import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_company import UserCompany
from .user_job import UserJob


@dataclass
class UserJobResponse(BaseSchema):
    """
    JSON object of `UserJobResponse`.
    """

    job: None | UserCompany | UserJob

    @staticmethod
    def parse(data):
        return UserJobResponse(
            job=BaseSchema.parse(data.get("job"), None | UserCompany | UserJob),
        )
