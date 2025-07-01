import typing

from FactionBasic import FactionBasic

from ..base_schema import BaseSchema


class FactionBasicResponse(BaseSchema):

    basic: FactionBasic
