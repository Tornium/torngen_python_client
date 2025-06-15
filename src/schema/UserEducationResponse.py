import typing

from UserEducation import UserEducation

from ..base_schema import BaseSchema


class UserEducationResponse(BaseSchema):

    education: UserEducation
