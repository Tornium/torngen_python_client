import typing

from FactionCrimeUser import FactionCrimeUser
from ItemId import ItemId

from ..base_schema import BaseSchema


class FactionCrimeSlot(BaseSchema):

    user: None | FactionCrimeUser
    position: str
    item_requirement: None | typing.TypedDict(
        "", {"is_reusable": bool, "is_available": bool, "id": ItemId}
    )
    checkpoint_pass_rate: int
