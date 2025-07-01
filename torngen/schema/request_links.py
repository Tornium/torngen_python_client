import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class RequestLinks(BaseSchema):
    """
    JSON object of `RequestLinks`.
    """

    prev: None | str
    next: None | str

    @staticmethod
    def parse(data):
        return RequestLinks(
            prev=BaseSchema.parse(data.get("prev"), None | str),
            next=BaseSchema.parse(data.get("next"), None | str),
        )
