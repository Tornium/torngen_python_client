import os

import pytest
import requests
from torngen import HTTPAdapter


class RequestsAdapter(HTTPAdapter):
    @staticmethod
    def get(url, headers):
        return requests.get(url, headers=headers).json()

    @staticmethod
    def version():
        return "Requests/Unknown"

    @staticmethod
    def client_name():
        return "torngen-unit-test"


@pytest.fixture
def api_key():
    secret = os.environ.get("API_KEY")

    if secret is None:
        raise ValueError("An API key is required to execute these tests")

    return secret


@pytest.fixture
def requests_adapter():
    return RequestsAdapter
