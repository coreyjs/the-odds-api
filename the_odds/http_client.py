from typing import Tuple

from the_odds.odds_config import OddsConfig
from the_odds.request_helpers import RequestHelpers

import httpx
import logging


class OddsApiForbidden(Exception):
    pass


class OddsApiBadRequest(Exception):
    pass


class HttpClient:
    def __init__(self, config: OddsConfig) -> None:
        self._config = config
        if self._config.debug:
            logging.basicConfig(level=logging.INFO)

    def _build_request(
        self,
        resource: str,
        query_params: dict,
    ) -> Tuple[str, dict]:
        """
        Private method to build the URL for the The-Odds-API API.
        :param resource:
        :return:
        """
        query_params["apiKey"] = self._config.api_key

        url = f"{self._config.v4_base_url}{resource}?"

        return url, query_params

    @RequestHelpers.prepare_request
    def get(self, resource: str, params: dict = None, **kwargs) -> httpx.request:
        """
        Private method to make a get request to the Data Golf API.  This wraps the lib httpx functionality.
        :param params:
        :param resource:
        :return:
        """
        with httpx.Client(
            verify=self._config.ssl_verify, timeout=self._config.timeout
        ) as client:
            url, q = self._build_request(
                resource=resource,
                query_params=params if params else {},
            )
            r: httpx.request = client.get(
                url=url,
                params=q,
                **kwargs,
            )

        if r.status_code == 403:
            raise OddsApiForbidden("403 Forbidden: Check your API key.")

        if r.status_code == 400:
            raise OddsApiForbidden(r.content)

        if self._config.debug:
            logging.info(f"API URL: {r.url}")
            logging.info(kwargs["headers"])

        return r.json()
