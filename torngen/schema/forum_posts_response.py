import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_post import ForumPost
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class ForumPostsResponse(BaseSchema):
    """
    JSON object of `ForumPostsResponse`.
    """

    posts: typing.List[ForumPost]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return ForumPostsResponse(
            posts=BaseSchema.parse(data.get("posts"), typing.List[ForumPost]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
