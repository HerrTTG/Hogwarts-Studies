import requests


class Cart:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.send = requests.request


    def add(self):
        pass
