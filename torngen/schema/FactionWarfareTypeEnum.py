from ..base_schema import BaseSchema


class FactionWarfareTypeEnum(BaseSchema):

    values = [
        "ranked",
        "territory",
        "raid",
        "chain",
        "db",
    ]
