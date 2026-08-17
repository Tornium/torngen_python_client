import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_links import RequestLinks


@dataclass
class RequestMetadataWithLinksAndNanostamp(BaseSchema):
    """
    JSON object of `RequestMetadataWithLinksAndNanostamp`.
    """

    nanostamp: typing.Optional[str]
    links: RequestLinks

    @staticmethod
    def parse(data):
        return RequestMetadataWithLinksAndNanostamp(
            nanostamp=BaseSchema.parse(data.get("nanostamp"), typing.Optional[str]),
            links=BaseSchema.parse(data.get("links"), RequestLinks),
        )
