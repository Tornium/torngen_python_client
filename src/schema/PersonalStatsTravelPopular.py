import typing

from ..base_schema import BaseSchema


class PersonalStatsTravelPopular(BaseSchema):

    travel: typing.TypedDict("", {"total": int, "time_spent": int})
