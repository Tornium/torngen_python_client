import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_type_id import CompanyTypeId
from .torn_company_position import TornCompanyPosition
from .torn_company_special import TornCompanySpecial
from .torn_company_stock import TornCompanyStock


@dataclass
class TornCompany(BaseSchema):
    """
    JSON object of `TornCompany`.
    """

    stock: typing.List[TornCompanyStock]
    specials: typing.List[TornCompanySpecial]
    positions: typing.List[TornCompanyPosition]
    name: str
    id: CompanyTypeId
    employees: int
    cost: int

    @staticmethod
    def parse(data):
        return TornCompany(
            stock=BaseSchema.parse(data.get("stock"), typing.List[TornCompanyStock]),
            specials=BaseSchema.parse(
                data.get("specials"), typing.List[TornCompanySpecial]
            ),
            positions=BaseSchema.parse(
                data.get("positions"), typing.List[TornCompanyPosition]
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), CompanyTypeId),
            employees=BaseSchema.parse(data.get("employees"), int),
            cost=BaseSchema.parse(data.get("cost"), int),
        )
