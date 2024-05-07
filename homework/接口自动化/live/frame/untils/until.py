import os


class Untils():
    @classmethod
    def get_path(cls):
        ## ..\\..\\..\\live
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # print(path)
        return path
