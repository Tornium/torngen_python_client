import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserPersonalStatsPopular(BaseSchema):
    """
    JSON object of `UserPersonalStatsPopular`.
    """

    personalstats: typing.TypedDict(
        "",
        {
            "other": typing.TypedDict(
                "",
                {
                    "refills": typing.TypedDict("", {"nerve": int, "energy": int}),
                    "ranked_war_wins": int,
                    "merits_bought": int,
                    "donator_days": int,
                    "awards": int,
                    "activity": typing.TypedDict(
                        "",
                        {
                            "time": int,
                            "streak": typing.TypedDict(
                                "", {"current": int, "best": int}
                            ),
                        },
                    ),
                },
            ),
            "networth": typing.TypedDict("", {"total": int}),
            "drugs": typing.TypedDict(
                "",
                {
                    "xanax": int,
                    "vicodin": int,
                    "total": int,
                    "speed": int,
                    "shrooms": int,
                    "rehabilitations": typing.TypedDict(
                        "", {"fees": int, "amount": int}
                    ),
                    "pcp": int,
                    "overdoses": int,
                    "opium": int,
                    "lsd": int,
                    "ketamine": int,
                    "ecstasy": int,
                    "cannabis": int,
                },
            ),
            "travel": typing.TypedDict("", {"total": int, "time_spent": int}),
            "items": typing.TypedDict(
                "",
                {
                    "used": typing.TypedDict(
                        "",
                        {
                            "stat_enhancers": int,
                            "energy_drinks": int,
                            "easter_eggs": int,
                            "consumables": int,
                            "candy": int,
                            "boosters": int,
                            "books": int,
                            "alcohol": int,
                        },
                    ),
                    "found": typing.TypedDict("", {"dump": int}),
                },
            ),
            "crimes": typing.TypedDict("", {"version": str, "total": int}),
            "hospital": typing.TypedDict(
                "",
                {
                    "reviving": typing.TypedDict("", {"skill": int, "revives": int}),
                    "medical_items_used": int,
                },
            ),
            "jobs": typing.TypedDict(
                "", {"trains_received": int, "job_points_used": int}
            ),
            "attacking": typing.TypedDict(
                "",
                {
                    "networth": typing.TypedDict(
                        "",
                        {"money_mugged": int, "largest_mug": int, "items_looted": int},
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
            ),
        },
    )

    @staticmethod
    def parse(data):
        return UserPersonalStatsPopular(
            personalstats=BaseSchema.parse(
                data.get("personalstats"),
                typing.TypedDict(
                    "",
                    {
                        "other": typing.TypedDict(
                            "",
                            {
                                "refills": typing.TypedDict(
                                    "", {"nerve": int, "energy": int}
                                ),
                                "ranked_war_wins": int,
                                "merits_bought": int,
                                "donator_days": int,
                                "awards": int,
                                "activity": typing.TypedDict(
                                    "",
                                    {
                                        "time": int,
                                        "streak": typing.TypedDict(
                                            "", {"current": int, "best": int}
                                        ),
                                    },
                                ),
                            },
                        ),
                        "networth": typing.TypedDict("", {"total": int}),
                        "drugs": typing.TypedDict(
                            "",
                            {
                                "xanax": int,
                                "vicodin": int,
                                "total": int,
                                "speed": int,
                                "shrooms": int,
                                "rehabilitations": typing.TypedDict(
                                    "", {"fees": int, "amount": int}
                                ),
                                "pcp": int,
                                "overdoses": int,
                                "opium": int,
                                "lsd": int,
                                "ketamine": int,
                                "ecstasy": int,
                                "cannabis": int,
                            },
                        ),
                        "travel": typing.TypedDict(
                            "", {"total": int, "time_spent": int}
                        ),
                        "items": typing.TypedDict(
                            "",
                            {
                                "used": typing.TypedDict(
                                    "",
                                    {
                                        "stat_enhancers": int,
                                        "energy_drinks": int,
                                        "easter_eggs": int,
                                        "consumables": int,
                                        "candy": int,
                                        "boosters": int,
                                        "books": int,
                                        "alcohol": int,
                                    },
                                ),
                                "found": typing.TypedDict("", {"dump": int}),
                            },
                        ),
                        "crimes": typing.TypedDict("", {"version": str, "total": int}),
                        "hospital": typing.TypedDict(
                            "",
                            {
                                "reviving": typing.TypedDict(
                                    "", {"skill": int, "revives": int}
                                ),
                                "medical_items_used": int,
                            },
                        ),
                        "jobs": typing.TypedDict(
                            "", {"trains_received": int, "job_points_used": int}
                        ),
                        "attacking": typing.TypedDict(
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
                                "escapes": typing.TypedDict(
                                    "", {"player": int, "foes": int}
                                ),
                                "elo": int,
                                "defends": typing.TypedDict(
                                    "", {"won": int, "stalemate": int, "lost": int}
                                ),
                                "damage": typing.TypedDict(
                                    "", {"total": int, "best": int}
                                ),
                                "attacks": typing.TypedDict(
                                    "",
                                    {
                                        "won": int,
                                        "stalemate": int,
                                        "lost": int,
                                        "assist": int,
                                    },
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
                    },
                ),
            ),
        )
