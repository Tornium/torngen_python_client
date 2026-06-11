import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_customers import CompanyCustomers
from .company_employees import CompanyEmployees
from .company_id import CompanyId
from .company_income import CompanyIncome
from .company_type import CompanyType


@dataclass
class CompanySearchProfile(BaseSchema):
    """
    JSON object of `CompanySearchProfile`.
    """

    type: CompanyType
    rating: int
    name: str
    income: CompanyIncome
    image: None | str
    id: CompanyId
    employees: CompanyEmployees
    days_old: int
    customers: CompanyCustomers
    created_at: int
    applications_allowed: bool

    @staticmethod
    def parse(data):
        return CompanySearchProfile(
            type=BaseSchema.parse(data.get("type"), CompanyType),
            rating=BaseSchema.parse(data.get("rating"), int),
            name=BaseSchema.parse(data.get("name"), str),
            income=BaseSchema.parse(data.get("income"), CompanyIncome),
            image=BaseSchema.parse(data.get("image"), None | str),
            id=BaseSchema.parse(data.get("id"), CompanyId),
            employees=BaseSchema.parse(data.get("employees"), CompanyEmployees),
            days_old=BaseSchema.parse(data.get("days_old"), int),
            customers=BaseSchema.parse(data.get("customers"), CompanyCustomers),
            created_at=BaseSchema.parse(data.get("created_at"), int),
            applications_allowed=BaseSchema.parse(
                data.get("applications_allowed"), bool
            ),
        )
