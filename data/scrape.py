import requests
from bs4 import BeautifulSoup
import json
from .models import Search


def get_search_results(search: Search) -> list:
    """Scrapes the search url for properties

    Args:
        search (Search): The search to scrape

    Returns:
        list: A list of properties
    """
    response = requests.get(
        search.url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        },
    )
    soup = BeautifulSoup(response.text, "html.parser")
    scripts = soup.findAll("script")
    data = "".join(scripts[5].text.split(" = ")[1:])
    return json.loads(data)["properties"]
