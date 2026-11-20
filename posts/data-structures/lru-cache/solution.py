class _Node:
    __slots__ = ("key", "value", "prev", "next")
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head, self.tail = _Node(), _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _touch(self, node):
        self._remove(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._touch(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key)
        if node is not None:
            node.value = value
            self._touch(node)
            return
        node = _Node(key, value)
        self.nodes[key] = node
        self._add_to_front(node)
        if len(self.nodes) > self.capacity:
            least_recent = self.tail.prev
            self._remove(least_recent)
            del self.nodes[least_recent.key]
