import typing

from EducationId import EducationId

from ..base_schema import BaseSchema


class UserCurrentEducation(BaseSchema):

    until: int
    id: EducationId
