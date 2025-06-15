import typing

from ..base_schema import BaseSchema


class ReportStats(BaseSchema):

    total: None | int
    strength: None | int
    speed: None | int
    dexterity: None | int
    defense: None | int
