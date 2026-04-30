import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_customers import CompanyCustomers
from .company_director import CompanyDirector
from .company_employees import CompanyEmployees
from .company_id import CompanyId
from .company_income import CompanyIncome
from .company_type import CompanyType


@dataclass
class CompanyProfile(BaseSchema):
    """
    JSON object of `CompanyProfile`.
    """

    type: CompanyType
    rating: int
    name: str
    income: CompanyIncome
    image: str
    id: CompanyId
    employees: CompanyEmployees
    director: CompanyDirector
    days_old: int
    customers: CompanyCustomers
    created_at: int

    @staticmethod
    def parse(data):
        return CompanyProfile(
            type=BaseSchema.parse(data.get("type"), CompanyType),
            rating=BaseSchema.parse(data.get("rating"), int),
            name=BaseSchema.parse(data.get("name"), str),
            income=BaseSchema.parse(data.get("income"), CompanyIncome),
            image=BaseSchema.parse(data.get("image"), str),
            id=BaseSchema.parse(data.get("id"), CompanyId),
            employees=BaseSchema.parse(data.get("employees"), CompanyEmployees),
            director=BaseSchema.parse(data.get("director"), CompanyDirector),
            days_old=BaseSchema.parse(data.get("days_old"), int),
            customers=BaseSchema.parse(data.get("customers"), CompanyCustomers),
            created_at=BaseSchema.parse(data.get("created_at"), int),
        )
