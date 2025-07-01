import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_thread_base import ForumThreadBase
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class ForumThreadsResponse(BaseSchema):
    """
    JSON object of `ForumThreadsResponse`.
    """

    threads: typing.List[ForumThreadBase]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return ForumThreadsResponse(
            threads=BaseSchema.parse(data.get("threads"), typing.List[ForumThreadBase]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
