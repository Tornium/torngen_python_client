import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornSelectionName(BaseSchema):
    value: str | str
