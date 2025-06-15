from ..base_schema import BaseSchema


class JobPositionMedicalEnum(BaseSchema):

    values = [
        "Medical Student",
        "Houseman",
        "Senior Houseman",
        "GP",
        "Consultant",
        "Surgeon",
        "Brain Surgeon",
    ]
