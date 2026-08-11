import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_special_id import CompanySpecialId


@dataclass
class TornCompanySpecial(BaseSchema):
    """
    JSON object of `TornCompanySpecial`.
    """

    rating: int
    name: str
    id: CompanySpecialId
    effect: str
    cost: int

    @staticmethod
    def parse(data):
        return TornCompanySpecial(
            rating=BaseSchema.parse(data.get("rating"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), CompanySpecialId),
            effect=BaseSchema.parse(data.get("effect"), str),
            cost=BaseSchema.parse(data.get("cost"), int),
        )
