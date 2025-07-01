from ..base_schema import BaseSchema


class FactionCrimeUserOutcome(BaseSchema):

    values = [
        "Successful",
        "Failed",
        "Jailed",
        "Injured",
        "Hospitalized",
    ]
