import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .stock_id import StockId
from .torn_stock_history import TornStockHistory
from .torn_stock_performance import TornStockPerformance


@dataclass
class TornStockDetailed(BaseSchema):

    chart: typing.TypedDict(
        "",
        {
            "performance": typing.TypedDict(
                "",
                {
                    "last_year": TornStockPerformance,
                    "last_week": TornStockPerformance,
                    "last_month": TornStockPerformance,
                    "last_hour": TornStockPerformance,
                    "last_day": TornStockPerformance,
                    "all_time": TornStockPerformance,
                },
            ),
            "history": typing.List[TornStockHistory],
        },
    )
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
        return TornStockDetailed(
            chart=BaseSchema.parse(
                data.get("chart"),
                typing.TypedDict(
                    "",
                    {
                        "performance": typing.TypedDict(
                            "",
                            {
                                "last_year": TornStockPerformance,
                                "last_week": TornStockPerformance,
                                "last_month": TornStockPerformance,
                                "last_hour": TornStockPerformance,
                                "last_day": TornStockPerformance,
                                "all_time": TornStockPerformance,
                            },
                        ),
                        "history": typing.List[TornStockHistory],
                    },
                ),
            ),
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
