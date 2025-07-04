import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class Parameters(BaseSchema):
    value: str | str
