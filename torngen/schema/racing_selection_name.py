import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class RacingSelectionName(BaseSchema):
    value: str | str
