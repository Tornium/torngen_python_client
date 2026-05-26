import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_profile import CompanyProfile
from .request_metadata_with_links_and_total import RequestMetadataWithLinksAndTotal


@dataclass
class CompaniesResponse(BaseSchema):
    """
    JSON object of `CompaniesResponse`.
    """

    companies_timestamp: int
    companies_delay: int
    companies: typing.List[CompanyProfile]
    _metadata: RequestMetadataWithLinksAndTotal

    @staticmethod
    def parse(data):
        return CompaniesResponse(
            companies_timestamp=BaseSchema.parse(data.get("companies_timestamp"), int),
            companies_delay=BaseSchema.parse(data.get("companies_delay"), int),
            companies=BaseSchema.parse(
                data.get("companies"), typing.List[CompanyProfile]
            ),
            _metadata=BaseSchema.parse(
                data.get("_metadata"), RequestMetadataWithLinksAndTotal
            ),
        )
