import random
import sys
import typing
import urllib.parse

import pytest
from torngen.base_query import _URLComponents, BaseQuery
from torngen.path import __all__ as __all_base_resources__

all_base_resources = [
    getattr(sys.modules["torngen.path"], name) for name in __all_base_resources__
]
all_paths = {}

cls: typing.Type[BaseQuery]
for cls in all_base_resources:
    instance = cls()
    for key, path in instance.__class__.__dict__.items():
        if (
            not key.startswith("__")
            and "id}" not in key.lower()
            and "ids}" not in key.lower()
        ):
            # all_paths.append((cls, path))
            url = urllib.parse.urlunparse(
                _URLComponents(
                    scheme="",
                    netloc="",
                    path=f"/{key}/{path.selection}",
                    params="",
                    query="",
                    fragment="",
                )
            )
            all_paths[url] = (cls, path)


@pytest.mark.parametrize("test_data", all_paths.values(), ids=all_paths.keys())
def test_fuzzy_single_selection(api_key, requests_adapter, test_data):
    base_resource, selection = test_data
    query = base_resource().select(selection).key(api_key)

    try:
        print(query.url())
        response = query.get(adapter=requests_adapter)
    except RuntimeError:
        # NOTE: selections containing a resource using a path parmeter are skipped
        # as the logic to determine how to fill the path parameter correctly is
        # not ready yet
        return

    try:
        response.parse()
    except Exception as e:
        print(response.response)
        raise e
