import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserSelectionName(BaseSchema):
    value: str | str
