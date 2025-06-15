import typing

from UserRaceCarDetails import UserRaceCarDetails

from ..base_schema import BaseSchema


class UserEnlistedCarsResponse(BaseSchema):

    enlistedcars: typing.List[UserRaceCarDetails]
