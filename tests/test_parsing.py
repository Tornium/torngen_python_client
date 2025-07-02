from torngen.path import User


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
