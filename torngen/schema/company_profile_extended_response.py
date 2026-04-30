import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_profile_extended import CompanyProfileExtended


@dataclass
class CompanyProfileExtendedResponse(BaseSchema):
    """
    JSON object of `CompanyProfileExtendedResponse`.
    """

    profile: CompanyProfileExtended

    @staticmethod
    def parse(data):
        return CompanyProfileExtendedResponse(
            profile=BaseSchema.parse(data.get("profile"), CompanyProfileExtended),
        )
