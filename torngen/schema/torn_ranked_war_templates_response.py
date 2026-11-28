import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_ranked_war_templates import TornRankedWarTemplates


@dataclass
class TornRankedWarTemplatesResponse(BaseSchema):
    """
    JSON object of `TornRankedWarTemplatesResponse`.
    """

    rankedwartemplates: TornRankedWarTemplates

    @staticmethod
    def parse(data):
        return TornRankedWarTemplatesResponse(
            rankedwartemplates=BaseSchema.parse(
                data.get("rankedwartemplates"), TornRankedWarTemplates
            ),
        )
