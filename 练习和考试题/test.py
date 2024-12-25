import abc


class PerMeta(type):
    ...


class Record(abc.ABC, metaclass=PerMeta):
    ...


hhh = Record()
