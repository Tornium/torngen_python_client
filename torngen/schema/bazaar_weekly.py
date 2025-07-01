import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .bazaar_advanced_item_sales import BazaarAdvancedItemSales
from .bazaar_bargain_sales import BazaarBargainSales
from .bazaar_bulk_sales import BazaarBulkSales
from .bazaar_dollar_sales import BazaarDollarSales
from .bazaar_recent_favorites import BazaarRecentFavorites
from .bazaar_total_favorites import BazaarTotalFavorites
from .bazaar_weekly_customers import BazaarWeeklyCustomers
from .bazaar_weekly_income import BazaarWeeklyIncome


@dataclass
class BazaarWeekly(BaseSchema):
    """
    JSON object of `BazaarWeekly`.
    """

    trending: typing.List[BazaarRecentFavorites]
    top_grossing: typing.List[BazaarWeeklyIncome]
    most_popular: typing.List[BazaarTotalFavorites]
    dollar_sale: typing.List[BazaarDollarSales]
    busiest: typing.List[BazaarWeeklyCustomers]
    bulk: typing.List[BazaarBulkSales]
    bargain: typing.List[BazaarBargainSales]
    advanced_item: typing.List[BazaarAdvancedItemSales]

    @staticmethod
    def parse(data):
        return BazaarWeekly(
            trending=BaseSchema.parse(
                data.get("trending"), typing.List[BazaarRecentFavorites]
            ),
            top_grossing=BaseSchema.parse(
                data.get("top_grossing"), typing.List[BazaarWeeklyIncome]
            ),
            most_popular=BaseSchema.parse(
                data.get("most_popular"), typing.List[BazaarTotalFavorites]
            ),
            dollar_sale=BaseSchema.parse(
                data.get("dollar_sale"), typing.List[BazaarDollarSales]
            ),
            busiest=BaseSchema.parse(
                data.get("busiest"), typing.List[BazaarWeeklyCustomers]
            ),
            bulk=BaseSchema.parse(data.get("bulk"), typing.List[BazaarBulkSales]),
            bargain=BaseSchema.parse(
                data.get("bargain"), typing.List[BazaarBargainSales]
            ),
            advanced_item=BaseSchema.parse(
                data.get("advanced_item"), typing.List[BazaarAdvancedItemSales]
            ),
        )
