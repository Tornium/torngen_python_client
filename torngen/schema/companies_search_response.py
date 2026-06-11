import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_search_profile import CompanySearchProfile
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class CompaniesSearchResponse(BaseSchema):
    """
    JSON object of `CompaniesSearchResponse`.
    """

    search: typing.List[CompanySearchProfile]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return CompaniesSearchResponse(
            search=BaseSchema.parse(
                data.get("search"), typing.List[CompanySearchProfile]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
