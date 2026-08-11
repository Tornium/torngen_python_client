import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_position_id import CompanyPositionId


@dataclass
class TornCompanyPosition(BaseSchema):
    """
    JSON object of `TornCompanyPosition`.
    """

    working_stats: typing.TypedDict(
        "",
        {
            "required": typing.TypedDict(
                "", {"manual_labor": int, "intelligence": int, "endurance": int}
            ),
            "daily_gains": typing.TypedDict(
                "", {"manual_labor": int, "intelligence": int, "endurance": int}
            ),
        },
    )
    name: str
    id: CompanyPositionId
    description: str
    ability: str

    @staticmethod
    def parse(data):
        return TornCompanyPosition(
            working_stats=BaseSchema.parse(
                data.get("working_stats"),
                typing.TypedDict(
                    "",
                    {
                        "required": typing.TypedDict(
                            "",
                            {
                                "manual_labor": int,
                                "intelligence": int,
                                "endurance": int,
                            },
                        ),
                        "daily_gains": typing.TypedDict(
                            "",
                            {
                                "manual_labor": int,
                                "intelligence": int,
                                "endurance": int,
                            },
                        ),
                    },
                ),
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), CompanyPositionId),
            description=BaseSchema.parse(data.get("description"), str),
            ability=BaseSchema.parse(data.get("ability"), str),
        )
