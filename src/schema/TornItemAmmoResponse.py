import typing

from TornItemAmmo import TornItemAmmo

from ..base_schema import BaseSchema


class TornItemAmmoResponse(BaseSchema):

    itemammo: typing.List[TornItemAmmo]
