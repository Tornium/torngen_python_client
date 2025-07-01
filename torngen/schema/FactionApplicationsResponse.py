import typing

from FactionApplication import FactionApplication

from ..base_schema import BaseSchema


class FactionApplicationsResponse(BaseSchema):

    applications: typing.List[FactionApplication]
