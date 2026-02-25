import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .stock_id import StockId


@dataclass
class TornStock(BaseSchema):
    """
    JSON object of `TornStock`.
    """

    name: str
    market: typing.TypedDict(
        "", {"shares": int, "price": int | float, "investors": int, "cap": int}
    )
    images: typing.TypedDict("", {"logo": str, "full": str})
    id: StockId
    bonus: typing.TypedDict(
        "", {"requirement": int, "passive": bool, "frequency": int, "description": str}
    )
    acronym: str

    @staticmethod
    def parse(data):
        return TornStock(
            name=BaseSchema.parse(data.get("name"), str),
            market=BaseSchema.parse(
                data.get("market"),
                typing.TypedDict(
                    "",
                    {"shares": int, "price": int | float, "investors": int, "cap": int},
                ),
            ),
            images=BaseSchema.parse(
                data.get("images"), typing.TypedDict("", {"logo": str, "full": str})
            ),
            id=BaseSchema.parse(data.get("id"), StockId),
            bonus=BaseSchema.parse(
                data.get("bonus"),
                typing.TypedDict(
                    "",
                    {
                        "requirement": int,
                        "passive": bool,
                        "frequency": int,
                        "description": str,
                    },
                ),
            ),
            acronym=BaseSchema.parse(data.get("acronym"), str),
        )
