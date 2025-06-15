import typing

from UserId import UserId

from ..base_schema import BaseSchema


class Bounty(BaseSchema):

    valid_until: int
    target_name: str
    target_level: int
    target_id: UserId
    reward: int
    reason: None | str
    quantity: int
    lister_name: None | str
    lister_id: None | UserId
    is_anonymous: bool
