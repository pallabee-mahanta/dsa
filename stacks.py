# implement stacks with fixed size array

class FixedStack:
    """Fixed-size stack implemented on top of a preallocated list (array)."""
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self._data = [None] * capacity
        self._top = -1
        self._capacity = capacity

    def push(self, item):
        if self.is_full():
            raise IndexError("push to full stack")
        self._top += 1
        self._data[self._top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[self._top]

    def is_empty(self) -> bool:
        return self._top == -1

    def is_full(self) -> bool:
        return self._top + 1 == self._capacity

    def size(self) -> int:
        return self._top + 1

    def capacity(self) -> int:
        return self._capacity

    def __len__(self):
        return self.size()

    def __repr__(self):
        return f"FixedStack(size={self.size()}, capacity={self._capacity})"

# implement stacks with linked list

class _Node:
    __slots__ = ("value", "next")
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedListStack:
    """Singly-linked (one-sided), non-cyclic stack implemented with nodes."""
    def __init__(self, iterable=None):
        self._head = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, item):
        self._head = _Node(item, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        node = self._head
        self._head = node.next
        self._size -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._head.value

    def is_empty(self) -> bool:
        return self._head is None

    def size(self) -> int:
        return self._size

    def clear(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"LinkedListStack(size={self._size})"