import pytest

from torngen import BaseQuery
from torngen.path import User


def test_empty_query():
    query = BaseQuery()

    assert query.api_key is None
    assert len(query.parameters) == 0
    assert len(query.selections) == 0


def test_query_selection():
    with pytest.raises(TypeError):
        BaseQuery().select("foo")

    with pytest.raises(TypeError):
        BaseQuery().select(BaseQuery())

    with pytest.raises(TypeError):
        BaseQuery().select(User.revives)

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

