import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_faction_tree_branch import TornFactionTreeBranch


@dataclass
class TornFactionTree(BaseSchema):
    """
    JSON object of `TornFactionTree`.
    """

    name: str
    branches: typing.List[TornFactionTreeBranch]

    @staticmethod
    def parse(data):
        return TornFactionTree(
            name=BaseSchema.parse(data.get("name"), str),
            branches=BaseSchema.parse(
                data.get("branches"), typing.List[TornFactionTreeBranch]
            ),
        )
