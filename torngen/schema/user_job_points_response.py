import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_company_points import UserCompanyPoints


@dataclass
class UserJobPointsResponse(BaseSchema):
    """
    JSON object of `UserJobPointsResponse`.
    """

    jobpoints: typing.TypedDict(
        "",
        {
            "jobs": typing.TypedDict(
                "",
                {
                    "medical": int,
                    "law": int,
                    "grocer": int,
                    "education": int,
                    "casino": int,
                    "army": int,
                },
            ),
            "companies": typing.List[UserCompanyPoints],
        },
    )

    @staticmethod
    def parse(data):
        return UserJobPointsResponse(
            jobpoints=BaseSchema.parse(
                data.get("jobpoints"),
                typing.TypedDict(
                    "",
                    {
                        "jobs": typing.TypedDict(
                            "",
                            {
                                "medical": int,
                                "law": int,
                                "grocer": int,
                                "education": int,
                                "casino": int,
                                "army": int,
                            },
                        ),
                        "companies": typing.List[UserCompanyPoints],
                    },
                ),
            ),
        )
