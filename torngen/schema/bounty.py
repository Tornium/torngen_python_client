import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class Bounty(BaseSchema):
    """
    JSON object of `Bounty`.
    """

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

    @staticmethod
    def parse(data):
        return Bounty(
            valid_until=BaseSchema.parse(data.get("valid_until"), int),
            target_name=BaseSchema.parse(data.get("target_name"), str),
            target_level=BaseSchema.parse(data.get("target_level"), int),
            target_id=BaseSchema.parse(data.get("target_id"), UserId),
            reward=BaseSchema.parse(data.get("reward"), int),
            reason=BaseSchema.parse(data.get("reason"), None | str),
            quantity=BaseSchema.parse(data.get("quantity"), int),
            lister_name=BaseSchema.parse(data.get("lister_name"), None | str),
            lister_id=BaseSchema.parse(data.get("lister_id"), None | UserId),
            is_anonymous=BaseSchema.parse(data.get("is_anonymous"), bool),
        )
