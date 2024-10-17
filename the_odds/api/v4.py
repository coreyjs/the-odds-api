from typing import Optional, List


class V4:
    def __init__(self, client):
        self._client = client

    def get_sports(self, all: Optional[bool] = False) -> List[dict]:

        params = {"all": all}
        return self._client.get(resource="/sports", params=params)

    def get_odds(
        self,
        sport: str,
        regions: List[str],
        markets: List[str],
        event_ids: List[str] = None,
        bookmakers: List[str] = None,
        commence_time_to: str = None,
        commence_time_from: str = None,
        include_links: bool = None,
        include_sids: bool = None,
        include_bet_limits: bool = None,
        date_format: str = "iso",
        odds_format: str = "decimal",
    ) -> List[dict]:
        """
        Returns a list of upcoming and live games with recent odds for a given sport, region and market.

        Documentation: https://the-odds-api.com/liveapi/guides/v4/#get-odds

        :param sport: The sport key obtained from calling the /sports endpoint. upcoming is always valid, returning
        any live games as well as the next 8 upcoming games across all sports.

        An example are the following: ['americanfootball_cfl', 'americanfootball_ncaaf', 'americanfootball_ncaaf_championship_winner',
         'americanfootball_nfl', 'americanfootball_nfl_super_bowl_winner', 'baseball_kbo', 'baseball_mlb', 'baseball_mlb_world_series_winner',
         'baseball_npb', 'basketball_euroleague', 'basketball_nba', 'basketball_nba_championship_winner', 'basketball_nba_preseason',
         'basketball_nbl', 'basketball_ncaab_championship_winner', 'boxing_boxing', 'cricket_international_t20', 'cricket_test_match',
         'golf_masters_tournament_winner', 'golf_pga_championship_winner', 'icehockey_nhl', 'icehockey_nhl_championship_winner',
         'icehockey_sweden_allsvenskan', 'icehockey_sweden_hockey_league', 'mma_mixed_martial_arts', 'politics_us_presidential_election_winner',
          'soccer_argentina_primera_division', 'soccer_australia_aleague', 'soccer_austria_bundesliga', 'soccer_belgium_first_div',
           'soccer_brazil_campeonato', 'soccer_brazil_serie_b', 'soccer_chile_campeonato', 'soccer_china_superleague',
           'soccer_conmebol_copa_libertadores', 'soccer_denmark_superliga', 'soccer_efl_champ', 'soccer_england_league1',
           'soccer_england_league2', 'soccer_epl', 'soccer_fifa_world_cup_winner', 'soccer_finland_veikkausliiga',
           'soccer_france_ligue_one', 'soccer_france_ligue_two', 'soccer_germany_bundesliga', 'soccer_germany_bundesliga2',
            'soccer_germany_liga3', 'soccer_greece_super_league', 'soccer_italy_serie_a', 'soccer_italy_serie_b',
            'soccer_japan_j_league', 'soccer_korea_kleague1', 'soccer_league_of_ireland', 'soccer_mexico_ligamx',
            'soccer_netherlands_eredivisie', 'soccer_norway_eliteserien', 'soccer_poland_ekstraklasa', 'soccer_portugal_primeira_liga',
            'soccer_spain_la_liga', 'soccer_spain_segunda_division', 'soccer_spl', 'soccer_sweden_allsvenskan', 'soccer_sweden_superettan',
             'soccer_switzerland_superleague', 'soccer_turkey_super_league', 'soccer_uefa_champs_league', 'soccer_usa_mls']


        :param commence_time_from: Optional - filter the response to show games that commence on and after this parameter. Values are in ISO 8601 format, for example 2023-09-09T00:00:00Z. This parameter has no effect if the sport is set to 'upcoming'.
        :param odds_format:   Optional - Determines the format of odds in the response. Valid values are decimal and
        american. Defaults to decimal. When set to american, small discrepancies might exist for some bookmakers due
        to rounding errors.
        :param date_format: Optional - Determines the format of timestamps in the response. Valid values are unix and iso (ISO 8601). Defaults to iso.
        :param include_bet_limits: Optional - if "true", the response will include the bet limit of each betting option, mainly available for betting exchanges. Valid values are "true" or "false"
        :param include_sids:  Optional - if "true", the response will include source ids (bookmaker ids) for events, markets and outcomes if available. Valid values are "true" or "false". This field can be useful to construct your own links to handle variations in state or mobile app links.
        :param commence_time_to: Optional - filter the response to show games that commence on and before this parameter. Values are in ISO 8601 format, for example 2023-09-10T23:59:59Z. This parameter has no effect if the sport is set to 'upcoming'.
        :param bookmakers: Optional - Comma-separated list of bookmakers to be returned. If both bookmakers and regions are both specified, bookmakers takes priority. Bookmakers can be from any region. Every group of 10 bookmakers is the equivalent of 1 region. For example, specifying up to 10 bookmakers counts as 1 region. Specifying between 11 and 20 bookmakers counts as 2 regions.
        :param event_ids: Optional List[str] - List of game ids. Filters the response to only return games with the specified ids.
        :param include_links: Optional - if "true", the response will include bookmaker links to events, markets, and betslips if available. Valid values are "true" or "false"
        :param regions:
        :param markets: Optional - Determines which odds market is returned. Defaults to h2h (head to head / moneyline).
        Valid markets are h2h (moneyline), spreads (points handicaps), totals (over/under) and outrights (futures).
         Multiple markets can be specified if comma delimited. spreads and totals markets are mainly available for
         US sports and bookmakers at this time. Each specified market costs 1 against the usage quota, for each
         region.Lay odds are automatically included with h2h results for relevant betting exchanges
          (Betfair, Matchbook etc). These have a h2h_lay market key.For sports with outright markets (such as Golf),
          the market will default to outrights if not specified. Lay odds for outrights (outrights_lay)
          will automatically be available for relevant exchanges.
        :return: List[dict]
        """
        if not markets:
            markets = ["h2h"]
        params = {
            "regions": ",".join(regions),
            "markets": ",".join(markets),
            "dateFormat": date_format,
            "oddsFormat": odds_format,
        }

        if event_ids:
            params["eventIds"] = ",".join(event_ids)
        if bookmakers:
            params["bookmakers"] = ",".join(bookmakers)
        if commence_time_to:
            params["commenceTimeTo"] = commence_time_to
        if commence_time_from:
            params["commenceTimeFrom"] = commence_time_from
        if include_links:
            params["includeLinks"] = include_links
        if include_sids:
            params["includeSids"] = include_sids
        if include_bet_limits:
            params["includeBetLimits"] = include_bet_limits

        return self._client.get(resource=f"/sports/{sport}/odds", params=params)
