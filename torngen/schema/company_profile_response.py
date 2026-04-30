import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_profile import CompanyProfile


@dataclass
class CompanyProfileResponse(BaseSchema):
    """
    JSON object of `CompanyProfileResponse`.
    """

    profile: CompanyProfile

    @staticmethod
    def parse(data):
        return CompanyProfileResponse(
            profile=BaseSchema.parse(data.get("profile"), CompanyProfile),
        )
