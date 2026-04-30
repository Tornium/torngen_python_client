import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class CompanyEmployeeEffectiveness(BaseSchema):
    """
    JSON object of `CompanyEmployeeEffectiveness`.
    """

    wrong_gender: int
    working_stats: int
    total: int
    settled_in: int
    merits: int
    management: int
    inactivity: int
    director_education: int
    book: int
    addiction: int

    @staticmethod
    def parse(data):
        return CompanyEmployeeEffectiveness(
            wrong_gender=BaseSchema.parse(data.get("wrong_gender"), int),
            working_stats=BaseSchema.parse(data.get("working_stats"), int),
            total=BaseSchema.parse(data.get("total"), int),
            settled_in=BaseSchema.parse(data.get("settled_in"), int),
            merits=BaseSchema.parse(data.get("merits"), int),
            management=BaseSchema.parse(data.get("management"), int),
            inactivity=BaseSchema.parse(data.get("inactivity"), int),
            director_education=BaseSchema.parse(data.get("director_education"), int),
            book=BaseSchema.parse(data.get("book"), int),
            addiction=BaseSchema.parse(data.get("addiction"), int),
        )
