import typing

from ..base_schema import BaseSchema
from .report_base import ReportBase
from .report_report import ReportReport


class Report(BaseSchema):
    value: typing.List[ReportReport | ReportBase]
