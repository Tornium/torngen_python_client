from ..base_schema import BaseSchema


class FactionTerritoryWarResultEnum(BaseSchema):

    values = [
        "success_assault",
        "fail_assault",
        "end_with_nap",
        "end_with_destroy_attack",
        "end_with_destroy_defense",
        "end_with_peace_treaty",
    ]
