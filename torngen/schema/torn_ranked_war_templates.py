import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_ranked_war_template_entry import TornRankedWarTemplateEntry


@dataclass
class TornRankedWarTemplates(BaseSchema):
    """
    JSON object of `TornRankedWarTemplates`.
    """

    rules: typing.List[TornRankedWarTemplateEntry]
    modes: typing.List[TornRankedWarTemplateEntry]

    @staticmethod
    def parse(data):
        return TornRankedWarTemplates(
            rules=BaseSchema.parse(
                data.get("rules"), typing.List[TornRankedWarTemplateEntry]
            ),
            modes=BaseSchema.parse(
                data.get("modes"), typing.List[TornRankedWarTemplateEntry]
            ),
        )
