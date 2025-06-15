import typing

from UserSelectionName import UserSelectionName

from ..base_schema import BaseSchema


class UserLookupResponse(BaseSchema):

    selections: typing.List[UserSelectionName]
