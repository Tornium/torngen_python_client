from ..base_schema import BaseSchema


class JobPositionLawEnum(BaseSchema):

    values = [
        "Law Student",
        "Paralegal",
        "Probate Lawyer",
        "Trial Lawyer",
        "Circuit Court Judge",
        "Federal Judge",
    ]
