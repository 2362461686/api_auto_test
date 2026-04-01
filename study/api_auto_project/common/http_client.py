import requests

class HttpClient:
    @staticmethod
    def post(url, json=None):
        return requests.post(url, json=json)