# from data_golf.api.betting import Betting
# from data_golf.api.prediction import Prediction
# from data_golf.config import DGConfig
# from data_golf.http_client import HttpClient
# from data_golf.api.general import General
# from data_golf.api.live_prediction import LivePrediction
from the_odds.http_client import HttpClient
from the_odds.odds_config import OddsConfig
from the_odds.api.v4 import V4


class OddsApiInvalidApiKey(Exception):
    pass


class OddsApiClient:
    def __init__(
        self,
        api_key: str,
        debug: bool = False,
        timeout: int = 15,
        ssl_verify: bool = True,
    ) -> None:
        self._validate_api_key(api_key)

        self._config = OddsConfig(
            api_key=api_key, debug=debug, timeout=timeout, ssl_verify=ssl_verify
        )
        self._http_client = HttpClient(self._config)

        # Endpoints
        # self.general = General(self._http_client)
        # self.predictions = Prediction(self._http_client)
        # self.live_predictions = LivePrediction(self._http_client)
        # self.betting = Betting(self._http_client)
        self.v4 = V4(self._http_client)

    def _validate_api_key(self, api_key: str) -> None:
        """
        Private method to validate the API key.
        :param api_key:
        :return:
        """
        if not isinstance(api_key, str):
            raise OddsApiInvalidApiKey("API key must be a string.")
        if not api_key:
            raise OddsApiInvalidApiKey("API key cannot be empty.")
