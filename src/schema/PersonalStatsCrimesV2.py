import typing

from ..base_schema import BaseSchema


class PersonalStatsCrimesV2(BaseSchema):

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
