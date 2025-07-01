from ..base_schema import BaseSchema


class ItemUid(BaseSchema):
    value: int

    def parse(data):
        if not isinstance(data, int):
            raise TypeError(f"Expected type {int}, but got type {type(data)}")
        return BaseSchema.parse(data, int)
