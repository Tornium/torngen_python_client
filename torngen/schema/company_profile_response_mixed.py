import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_profile import CompanyProfile
from .company_profile_extended import CompanyProfileExtended


@dataclass
class CompanyProfileResponseMixed(BaseSchema):
    """
    JSON object of `CompanyProfileResponseMixed`.
    """

    profile: CompanyProfileExtended | CompanyProfile

    @staticmethod
    def parse(data):
        return CompanyProfileResponseMixed(
            profile=BaseSchema.parse(
                data.get("profile"), CompanyProfileExtended | CompanyProfile
            ),
        )
