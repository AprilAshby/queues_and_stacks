class ListNode:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def __repr__(self):
        return f"ListNode({self.value}"


class Queue:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.size = 1 if node is not None else 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = ListNode(value)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            # new_node.next = self.head
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        removed = self.tail.value
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1
        return removed
