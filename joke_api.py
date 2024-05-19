# joke_api.py
import requests

BASE_URL = "https://icanhazdadjoke.com/"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Joker (https://github.com/themrhagan/Joker)"
}

def search_jokes(term, page=1, limit=20):
    """Search for dad jokes using a search term."""
    url = f"{BASE_URL}search"
    params = {
        "term": term,
        "page": page,
        "limit": limit
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()
