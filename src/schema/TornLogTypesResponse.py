import typing

from TornLog import TornLog

from ..base_schema import BaseSchema


class TornLogTypesResponse(BaseSchema):

    logtypes: typing.List[TornLog]
