import pytest

from the_odds import OddsApiClient


@pytest.fixture(scope="function")
def odds_client() -> OddsApiClient:
    yield OddsApiClient(api_key="test_key")
