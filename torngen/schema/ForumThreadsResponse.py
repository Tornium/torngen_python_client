import typing

from ForumThreadBase import ForumThreadBase
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class ForumThreadsResponse(BaseSchema):

    threads: typing.List[ForumThreadBase]
    _metadata: RequestMetadataWithLinks
