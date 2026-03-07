class Node:
    def __init__(self, key, value, new_node = None):
        self.key = key
        self.value = value
        self.next = new_node
class SymbolTable:
    def __init__(self):
        self.head = None
        self.size = 0
    def put(self, key, value):
        if key is None:
            raise KeyError("Key is null")
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value, self.head)
        self.head = new_node
        self.size += 1
        return
    def get(self, key):
        if key is None:
            raise KeyError("Key is null")
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def __str__(self):
        if self.head is None:
            return "{}"
        
        items = []
        current = self.head
        while current:
            items.append(f"{current.key}: {current.value}")
            current = current.next
        
        return "{" + ", ".join(items) + "}"
    
    
class WebTracker:
    def __init__(self):
        self.history = SymbolTable()
    def record_visit(self, user, website):
        user_table = self.history.get(user)
        if user_table is None:
            user_table = SymbolTable()
            self.history.put(user, user_table)
        visit_count = user_table.get(website)
        if visit_count is None:
            user_table.put(website, 1)
        else:
            user_table.put(website, visit_count + 1)
    def has_visited(self, user, website):
        user_table = self.history.get(user)
        if user_table is not None:
            return True if user_table.get(website) is not None else False
        return None
    def visit_count(self, user, website):
        user_table = self.history.get(user)
        if user_table is not None:
            return user_table.get(website) if user_table.get(website) is not None else 0
        return 0


if __name__ == "__main__":
    tracker = WebTracker()
    
    tracker.record_visit("Alice", "google.com")
    tracker.record_visit("Bob", "youtube.com")
    tracker.record_visit("Alice", "google.com")
    tracker.record_visit("Alice", "reddit.com")
    
    print("Has Alice visited google.com?", tracker.has_visited("Alice", "google.com"))
    print("How many times did Alice visit google.com?", tracker.visit_count("Alice", "google.com"))
    print("How many times did Bob visit google.com?", tracker.visit_count("Bob", "google.com"))
    
    print(tracker.history)