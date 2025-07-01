import typing

from UserPropertyDetails import UserPropertyDetails

from ..base_schema import BaseSchema


class UserPropertyResponse(BaseSchema):

    property: UserPropertyDetails
