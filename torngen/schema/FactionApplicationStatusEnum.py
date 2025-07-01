from ..base_schema import BaseSchema


class FactionApplicationStatusEnum(BaseSchema):

    values = [
        "accepted",
        "declined",
        "withdrawn",
        "active",
    ]
