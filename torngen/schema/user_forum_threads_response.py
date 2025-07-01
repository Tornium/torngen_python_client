import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_thread_user_extended import ForumThreadUserExtended
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class UserForumThreadsResponse(BaseSchema):
    """
    JSON object of `UserForumThreadsResponse`.
    """

    forumThreads: typing.List[ForumThreadUserExtended]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserForumThreadsResponse(
            forumThreads=BaseSchema.parse(
                data.get("forumThreads"), typing.List[ForumThreadUserExtended]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
