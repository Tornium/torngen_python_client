import typing

from ForumPost import ForumPost
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class UserForumPostsResponse(BaseSchema):

    forumPosts: typing.List[ForumPost]
    _metadata: RequestMetadataWithLinks
