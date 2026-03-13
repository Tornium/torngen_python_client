import typing

from .trade_item_company import TradeItemCompany
from .trade_item_faction import TradeItemFaction
from .trade_item_item import TradeItemItem
from .trade_item_money import TradeItemMoney
from .trade_item_nap import TradeItemNap
from .trade_item_property import TradeItemProperty

TradeItem = (
    TradeItemNap
    | TradeItemProperty
    | TradeItemCompany
    | TradeItemFaction
    | TradeItemItem
    | TradeItemMoney
)
