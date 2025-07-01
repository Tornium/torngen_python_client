import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsAttackingPopular(BaseSchema):
    """
    JSON object of `PersonalStatsAttackingPopular`.
    """

    attacking: typing.TypedDict(
        "",
        {
            "networth": typing.TypedDict(
                "", {"money_mugged": int, "largest_mug": int, "items_looted": int}
            ),
            "killstreak": typing.TypedDict("", {"best": int}),
            "hits": typing.TypedDict(
                "", {"success": int, "one_hit_kills": int, "miss": int, "critical": int}
            ),
            "faction": typing.TypedDict("", {"respect": int, "ranked_war_hits": int}),
            "escapes": typing.TypedDict("", {"player": int, "foes": int}),
            "elo": int,
            "defends": typing.TypedDict(
                "", {"won": int, "stalemate": int, "lost": int}
            ),
            "damage": typing.TypedDict("", {"total": int, "best": int}),
            "attacks": typing.TypedDict(
                "", {"won": int, "stalemate": int, "lost": int, "assist": int}
            ),
            "ammunition": typing.TypedDict(
                "",
                {
                    "tracer": int,
                    "total": int,
                    "special": int,
                    "piercing": int,
                    "incendiary": int,
                    "hollow_point": int,
                },
            ),
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsAttackingPopular(
            attacking=BaseSchema.parse(
                data.get("attacking"),
                typing.TypedDict(
                    "",
                    {
                        "networth": typing.TypedDict(
                            "",
                            {
                                "money_mugged": int,
                                "largest_mug": int,
                                "items_looted": int,
                            },
                        ),
                        "killstreak": typing.TypedDict("", {"best": int}),
                        "hits": typing.TypedDict(
                            "",
                            {
                                "success": int,
                                "one_hit_kills": int,
                                "miss": int,
                                "critical": int,
                            },
                        ),
                        "faction": typing.TypedDict(
                            "", {"respect": int, "ranked_war_hits": int}
                        ),
                        "escapes": typing.TypedDict("", {"player": int, "foes": int}),
                        "elo": int,
                        "defends": typing.TypedDict(
                            "", {"won": int, "stalemate": int, "lost": int}
                        ),
                        "damage": typing.TypedDict("", {"total": int, "best": int}),
                        "attacks": typing.TypedDict(
                            "",
                            {"won": int, "stalemate": int, "lost": int, "assist": int},
                        ),
                        "ammunition": typing.TypedDict(
                            "",
                            {
                                "tracer": int,
                                "total": int,
                                "special": int,
                                "piercing": int,
                                "incendiary": int,
                                "hollow_point": int,
                            },
                        ),
                    },
                ),
            ),
        )
