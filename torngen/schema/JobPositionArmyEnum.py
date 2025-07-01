from ..base_schema import BaseSchema


class JobPositionArmyEnum(BaseSchema):

    values = [
        "Private",
        "Corporal",
        "Sergeant",
        "Master Sergeant",
        "Warrant Officer",
        "Lieutenant",
        "Major",
        "Colonel",
        "Brigadier",
        "General",
    ]
