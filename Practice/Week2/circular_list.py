class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularList:
    def __init__(self):
        self.root = None
        self.size = 0
    def isEmpty(self):
        return self.root is None
    def length(self):
        return self.size
    def append(self, data):
        new_node = Node(data)
        current = self.root
        if self.isEmpty():
            self.root = new_node
            new_node.next = new_node
        else:
            while current.next != self.root:
                current = current.next
            current.next = new_node
            new_node.next = self.root
        self.size += 1
    def prepend(self, data):
        new_node = Node(data)
        current = self.root
        if self.isEmpty():
            self.root = new_node
            new_node.next = new_node
        else:
            while current.next != self.root:
                current = current.next
            new_node.next = self.root
            current.next = new_node
            self.root = new_node
        self.size += 1
    def delete(self, pos):
        if self.isEmpty() or pos >= self.size or pos < 0:
            return
        if self.size == 1:
            item = self.root.data
            self.root = None
            self.size = 0
            return item
        if pos == 0:
            item = self.root.data
            self.root = self.root.next
            self.size -= 1
            return item
        current = self.root
        for _ in range(pos - 1):
            current = current.next
        item = current.next.data
        current.next = current.next.next
        self.size -= 1
        return item
    def access(self, pos):
        if pos >= self.size or self.isEmpty() or pos < 0:
            return
        current = self.root
        for _ in range(pos):
            current = current.next
        return current.data

cl = CircularList()
cl.append(1)
cl.append(2)
cl.prepend(0)
print(cl.access(0))
print(cl.access(1))
print(cl.access(2))
print(cl.delete(1))
print(cl.access(0))
print(cl.access(1))