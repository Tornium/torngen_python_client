import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorCategorySelectionUnavailableForInteractionLogs(BaseSchema):
    """
    JSON object of `ErrorCategorySelectionUnavailableForInteractionLogs`.
    """

    error: str
    code: typing.Literal[29]

    @staticmethod
    def parse(data):
        return ErrorCategorySelectionUnavailableForInteractionLogs(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[29]),
        )
