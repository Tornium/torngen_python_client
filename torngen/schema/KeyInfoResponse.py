import typing

from ApiKeyAccessTypeEnum import ApiKeyAccessTypeEnum
from CompanyId import CompanyId
from FactionId import FactionId
from FactionSelectionName import FactionSelectionName
from ForumSelectionName import ForumSelectionName
from KeySelectionName import KeySelectionName
from MarketSelectionName import MarketSelectionName
from RacingSelectionName import RacingSelectionName
from TornSelectionName import TornSelectionName
from UserSelectionName import UserSelectionName

from ..base_schema import BaseSchema


class KeyInfoResponse(BaseSchema):

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
