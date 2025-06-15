import typing

from TornFactionTreeBranch import TornFactionTreeBranch

from ..base_schema import BaseSchema


class TornFactionTree(BaseSchema):

    name: str
    branches: typing.List[TornFactionTreeBranch]
