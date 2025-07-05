import sys

from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st
from torngen.path import __all__ as __all_base_resources__

all_base_resources = [
    getattr(sys.modules["torngen.path"], name) for name in __all_base_resources__
]
all_paths = []
for cls in all_base_resources:
    instance = cls()
    for key, path in instance.__class__.__dict__.items():
        if (
            not key.startswith("__")
            and "id}" not in key.lower()
            and "ids}" not in key.lower()
        ):
            all_paths.append((cls, path))


@st.composite
def single_path_strategy(draw):
    return draw(st.sampled_from(all_paths))


@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
@given(test_data=single_path_strategy())
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
