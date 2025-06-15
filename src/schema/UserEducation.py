import typing

from EducationId import EducationId
from UserCurrentEducation import UserCurrentEducation

from ..base_schema import BaseSchema


class UserEducation(BaseSchema):

    current: None | UserCurrentEducation
    complete: typing.List[EducationId]
