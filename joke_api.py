# joke_api.py
import requests

BASE_URL = "https://icanhazdadjoke.com/"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Joker (https://github.com/themrhagan/Joker)"
}

def search_jokes(term, page=1, limit=30):
    """Search for dad jokes using a search term."""
    url = f"{BASE_URL}search"
    params = {
        "term": term,
        "page": page,
        "limit": limit
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")
        return None
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects. Check the URL.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching jokes: {e}")
        return None

def get_random_joke():
    """Fetch a random dad joke."""
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")
        return None
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects. Check the URL.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None
