import typing

from ReportWarrantDetails import ReportWarrantDetails

from ..base_schema import BaseSchema


class ReportMostWanted(BaseSchema):

    top: typing.List[ReportWarrantDetails]
    notable: typing.List[ReportWarrantDetails]
