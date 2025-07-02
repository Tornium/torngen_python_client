import sys
from hypothesis import given, settings, HealthCheck, strategies as st
from torngen.path import __all__ as __all_base_resources__

all_base_resources = [getattr(sys.modules["torngen.path"], name) for name in __all_base_resources__]


@st.composite
def single_path_strategy(draw):
    cls = draw(st.sampled_from(all_base_resources))
    paths = [
        path
        for key, path in cls().__class__.__dict__.items()
        if not key.startswith("__") and "id}" not in key.lower()
    ]
    return cls, draw(st.sampled_from(paths))


@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
@given(test_data=single_path_strategy())
def test_fuzzy_single_selection(api_key, requests_adapter, test_data):
    base_resource, selection = test_data

    query = (
        base_resource()
        .select(selection)
        .key(api_key)
    )
    if "id}" in query.url().lower():
        # NOTE: selections containing a resource using a path parmeter are skipped
        # as the logic to determine how to fill the path parameter correctly is 
        # not ready yet
        return

    print(query.url())

    query.get(adapter=requests_adapter).parse()
