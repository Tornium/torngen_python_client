from ..base_schema import BaseSchema


class AttackCode(BaseSchema):
    value: str

    def parse(data):
        if not isinstance(data, str):
            raise TypeError(f"Expected type {str}, but got type {type(data)}")
        return BaseSchema.parse(data, str)
