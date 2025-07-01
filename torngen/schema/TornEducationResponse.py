import typing

from TornEducation import TornEducation

from ..base_schema import BaseSchema


class TornEducationResponse(BaseSchema):

    education: typing.List[TornEducation]
