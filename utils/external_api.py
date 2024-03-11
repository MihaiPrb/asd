# utils/external_api.py

import requests

class ExternalAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def get(self, endpoint, params=None, headers=None):
        """
        Make a GET request to the external API.
        """
        url = f"{self.api_url}/{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    def post(self, endpoint, data=None, headers=None):
        """
        Make a POST request to the external API.
        """
        url = f"{self.api_url}/{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response.json()

    def put(self, endpoint, data=None, headers=None):
        """
        Make a PUT request to the external API.
        """
        url = f"{self.api_url}/{endpoint}"
        response = requests.put(url, json=data, headers=headers)
        return response.json()

    def delete(self, endpoint, headers=None):
        """
        Make a DELETE request to the external API.
        """
        url = f"{self.api_url}/{endpoint}"
        response = requests.delete(url, headers=headers)
        return response.json()