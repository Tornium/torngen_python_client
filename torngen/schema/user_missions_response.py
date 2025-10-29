import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .mission_difficulty_enum import MissionDifficultyEnum
from .mission_reward_details_ammo import MissionRewardDetailsAmmo
from .mission_reward_details_item import MissionRewardDetailsItem
from .mission_reward_details_upgrade import MissionRewardDetailsUpgrade
from .mission_reward_upgrade import MissionRewardUpgrade
from .mission_status_enum import MissionStatusEnum
from .user_id import UserId


@dataclass
class UserMissionsResponse(BaseSchema):
    """
    JSON object of `UserMissionsResponse`.
    """

    missions: typing.TypedDict(
        "",
        {
            "rewards": typing.List[
                typing.TypedDict(
                    "",
                    {
                        "type": MissionRewardUpgrade,
                        "expires_at": int,
                        "details": MissionRewardDetailsItem
                        | MissionRewardDetailsUpgrade
                        | MissionRewardDetailsAmmo,
                        "cost": int,
                        "amount": int,
                    },
                )
            ],
            "givers": typing.List[
                typing.TypedDict(
                    "",
                    {
                        "name": str,
                        "id": UserId,
                        "contracts": typing.List[
                            typing.TypedDict(
                                "",
                                {
                                    "title": str,
                                    "status": MissionStatusEnum,
                                    "started_at": None | int,
                                    "rewards": None
                                    | typing.TypedDict(
                                        "", {"money": int, "credits": int}
                                    ),
                                    "expires_at": None | int,
                                    "difficulty": MissionDifficultyEnum,
                                    "created_at": int,
                                    "completed_at": None | int,
                                },
                            )
                        ],
                    },
                )
            ],
            "credits": int,
        },
    )

    @staticmethod
    def parse(data):
        return UserMissionsResponse(
            missions=BaseSchema.parse(
                data.get("missions"),
                typing.TypedDict(
                    "",
                    {
                        "rewards": typing.List[
                            typing.TypedDict(
                                "",
                                {
                                    "type": MissionRewardUpgrade,
                                    "expires_at": int,
                                    "details": MissionRewardDetailsItem
                                    | MissionRewardDetailsUpgrade
                                    | MissionRewardDetailsAmmo,
                                    "cost": int,
                                    "amount": int,
                                },
                            )
                        ],
                        "givers": typing.List[
                            typing.TypedDict(
                                "",
                                {
                                    "name": str,
                                    "id": UserId,
                                    "contracts": typing.List[
                                        typing.TypedDict(
                                            "",
                                            {
                                                "title": str,
                                                "status": MissionStatusEnum,
                                                "started_at": None | int,
                                                "rewards": None
                                                | typing.TypedDict(
                                                    "", {"money": int, "credits": int}
                                                ),
                                                "expires_at": None | int,
                                                "difficulty": MissionDifficultyEnum,
                                                "created_at": int,
                                                "completed_at": None | int,
                                            },
                                        )
                                    ],
                                },
                            )
                        ],
                        "credits": int,
                    },
                ),
            ),
        )
