from ..base_schema import BaseSchema


class RaceStatusEnum(BaseSchema):

    values = [
        "open",
        "in_progress",
        "finished",
    ]
