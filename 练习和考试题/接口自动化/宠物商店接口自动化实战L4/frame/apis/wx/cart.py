import requests


class Cart:
    def __init__(self, token):
        self.send = requests.request
        self.token = token

    def add(self):
        pass
