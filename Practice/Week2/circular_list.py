class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def length(self):
        return self.size
    def append(self, value):
        new_node = Node()
        if self.isEmpty():
            new_node = value
            new_node.next = None
        else:
            new_node = value
            new_node.next = head.next
