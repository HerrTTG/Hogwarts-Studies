import requests


class Service:

    def __init__(self):
        self.r = None

    def get(self, value):
        self.r = requests.get(**value).text

    @property
    def result(self):
        return self.r

    def run_step(self, step: dict):
        for key, value in step.items():
            if key == 'get':
                self.get(value)
                break
            elif key == 'assert':
                assert eval(value)
                break
        else:
            return False
        return True


# 将对象初始化
service: Service = None
