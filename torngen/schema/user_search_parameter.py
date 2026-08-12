import typing

UserSearchParameter = (
    str
    | str
    | typing.Literal[
        "married",
        "notMarried",
        "traveling",
        "notTraveling",
        "inFaction",
        "notInFaction",
        "inCompany",
        "notInCompany",
        "inHospital",
        "notInHospital",
        "inJail",
        "notInJail",
        "inFederalJail",
        "notInFederalJail",
        "male",
        "female",
        "enby",
        "lastActionNow",
        "lastActionRecent",
        "lastActionHourAgo",
        "lastActionDayAgo",
        "lastActionWeekAgo",
        "lastActionMonthAgo",
        "lastActionYearAgo",
    ]
)
