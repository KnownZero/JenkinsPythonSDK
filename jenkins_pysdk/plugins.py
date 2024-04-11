__all__ = ["Plugins"]


class Plugins:
    def __init__(self, jenkins):
        self._jenkins = jenkins

    @property
    def updates(self):
        raise NotImplemented

