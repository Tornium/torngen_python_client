import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_selection_name import CompanySelectionName


@dataclass
class CompanyLookupResponse(BaseSchema):
    """
    JSON object of `CompanyLookupResponse`.
    """

    selections: typing.List[CompanySelectionName]

    @staticmethod
    def parse(data):
        return CompanyLookupResponse(
            selections=BaseSchema.parse(
                data.get("selections"), typing.List[CompanySelectionName]
            ),
        )
