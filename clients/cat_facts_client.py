import requests
import json
from config import BASE_URL

class CatFactsClient:
    def __init__(self):
        self.base_url = BASE_URL

    def _make_request(self, method, endpoint, **kwargs):
        """
        A centralized method to make requests and log the response.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, **kwargs)
        
        # Log the response
        try:
            print(f"\nResponse from {url}: {json.dumps(response.json(), indent=2)}")
        except json.JSONDecodeError:
            print(f"\nResponse from {url}: {response.text}")
            
        return response

    def get_random_fact(self):
        """
        Retrieves a random cat fact.
        """
        return self._make_request("GET", "fact")

    def get_facts(self, limit=None):
        """
        Retrieves a list of cat facts, with an optional limit.
        """
        params = {}
        if limit:
            params['limit'] = limit
        return self._make_request("GET", "facts", params=params)

    def get_breeds(self):
        """
        Retrieves a list of cat breeds.
        """
        return self._make_request("GET", "breeds")
