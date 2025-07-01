import typing

from PropertyTypeId import PropertyTypeId

from ..base_schema import BaseSchema


class BasicProperty(BaseSchema):

    name: str
    id: PropertyTypeId
