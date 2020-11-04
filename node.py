from abc import ABC
from uuid import UUID, uuid4


class Node(ABC):
    def __init__(self, uuid: UUID = None):
        self._uuid = uuid if uuid else uuid4()

    def __hash__(self):
        return self._uuid

    def __eq__(self, other):
        return self.uuid == other.uuid

    @property
    def uuid(self) -> UUID:
        """UUID узла графа."""
        return self._uuid
