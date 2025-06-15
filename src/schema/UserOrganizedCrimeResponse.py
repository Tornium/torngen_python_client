import typing

from FactionCrime import FactionCrime

from ..base_schema import BaseSchema


class UserOrganizedCrimeResponse(BaseSchema):

    organizedCrime: None | FactionCrime
