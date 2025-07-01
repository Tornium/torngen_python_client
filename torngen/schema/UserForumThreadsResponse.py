import typing

from ForumThreadUserExtended import ForumThreadUserExtended
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class UserForumThreadsResponse(BaseSchema):

    forumThreads: typing.List[ForumThreadUserExtended]
    _metadata: RequestMetadataWithLinks
