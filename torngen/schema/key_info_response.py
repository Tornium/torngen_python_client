import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .api_key_access_type_enum import ApiKeyAccessTypeEnum
from .company_id import CompanyId
from .faction_id import FactionId
from .faction_selection_name import FactionSelectionName
from .forum_selection_name import ForumSelectionName
from .key_selection_name import KeySelectionName
from .market_selection_name import MarketSelectionName
from .racing_selection_name import RacingSelectionName
from .torn_selection_name import TornSelectionName
from .user_selection_name import UserSelectionName


@dataclass
class KeyInfoResponse(BaseSchema):
    """
    JSON object of `KeyInfoResponse`.
    """

    info: typing.TypedDict(
        "",
        {
            "selections": typing.TypedDict(
                "",
                {
                    "user": typing.List[UserSelectionName],
                    "torn": typing.List[TornSelectionName],
                    "racing": typing.List[RacingSelectionName],
                    "property": typing.List[str],
                    "market": typing.List[MarketSelectionName],
                    "key": typing.List[KeySelectionName],
                    "forum": typing.List[ForumSelectionName],
                    "faction": typing.List[FactionSelectionName],
                    "company": typing.List[str],
                },
            ),
            "access": typing.TypedDict(
                "",
                {
                    "type": ApiKeyAccessTypeEnum,
                    "level": int,
                    "faction_id": None | FactionId,
                    "faction": bool,
                    "company_id": None | CompanyId,
                    "company": bool,
                },
            ),
        },
    )

    @staticmethod
    def parse(data):
        return KeyInfoResponse(
            info=BaseSchema.parse(
                data.get("info"),
                typing.TypedDict(
                    "",
                    {
                        "selections": typing.TypedDict(
                            "",
                            {
                                "user": typing.List[UserSelectionName],
                                "torn": typing.List[TornSelectionName],
                                "racing": typing.List[RacingSelectionName],
                                "property": typing.List[str],
                                "market": typing.List[MarketSelectionName],
                                "key": typing.List[KeySelectionName],
                                "forum": typing.List[ForumSelectionName],
                                "faction": typing.List[FactionSelectionName],
                                "company": typing.List[str],
                            },
                        ),
                        "access": typing.TypedDict(
                            "",
                            {
                                "type": ApiKeyAccessTypeEnum,
                                "level": int,
                                "faction_id": None | FactionId,
                                "faction": bool,
                                "company_id": None | CompanyId,
                                "company": bool,
                            },
                        ),
                    },
                ),
            ),
        )
