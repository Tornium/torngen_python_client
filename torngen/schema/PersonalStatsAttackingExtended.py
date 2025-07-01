import typing

from ..base_schema import BaseSchema


class PersonalStatsAttackingExtended(BaseSchema):

    attacking: typing.TypedDict(
        "",
        {
            "unarmored_wins": int,
            "networth": typing.TypedDict(
                "", {"money_mugged": int, "largest_mug": int, "items_looted": int}
            ),
            "killstreak": typing.TypedDict("", {"current": int, "best": int}),
            "hits": typing.TypedDict(
                "", {"success": int, "one_hit_kills": int, "miss": int, "critical": int}
            ),
            "highest_level_beaten": int,
            "faction": typing.TypedDict(
                "",
                {
                    "territory": typing.TypedDict(
                        "", {"wall_time": int, "wall_joins": int, "wall_clears": int}
                    ),
                    "retaliations": int,
                    "respect": int,
                    "ranked_war_hits": int,
                    "raid_hits": int,
                },
            ),
            "escapes": typing.TypedDict("", {"player": int, "foes": int}),
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
    )
