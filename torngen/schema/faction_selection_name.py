import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionSelectionName(BaseSchema):
    value: str | str
