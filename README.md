[![The-Odds-API](https://github.com/coreyjs/the-odds-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/coreyjs/the-odds-api/actions/workflows/python-app.yml)


# The Odds API (Unofficial) Client for the-odds-api.com

(This is basically a rough draft.  Kinda quick and dirty for now)

You will need to acquire an API KEY from [The Odds API](https://the-odds-api.com/) to use this client.

```python
pip install the-odds
```

### Contact
Im available on [Bluesky](https://bsky.app/profile/coreyjs.dev) for any questions or just general chats about enhancements.


# Installation and Setup
```
pip install the-odds
```

```python
from the_odds import OddsApiClient

client = OddsApiClient(api_key='your_key')

# for debug logging and request logging
client = OddsApiClient(api_key='your_key', debug=True)
```

## Available Endpoints

### Get Sports

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/v4/sports`  
**Method:** GET  
**Formats:** JSON


| Param | Type | Ex           | Note |
|-------|------|--------------|----|
| all   | bool | True / False | Optional - if this parameter is set to true (all=true), a list of both in and out of season sports will be returned |

</details>

```python
sports = client.v4.get_sports()
```