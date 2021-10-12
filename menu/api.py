import requests as rq
url = 'https://c900-186-84-90-148.ngrok.io/status-game'

def get_status():
    response = rq.get(url)
    return response.json()

def set_status():
    body = {"status": True, "name": "oscar"}
    response = rq.post(url, data = body)
    return response.json()

print(get_status())
print(set_status())
print(get_status())