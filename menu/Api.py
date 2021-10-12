import requests as rq


class Api:
    def __init__(self):
        self.url = 'http://localhost:3000/status-game'

    def get_status(self):
        response = rq.get(self.url)
        return response.json()

    def set_status(self):
        body = {"status": True, "name": "oscar"}
        response = rq.post(self.url, data=body)
        return response.json()