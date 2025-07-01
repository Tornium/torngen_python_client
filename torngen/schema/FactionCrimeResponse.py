import typing

from FactionCrime import FactionCrime

from ..base_schema import BaseSchema


class FactionCrimeResponse(BaseSchema):

    crime: FactionCrime
