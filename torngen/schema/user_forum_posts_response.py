import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_post import ForumPost
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class UserForumPostsResponse(BaseSchema):
    """
    JSON object of `UserForumPostsResponse`.
    """

    forumPosts: typing.List[ForumPost]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserForumPostsResponse(
            forumPosts=BaseSchema.parse(data.get("forumPosts"), typing.List[ForumPost]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
