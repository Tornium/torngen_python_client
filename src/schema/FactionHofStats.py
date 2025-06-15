import typing

from HofValue import HofValue
from HofValueString import HofValueString

from ..base_schema import BaseSchema


class FactionHofStats(BaseSchema):

    respect: HofValue
    rank: HofValueString
    chain: HofValue
