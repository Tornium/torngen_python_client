import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_links import RequestLinks


@dataclass
class RequestMetadataWithLinksAndTotal(BaseSchema):
    """
    JSON object of `RequestMetadataWithLinksAndTotal`.
    """

    total: typing.Optional[int]
    links: RequestLinks

    @staticmethod
    def parse(data):
        return RequestMetadataWithLinksAndTotal(
            total=BaseSchema.parse(data.get("total"), typing.Optional[int]),
            links=BaseSchema.parse(data.get("links"), RequestLinks),
        )
