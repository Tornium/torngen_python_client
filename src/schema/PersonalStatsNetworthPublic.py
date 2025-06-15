import typing

from ..base_schema import BaseSchema


class PersonalStatsNetworthPublic(BaseSchema):

    networth: typing.TypedDict("", {"total": int})
