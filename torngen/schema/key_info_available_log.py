import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .log_category_id import LogCategoryId
from .log_id import LogId


@dataclass
class KeyInfoAvailableLog(BaseSchema):
    """
    JSON object of `KeyInfoAvailableLog`.
    """

    log_ids: typing.List[LogId]
    category_id: LogCategoryId

    @staticmethod
    def parse(data):
        return KeyInfoAvailableLog(
            log_ids=BaseSchema.parse(data.get("log_ids"), typing.List[LogId]),
            category_id=BaseSchema.parse(data.get("category_id"), LogCategoryId),
        )
