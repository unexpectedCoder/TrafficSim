from abstract import Node


class Crossroad(Node):
    def __init__(self, **kwargs):
        Node.__init__(self, **kwargs)
        self.__hash__ = Node.__hash__
        self.__eq__ = Node.__eq__

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"
