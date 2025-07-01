import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .property_type_id import PropertyTypeId


@dataclass
class BasicProperty(BaseSchema):
    """
    JSON object of `BasicProperty`.
    """

    name: str
    id: PropertyTypeId

    @staticmethod
    def parse(data):
        return BasicProperty(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), PropertyTypeId),
        )
