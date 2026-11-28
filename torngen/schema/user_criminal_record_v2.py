import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCriminalRecordV2(BaseSchema):
    """
    JSON object of `UserCriminalRecordV2`.
    """

    version: typing.Literal["v2"]
    vandalism: int
    total: int
    theft: int
    illicit_services: int
    illegal_production: int
    fraud: int
    extortion: int
    cybercrime: int
    counterfeiting: int

    @staticmethod
    def parse(data):
        return UserCriminalRecordV2(
            version=BaseSchema.parse(data.get("version"), typing.Literal["v2"]),
            vandalism=BaseSchema.parse(data.get("vandalism"), int),
            total=BaseSchema.parse(data.get("total"), int),
            theft=BaseSchema.parse(data.get("theft"), int),
            illicit_services=BaseSchema.parse(data.get("illicit_services"), int),
            illegal_production=BaseSchema.parse(data.get("illegal_production"), int),
            fraud=BaseSchema.parse(data.get("fraud"), int),
            extortion=BaseSchema.parse(data.get("extortion"), int),
            cybercrime=BaseSchema.parse(data.get("cybercrime"), int),
            counterfeiting=BaseSchema.parse(data.get("counterfeiting"), int),
        )
