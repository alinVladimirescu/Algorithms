class Deque:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        return len(self.data) == 0
    def length(self):
        return len(self.data)
    def addFirst(self, value : int):
        if self.isEmpty():
            self.data.append(value)
            return
        self.data.insert(0, value)
    def addLast(self, value: int):
        self.data.append(value)
    def removeFirst(self):
        if self.isEmpty():
            return
        self.data.remove(0)
    def removeLast(self):
        if self.isEmpty():
            return
        self.data.pop()


if __name__ == "__main__":
    dq = Deque()
    dq.addFirst(1)
    dq.addFirst(2)
    dq.addLast(3)
    dq.addFirst(0)
    print(dq.isEmpty())
    print(dq.data)
    dq.removeFirst()
    print(dq.data)
    dq.removeLast()
    print(dq.data)
    print(dq.length())