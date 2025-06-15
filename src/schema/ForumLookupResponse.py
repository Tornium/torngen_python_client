import typing

from ForumSelectionName import ForumSelectionName

from ..base_schema import BaseSchema


class ForumLookupResponse(BaseSchema):

    selections: typing.List[ForumSelectionName]
