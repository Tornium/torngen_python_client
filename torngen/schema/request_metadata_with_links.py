import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_links import RequestLinks


@dataclass
class RequestMetadataWithLinks(BaseSchema):
    """
    JSON object of `RequestMetadataWithLinks`.
    """

    links: RequestLinks

    @staticmethod
    def parse(data):
        return RequestMetadataWithLinks(
            links=BaseSchema.parse(data.get("links"), RequestLinks),
        )
