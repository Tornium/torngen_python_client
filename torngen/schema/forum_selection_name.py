import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ForumSelectionName(BaseSchema):
    value: str | str
