import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionTerritoryOwnership(BaseSchema):

    owned_by: None | FactionId
    id: str
    acquired_at: None | int
