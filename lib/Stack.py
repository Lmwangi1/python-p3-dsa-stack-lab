class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        # Returns distance from top (0-based), or -1 if not found
        try:
            index = self.items[::-1].index(target)  # index from top
            return index
        except ValueError:
            return -1
