import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_links import RequestLinks


@dataclass
class RequestMetadata(BaseSchema):
    """
    JSON object of `RequestMetadata`.
    """

    links: RequestLinks

    @staticmethod
    def parse(data):
        return RequestMetadata(
            links=BaseSchema.parse(data.get("links"), RequestLinks),
        )
