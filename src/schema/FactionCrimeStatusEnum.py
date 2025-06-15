from ..base_schema import BaseSchema


class FactionCrimeStatusEnum(BaseSchema):

    values = [
        "Recruiting",
        "Planning",
        "Successful",
        "Failure",
        "Expired",
    ]
