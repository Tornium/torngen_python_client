import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class KeySelectionName(BaseSchema):
    value: str | str
