import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsCrimesV2(BaseSchema):
    """
    JSON object of `PersonalStatsCrimesV2`.
    """

    version: str
    skills: typing.TypedDict(
        "",
        {
            "shoplifting": int,
            "search_for_cash": int,
            "scamming": int,
            "pickpocketing": int,
            "hustling": int,
            "graffiti": int,
            "forgery": int,
            "disposal": int,
            "cracking": int,
            "card_skimming": int,
            "burglary": int,
            "bootlegging": int,
            "arson": int,
        },
    )
    offenses: typing.TypedDict(
        "",
        {
            "vandalism": int,
            "total": int,
            "theft": int,
            "organized_crimes": int,
            "illicit_services": int,
            "illegal_production": int,
            "fraud": int,
            "extortion": int,
            "cybercrime": int,
            "counterfeiting": int,
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsCrimesV2(
            version=BaseSchema.parse(data.get("version"), str),
            skills=BaseSchema.parse(
                data.get("skills"),
                typing.TypedDict(
                    "",
                    {
                        "shoplifting": int,
                        "search_for_cash": int,
                        "scamming": int,
                        "pickpocketing": int,
                        "hustling": int,
                        "graffiti": int,
                        "forgery": int,
                        "disposal": int,
                        "cracking": int,
                        "card_skimming": int,
                        "burglary": int,
                        "bootlegging": int,
                        "arson": int,
                    },
                ),
            ),
            offenses=BaseSchema.parse(
                data.get("offenses"),
                typing.TypedDict(
                    "",
                    {
                        "vandalism": int,
                        "total": int,
                        "theft": int,
                        "organized_crimes": int,
                        "illicit_services": int,
                        "illegal_production": int,
                        "fraud": int,
                        "extortion": int,
                        "cybercrime": int,
                        "counterfeiting": int,
                    },
                ),
            ),
        )
