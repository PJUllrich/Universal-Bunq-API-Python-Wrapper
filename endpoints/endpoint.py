

class Endpoint:

    endpoint_chat = "chat"

    def __init__(self, api_client):
        self.api_client = api_client

    def _make_get_request(self, endpoint):
        res = self.api_client.get(endpoint)
        return res.json()["Response"]
