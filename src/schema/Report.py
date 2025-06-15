import typing

from ReportBase import ReportBase
from ReportReport import ReportReport

from ..base_schema import BaseSchema


class Report(BaseSchema):
    value: typing.List[ReportReport | ReportBase]
