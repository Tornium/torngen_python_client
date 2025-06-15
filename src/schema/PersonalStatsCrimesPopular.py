import typing

from ..base_schema import BaseSchema


class PersonalStatsCrimesPopular(BaseSchema):

    crimes: typing.TypedDict("", {"version": str, "total": int})
