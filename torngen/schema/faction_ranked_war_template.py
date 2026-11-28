import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_ranked_war_mode import FactionRankedWarMode
from .faction_ranked_war_rule import FactionRankedWarRule


@dataclass
class FactionRankedWarTemplate(BaseSchema):
    """
    JSON object of `FactionRankedWarTemplate`.
    """

    rules: typing.List[FactionRankedWarRule]
    mode: None | FactionRankedWarMode

    @staticmethod
    def parse(data):
        return FactionRankedWarTemplate(
            rules=BaseSchema.parse(
                data.get("rules"), typing.List[FactionRankedWarRule]
            ),
            mode=BaseSchema.parse(data.get("mode"), None | FactionRankedWarMode),
        )
