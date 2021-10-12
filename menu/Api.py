import requests as rq


class Api:
    def __init__(self):
        self.url = 'https://c900-186-84-90-148.ngrok.io/status-game'

    def get_status(self):
        response = rq.get(self.url)
        return response.json()

    def set_status(self):
        body = {"status": True, "name": "David"}
        response = rq.post(self.url, data=body)
        return response.json()