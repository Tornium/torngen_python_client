from ..base_schema import BaseSchema


class RaceCarUpgradeCategory(BaseSchema):

    values = [
        "Aerodynamics",
        "Brakes",
        "Engine",
        "Exhaust and Induction",
        "Fuel",
        "Safety",
        "Suspension",
        "Transmission",
        "Weight Reduction",
        "Wheels and Tyres",
    ]
