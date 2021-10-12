import requests as rq


class Api:
    def __init__(self):
        self.url = 'https://c900-186-84-90-148.ngrok.io/'

    def get_status(self):
        response = rq.get(self.url+'status-game')
        return response.json()

    def set_status(self):
        body = {"status": True, "name": "David"}
        response = rq.post(self.url+'status-game', data=body)
        return response.json()

    def set_ready(self):
        response = rq.post(self.url+'start-player-1')
        return response.json()

    def all_ready(self):
        response = rq.get(self.url + 'ready')
        return response.json()