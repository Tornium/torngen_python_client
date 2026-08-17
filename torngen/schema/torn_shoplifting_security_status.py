import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_shoplifting_status_title_enum import TornShopliftingStatusTitleEnum


@dataclass
class TornShopliftingSecurityStatus(BaseSchema):
    """
    JSON object of `TornShopliftingSecurityStatus`.
    """

    title: TornShopliftingStatusTitleEnum
    disabled: bool

    @staticmethod
    def parse(data):
        return TornShopliftingSecurityStatus(
            title=BaseSchema.parse(data.get("title"), TornShopliftingStatusTitleEnum),
            disabled=BaseSchema.parse(data.get("disabled"), bool),
        )
