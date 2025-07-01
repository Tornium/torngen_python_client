import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_education import TornEducation


@dataclass
class TornEducationResponse(BaseSchema):
    """
    JSON object of `TornEducationResponse`.
    """

    education: typing.List[TornEducation]

    @staticmethod
    def parse(data):
        return TornEducationResponse(
            education=BaseSchema.parse(
                data.get("education"), typing.List[TornEducation]
            ),
        )
