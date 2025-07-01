from ..base_schema import BaseSchema


class ReportTypeEnum(BaseSchema):

    values = [
        "mostwanted",
        "money",
        "stats",
        "references",
        "friendorfoe",
        "companyfinancials",
        "truelevel",
        "stockanalysis",
        "anonymousbounties",
        "investment",
    ]
