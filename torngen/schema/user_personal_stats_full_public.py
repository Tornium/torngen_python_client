import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .personal_stats_crimes_v1 import PersonalStatsCrimesV1
from .personal_stats_crimes_v2 import PersonalStatsCrimesV2


@dataclass
class UserPersonalStatsFullPublic(BaseSchema):
    """
    JSON object of `UserPersonalStatsFullPublic`.
    """

    personalstats: typing.TypedDict(
        "",
        {
            "other": typing.TypedDict(
                "",
                {
                    "refills": typing.TypedDict(
                        "", {"token": int, "nerve": int, "energy": int}
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
            "racing": typing.TypedDict(
                "",
                {
                    "skill": int,
                    "races": typing.TypedDict("", {"won": int, "entered": int}),
                    "points": int,
                },
            ),
            "missions": typing.TypedDict(
                "",
                {
                    "missions": int,
                    "credits": int,
                    "contracts": typing.TypedDict("", {"total": int, "duke": int}),
                },
            ),
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
                "",
                {
                    "united_kingdom": int,
                    "united_arab_emirates": int,
                    "total": int,
                    "time_spent": int,
                    "switzerland": int,
                    "south_africa": int,
                    "mexico": int,
                    "japan": int,
                    "items_bought": int,
                    "hunting": typing.TypedDict("", {"skill": int}),
                    "hawaii": int,
                    "defends_lost": int,
                    "china": int,
                    "cayman_islands": int,
                    "canada": int,
                    "attacks_won": int,
                    "argentina": int,
                },
            ),
            "items": typing.TypedDict(
                "",
                {
                    "viruses_coded": int,
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
                    "trashed": int,
                    "found": typing.TypedDict(
                        "", {"easter_eggs": int, "dump": int, "city": int}
                    ),
                },
            ),
            "bounties": typing.TypedDict(
                "",
                {
                    "received": typing.TypedDict("", {"value": int, "amount": int}),
                    "placed": typing.TypedDict("", {"value": int, "amount": int}),
                    "collected": typing.TypedDict("", {"value": int, "amount": int}),
                },
            ),
            "crimes": PersonalStatsCrimesV2 | PersonalStatsCrimesV1,
            "communication": typing.TypedDict(
                "",
                {
                    "personals": int,
                    "mails_sent": typing.TypedDict(
                        "",
                        {
                            "total": int,
                            "spouse": int,
                            "friends": int,
                            "faction": int,
                            "colleagues": int,
                        },
                    ),
                    "classified_ads": int,
                },
            ),
            "finishing_hits": typing.TypedDict(
                "",
                {
                    "temporary": int,
                    "sub_machine_guns": int,
                    "slashing": int,
                    "shotguns": int,
                    "rifles": int,
                    "pistols": int,
                    "piercing": int,
                    "mechanical": int,
                    "machine_guns": int,
                    "heavy_artillery": int,
                    "hand_to_hand": int,
                    "clubbing": int,
                },
            ),
            "hospital": typing.TypedDict(
                "",
                {
                    "times_hospitalized": int,
                    "reviving": typing.TypedDict(
                        "", {"skill": int, "revives_received": int, "revives": int}
                    ),
                    "medical_items_used": int,
                    "blood_withdrawn": int,
                },
            ),
            "jail": typing.TypedDict(
                "",
                {
                    "times_jailed": int,
                    "busts": typing.TypedDict("", {"success": int, "fails": int}),
                    "bails": typing.TypedDict("", {"fees": int, "amount": int}),
                },
            ),
            "trading": typing.TypedDict(
                "",
                {
                    "trades": int,
                    "points": typing.TypedDict("", {"sold": int, "bought": int}),
                    "items": typing.TypedDict(
                        "",
                        {
                            "sent": int,
                            "bought": typing.TypedDict(
                                "", {"shops": int, "market": int}
                            ),
                            "auctions": typing.TypedDict("", {"won": int, "sold": int}),
                        },
                    ),
                    "item_market": typing.Optional[
                        typing.TypedDict(
                            "",
                            {
                                "sales": int,
                                "revenue": int,
                                "fees": int,
                                "customers": int,
                            },
                        )
                    ],
                    "bazaar": typing.TypedDict(
                        "", {"sales": int, "profit": int, "customers": int}
                    ),
                },
            ),
            "jobs": typing.TypedDict(
                "", {"trains_received": int, "job_points_used": int}
            ),
            "attacking": typing.TypedDict(
                "",
                {
                    "unarmored_wins": int,
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
                    "highest_level_beaten": int,
                    "faction": typing.TypedDict(
                        "",
                        {
                            "territory": typing.TypedDict(
                                "",
                                {
                                    "wall_time": int,
                                    "wall_joins": int,
                                    "wall_clears": int,
                                },
                            ),
                            "retaliations": int,
                            "respect": int,
                            "ranked_war_hits": int,
                            "raid_hits": int,
                        },
                    ),
                    "escapes": typing.Optional[
                        typing.TypedDict("", {"player": int, "foes": int})
                    ],
                    "elo": int,
                    "defends": typing.TypedDict(
                        "", {"won": int, "total": int, "stalemate": int, "lost": int}
                    ),
                    "damage": typing.TypedDict("", {"total": int, "best": int}),
                    "attacks": typing.TypedDict(
                        "",
                        {
                            "won": int,
                            "stealth": int,
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
    )

    @staticmethod
    def parse(data):
        return UserPersonalStatsFullPublic(
            personalstats=BaseSchema.parse(
                data.get("personalstats"),
                typing.TypedDict(
                    "",
                    {
                        "other": typing.TypedDict(
                            "",
                            {
                                "refills": typing.TypedDict(
                                    "", {"token": int, "nerve": int, "energy": int}
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
                        "racing": typing.TypedDict(
                            "",
                            {
                                "skill": int,
                                "races": typing.TypedDict(
                                    "", {"won": int, "entered": int}
                                ),
                                "points": int,
                            },
                        ),
                        "missions": typing.TypedDict(
                            "",
                            {
                                "missions": int,
                                "credits": int,
                                "contracts": typing.TypedDict(
                                    "", {"total": int, "duke": int}
                                ),
                            },
                        ),
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
                            "",
                            {
                                "united_kingdom": int,
                                "united_arab_emirates": int,
                                "total": int,
                                "time_spent": int,
                                "switzerland": int,
                                "south_africa": int,
                                "mexico": int,
                                "japan": int,
                                "items_bought": int,
                                "hunting": typing.TypedDict("", {"skill": int}),
                                "hawaii": int,
                                "defends_lost": int,
                                "china": int,
                                "cayman_islands": int,
                                "canada": int,
                                "attacks_won": int,
                                "argentina": int,
                            },
                        ),
                        "items": typing.TypedDict(
                            "",
                            {
                                "viruses_coded": int,
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
                                "trashed": int,
                                "found": typing.TypedDict(
                                    "", {"easter_eggs": int, "dump": int, "city": int}
                                ),
                            },
                        ),
                        "bounties": typing.TypedDict(
                            "",
                            {
                                "received": typing.TypedDict(
                                    "", {"value": int, "amount": int}
                                ),
                                "placed": typing.TypedDict(
                                    "", {"value": int, "amount": int}
                                ),
                                "collected": typing.TypedDict(
                                    "", {"value": int, "amount": int}
                                ),
                            },
                        ),
                        "crimes": PersonalStatsCrimesV2 | PersonalStatsCrimesV1,
                        "communication": typing.TypedDict(
                            "",
                            {
                                "personals": int,
                                "mails_sent": typing.TypedDict(
                                    "",
                                    {
                                        "total": int,
                                        "spouse": int,
                                        "friends": int,
                                        "faction": int,
                                        "colleagues": int,
                                    },
                                ),
                                "classified_ads": int,
                            },
                        ),
                        "finishing_hits": typing.TypedDict(
                            "",
                            {
                                "temporary": int,
                                "sub_machine_guns": int,
                                "slashing": int,
                                "shotguns": int,
                                "rifles": int,
                                "pistols": int,
                                "piercing": int,
                                "mechanical": int,
                                "machine_guns": int,
                                "heavy_artillery": int,
                                "hand_to_hand": int,
                                "clubbing": int,
                            },
                        ),
                        "hospital": typing.TypedDict(
                            "",
                            {
                                "times_hospitalized": int,
                                "reviving": typing.TypedDict(
                                    "",
                                    {
                                        "skill": int,
                                        "revives_received": int,
                                        "revives": int,
                                    },
                                ),
                                "medical_items_used": int,
                                "blood_withdrawn": int,
                            },
                        ),
                        "jail": typing.TypedDict(
                            "",
                            {
                                "times_jailed": int,
                                "busts": typing.TypedDict(
                                    "", {"success": int, "fails": int}
                                ),
                                "bails": typing.TypedDict(
                                    "", {"fees": int, "amount": int}
                                ),
                            },
                        ),
                        "trading": typing.TypedDict(
                            "",
                            {
                                "trades": int,
                                "points": typing.TypedDict(
                                    "", {"sold": int, "bought": int}
                                ),
                                "items": typing.TypedDict(
                                    "",
                                    {
                                        "sent": int,
                                        "bought": typing.TypedDict(
                                            "", {"shops": int, "market": int}
                                        ),
                                        "auctions": typing.TypedDict(
                                            "", {"won": int, "sold": int}
                                        ),
                                    },
                                ),
                                "item_market": typing.Optional[
                                    typing.TypedDict(
                                        "",
                                        {
                                            "sales": int,
                                            "revenue": int,
                                            "fees": int,
                                            "customers": int,
                                        },
                                    )
                                ],
                                "bazaar": typing.TypedDict(
                                    "", {"sales": int, "profit": int, "customers": int}
                                ),
                            },
                        ),
                        "jobs": typing.TypedDict(
                            "", {"trains_received": int, "job_points_used": int}
                        ),
                        "attacking": typing.TypedDict(
                            "",
                            {
                                "unarmored_wins": int,
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
                                "highest_level_beaten": int,
                                "faction": typing.TypedDict(
                                    "",
                                    {
                                        "territory": typing.TypedDict(
                                            "",
                                            {
                                                "wall_time": int,
                                                "wall_joins": int,
                                                "wall_clears": int,
                                            },
                                        ),
                                        "retaliations": int,
                                        "respect": int,
                                        "ranked_war_hits": int,
                                        "raid_hits": int,
                                    },
                                ),
                                "escapes": typing.Optional[
                                    typing.TypedDict("", {"player": int, "foes": int})
                                ],
                                "elo": int,
                                "defends": typing.TypedDict(
                                    "",
                                    {
                                        "won": int,
                                        "total": int,
                                        "stalemate": int,
                                        "lost": int,
                                    },
                                ),
                                "damage": typing.TypedDict(
                                    "", {"total": int, "best": int}
                                ),
                                "attacks": typing.TypedDict(
                                    "",
                                    {
                                        "won": int,
                                        "stealth": int,
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
