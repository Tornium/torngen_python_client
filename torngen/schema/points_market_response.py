import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PointsMarketResponse(BaseSchema):
    """
    JSON object of `PointsMarketResponse`.
    """

    pointsmarket: typing.List[
        typing.TypedDict(
            "", {"total_cost": int, "quantity": int, "id": int, "cost": int}
        )
    ]

    @staticmethod
    def parse(data):
        return PointsMarketResponse(
            pointsmarket=BaseSchema.parse(
                data.get("pointsmarket"),
                typing.List[
                    typing.TypedDict(
                        "", {"total_cost": int, "quantity": int, "id": int, "cost": int}
                    )
                ],
            ),
        )
