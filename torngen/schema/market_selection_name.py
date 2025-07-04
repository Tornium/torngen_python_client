import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class MarketSelectionName(BaseSchema):
    value: str | str
