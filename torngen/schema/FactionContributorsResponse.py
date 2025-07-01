import typing

from FactionContributor import FactionContributor

from ..base_schema import BaseSchema


class FactionContributorsResponse(BaseSchema):

    contributors: typing.List[FactionContributor]
