import pytest
from torngen import BaseQuery
from torngen.path import FactionId, User


def test_empty_query():
    query = BaseQuery("test")

    assert query.api_key is None
    assert len(query.parameters) == 0
    assert len(query.selections) == 0


def test_query_selection():
    with pytest.raises(TypeError):
        BaseQuery("test").select("foo")

    with pytest.raises(TypeError):
        BaseQuery("test").select(BaseQuery("test"))

    with pytest.raises(TypeError):
        BaseQuery("test").select(User.revives)

    query = User().select(User.revives, User.attacks)

    assert len(query.parameters) == 0
    assert len(query.selections) == 2
    assert User.revives in query.selections
    assert User.attacks in query.selections


def test_query_parameters():
    with pytest.raises(ValueError):
        User().id(10)

    query = User().select(User.revives).limit(10)
    assert len(query.parameters) == 1
    assert len(query.selections) == 1
    assert User.revives in query.selections
    assert query.parameters.get("limit") == 10


def test_query_api_key():
    return


def test_query_parameter_url():
    url = (
        User()
        .select(User.revives, User.attacks)
        .limit(10)
        .key("1234abcd1234abcd")
        .url()
    )

    assert url == "https://api.torn.com/v2/user/?selections=attacks,revives&limit=10"


def test_path_parameter_url():
    url = FactionId().select(FactionId.members).id(15644).key("1234abcd1234abcd").url()

    assert url == "https://api.torn.com/v2/faction/15644/?selections=members"
