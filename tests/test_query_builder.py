import pytest
import requests

from torngen import BaseQuery, HTTPAdapter
from torngen.path import User


class RequestsAdapter(HTTPAdapter):
    def get(url, headers):
        return requests.get(url, headers=headers).json()

    def version():
        return "Requests/Unknown"

    def client_name():
        return "torngen-unit-test"


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


def test_query_url():
    url = User().select(User.revives, User.attacks).limit(10).key("1234abcd1234abcd").url()

    assert url == "https://api.torn.com/v2/user/?selections=attacks,revives&limit=10"


def test_parsing():
    User().select(User.revives).limit(10).key("None").get(adapter=RequestsAdapter).parse()
