import pytest

from the_odds import OddsApiClient
from the_odds.odds_client import OddsApiInvalidApiKey


def test_client_responds_to_v4():
    oac = OddsApiClient(api_key="test_key")
    assert oac.v4 is not None


def test_client_will_err_on_invalid_api_key():
    with pytest.raises(OddsApiInvalidApiKey):
        OddsApiClient(api_key=1234)
