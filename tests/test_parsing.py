from torngen.path import FactionId, Market, User


def test_manual_user(api_key, requests_adapter):
    response = (
        User()
        .select(User.education, User.attacks, User.bounties, User.organizedcrime)
        .limit(10)
        .key(api_key)
        .get(adapter=requests_adapter)
        .parse()
    )

    assert len(response["attacks"].attacks) <= 10
    assert len(response["bounties"].bounties) <= 10
    assert isinstance(response["education"].education.complete, list)


def test_manual_faction(api_key, requests_adapter):
    response = (
        FactionId()
        .select(FactionId.basic, FactionId.members)
        .id(15644)
        .key(api_key)
        .striptags(True)
        .get(adapter=requests_adapter)
        .parse()
    )

    assert len(response["members"].members) >= 10
    assert response["basic"].basic.name is not None
    assert response["basic"].basic.best_chain >= 0
    assert response["basic"].basic.is_enlisted is None or isinstance(
        response["basic"].basic.is_enlisted, bool
    )


def test_manual_market(api_key, requests_adapter):
    response = (
        Market()
        .select(Market.bazaar, Market.timestamp, Market.lookup)
        .key(api_key)
        .get(adapter=requests_adapter)
        .parse()
    )

    assert response["timestamp"].timestamp > 0
    assert len(response["lookup"].selections) > 2
