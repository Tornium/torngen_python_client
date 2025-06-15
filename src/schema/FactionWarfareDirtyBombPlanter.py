import typing

from UserId import UserId

from ..base_schema import BaseSchema


class FactionWarfareDirtyBombPlanter(BaseSchema):

    name: str
    id: UserId
