import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornCityStatsResponse(BaseSchema):
    """
    JSON object of `TornCityStatsResponse`.
    """

    stats: typing.TypedDict(
        "",
        {
            "users": typing.TypedDict(
                "",
                {"total": int, "married": int, "male": int, "female": int, "enby": int},
            ),
            "traveling": typing.TypedDict(
                "",
                {
                    "united_kingdom": int,
                    "united_arab_emirates": int,
                    "total_trips": int,
                    "switzerland": int,
                    "south_africa": int,
                    "mexico": int,
                    "japan": int,
                    "items_bought_abroad": int,
                    "hawaii": int,
                    "china": int,
                    "cayman_islands": int,
                    "argentina": int,
                },
            ),
            "trading": typing.TypedDict(
                "",
                {
                    "trades": int,
                    "sold_points": int,
                    "sold_on_market": int,
                    "sold_in_bazaar": int,
                    "items_sent": int,
                    "bazaar_profit": int,
                    "auctions": int,
                },
            ),
            "other": typing.TypedDict(
                "",
                {
                    "years_played": int,
                    "stat_enhancers_used": int,
                    "merits_bought": int,
                    "logins": int,
                    "energy_refills": int,
                    "company_trains": int,
                },
            ),
            "jobs": typing.TypedDict(
                "",
                {
                    "unemployed": int,
                    "medical": int,
                    "law": int,
                    "grocer": int,
                    "education": int,
                    "company": int,
                    "casino": int,
                    "army": int,
                },
            ),
            "jail": typing.TypedDict(
                "",
                {
                    "jailings": int,
                    "busts_failed": int,
                    "busts": int,
                    "bails_spent": int,
                    "bails": int,
                },
            ),
            "items": typing.TypedDict(
                "",
                {
                    "trashed": int,
                    "total": int,
                    "found_in_dump": int,
                    "found_in_city": int,
                },
            ),
            "hospital": typing.TypedDict(
                "", {"trips": int, "revives": int, "medical_items_used": int}
            ),
            "drugs": typing.TypedDict(
                "",
                {
                    "xanax": int,
                    "vicodin": int,
                    "total_used": int,
                    "speed": int,
                    "shrooms": int,
                    "pcp": int,
                    "overdoses": int,
                    "opium": int,
                    "lsd": int,
                    "ketamine": int,
                    "ecstasy": int,
                    "cannabis": int,
                },
            ),
            "currency": typing.TypedDict(
                "",
                {
                    "points_used": int,
                    "points_total": int,
                    "points_players": int,
                    "points_market": int,
                    "points_factions": int,
                    "money_on_hand_average": int,
                    "money_on_hand": int,
                    "money_in_bank": int,
                },
            ),
            "crimes": typing.TypedDict("", {"total": int, "jail_sentences": int}),
            "communication": typing.TypedDict(
                "",
                {
                    "total_messages": int,
                    "spouses": int,
                    "personals_placed": int,
                    "friends": int,
                    "coworkers": int,
                    "classified_ads_placed": int,
                },
            ),
            "bounties": typing.TypedDict("", {"placed": int, "money_spent": int}),
            "attacking": typing.TypedDict(
                "",
                {
                    "rounds_fired": int,
                    "respect_gained": int,
                    "money_mugged": int,
                    "misses": int,
                    "hits": int,
                    "escapes": int,
                    "critical_hits": int,
                    "attacks_won": int,
                    "attacks_stealthed": int,
                    "attacks_stalemated": int,
                    "attacks_lost": int,
                },
            ),
        },
    )

    @staticmethod
    def parse(data):
        return TornCityStatsResponse(
            stats=BaseSchema.parse(
                data.get("stats"),
                typing.TypedDict(
                    "",
                    {
                        "users": typing.TypedDict(
                            "",
                            {
                                "total": int,
                                "married": int,
                                "male": int,
                                "female": int,
                                "enby": int,
                            },
                        ),
                        "traveling": typing.TypedDict(
                            "",
                            {
                                "united_kingdom": int,
                                "united_arab_emirates": int,
                                "total_trips": int,
                                "switzerland": int,
                                "south_africa": int,
                                "mexico": int,
                                "japan": int,
                                "items_bought_abroad": int,
                                "hawaii": int,
                                "china": int,
                                "cayman_islands": int,
                                "argentina": int,
                            },
                        ),
                        "trading": typing.TypedDict(
                            "",
                            {
                                "trades": int,
                                "sold_points": int,
                                "sold_on_market": int,
                                "sold_in_bazaar": int,
                                "items_sent": int,
                                "bazaar_profit": int,
                                "auctions": int,
                            },
                        ),
                        "other": typing.TypedDict(
                            "",
                            {
                                "years_played": int,
                                "stat_enhancers_used": int,
                                "merits_bought": int,
                                "logins": int,
                                "energy_refills": int,
                                "company_trains": int,
                            },
                        ),
                        "jobs": typing.TypedDict(
                            "",
                            {
                                "unemployed": int,
                                "medical": int,
                                "law": int,
                                "grocer": int,
                                "education": int,
                                "company": int,
                                "casino": int,
                                "army": int,
                            },
                        ),
                        "jail": typing.TypedDict(
                            "",
                            {
                                "jailings": int,
                                "busts_failed": int,
                                "busts": int,
                                "bails_spent": int,
                                "bails": int,
                            },
                        ),
                        "items": typing.TypedDict(
                            "",
                            {
                                "trashed": int,
                                "total": int,
                                "found_in_dump": int,
                                "found_in_city": int,
                            },
                        ),
                        "hospital": typing.TypedDict(
                            "",
                            {"trips": int, "revives": int, "medical_items_used": int},
                        ),
                        "drugs": typing.TypedDict(
                            "",
                            {
                                "xanax": int,
                                "vicodin": int,
                                "total_used": int,
                                "speed": int,
                                "shrooms": int,
                                "pcp": int,
                                "overdoses": int,
                                "opium": int,
                                "lsd": int,
                                "ketamine": int,
                                "ecstasy": int,
                                "cannabis": int,
                            },
                        ),
                        "currency": typing.TypedDict(
                            "",
                            {
                                "points_used": int,
                                "points_total": int,
                                "points_players": int,
                                "points_market": int,
                                "points_factions": int,
                                "money_on_hand_average": int,
                                "money_on_hand": int,
                                "money_in_bank": int,
                            },
                        ),
                        "crimes": typing.TypedDict(
                            "", {"total": int, "jail_sentences": int}
                        ),
                        "communication": typing.TypedDict(
                            "",
                            {
                                "total_messages": int,
                                "spouses": int,
                                "personals_placed": int,
                                "friends": int,
                                "coworkers": int,
                                "classified_ads_placed": int,
                            },
                        ),
                        "bounties": typing.TypedDict(
                            "", {"placed": int, "money_spent": int}
                        ),
                        "attacking": typing.TypedDict(
                            "",
                            {
                                "rounds_fired": int,
                                "respect_gained": int,
                                "money_mugged": int,
                                "misses": int,
                                "hits": int,
                                "escapes": int,
                                "critical_hits": int,
                                "attacks_won": int,
                                "attacks_stealthed": int,
                                "attacks_stalemated": int,
                                "attacks_lost": int,
                            },
                        ),
                    },
                ),
            ),
        )
