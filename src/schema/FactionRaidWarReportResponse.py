import typing

from FactionRaidReport import FactionRaidReport

from ..base_schema import BaseSchema


class FactionRaidWarReportResponse(BaseSchema):

    raidreport: typing.List[FactionRaidReport]
