import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .report_warrant_details import ReportWarrantDetails


@dataclass
class ReportMostWanted(BaseSchema):
    """
    JSON object of `ReportMostWanted`.
    """

    top: typing.List[ReportWarrantDetails]
    notable: typing.List[ReportWarrantDetails]

    @staticmethod
    def parse(data):
        return ReportMostWanted(
            top=BaseSchema.parse(data.get("top"), typing.List[ReportWarrantDetails]),
            notable=BaseSchema.parse(
                data.get("notable"), typing.List[ReportWarrantDetails]
            ),
        )
