import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PropertySelectionName(BaseSchema):
    value: str | str
