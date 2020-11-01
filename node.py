from abc import ABC


class Node(ABC):
    def __hash__(self):
        pass

    def __eq__(self, other: 'Node'):
        pass
