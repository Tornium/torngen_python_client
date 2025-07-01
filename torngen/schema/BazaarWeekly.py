import typing

from BazaarAdvancedItemSales import BazaarAdvancedItemSales
from BazaarBargainSales import BazaarBargainSales
from BazaarBulkSales import BazaarBulkSales
from BazaarDollarSales import BazaarDollarSales
from BazaarRecentFavorites import BazaarRecentFavorites
from BazaarTotalFavorites import BazaarTotalFavorites
from BazaarWeeklyCustomers import BazaarWeeklyCustomers
from BazaarWeeklyIncome import BazaarWeeklyIncome

from ..base_schema import BaseSchema


class BazaarWeekly(BaseSchema):

    trending: typing.List[BazaarRecentFavorites]
    top_grossing: typing.List[BazaarWeeklyIncome]
    most_popular: typing.List[BazaarTotalFavorites]
    dollar_sale: typing.List[BazaarDollarSales]
    busiest: typing.List[BazaarWeeklyCustomers]
    bulk: typing.List[BazaarBulkSales]
    bargain: typing.List[BazaarBargainSales]
    advanced_item: typing.List[BazaarAdvancedItemSales]
