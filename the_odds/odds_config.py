class OddsConfig:
    def __init__(
        self,
        api_key: str,
        debug: bool = False,
        timeout: int = 15,
        ssl_verify: bool = True,
    ) -> None:
        self.api_key = api_key
        self.debug = debug
        self.timeout = timeout
        self.ssl_verify = ssl_verify
        self.v4_base_url = "https://api.the-odds-api.com/v4"
