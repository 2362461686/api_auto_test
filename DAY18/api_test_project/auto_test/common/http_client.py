import requests

class HttpClient:
    @staticmethod
    def post(url, json=None, headers=None):
        if headers is None:
            headers = {"Content-Type": "application/json"}
        return requests.post(url, json=json, headers=headers)