class Node:
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node


class LinkedListSymbolTable:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def put(self, key, value):
        if key is None:
            raise ValueError("Key cannot be None")
        
        current = self.head
        while current:
            if current.key == key:
                current.value = value 
                return
            current = current.next
        
        new_node = Node(key, value, self.head)
        self.head = new_node
        self.size += 1
    
    def get(self, key):
        if key is None:
            return None
        
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None   
    
    def delete(self, key):
        if key is None or self.head is None:
            return
        
        if self.head.key == key:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
    
    def contains(self, key):
        return self.get(key) is not None
    
    def is_empty(self):
        return self.size == 0
    
    def size_of(self):
        return self.size
    
    def keys(self):
        keys_list = []
        current = self.head
        while current:
            keys_list.append(current.key)
            current = current.next
        return keys_list
    
    def values(self):
        values_list = []
        current = self.head
        while current:
            values_list.append(current.value)
            current = current.next
        return values_list
    
    def items(self):
        items_list = []
        current = self.head
        while current:
            items_list.append((current.key, current.value))
            current = current.next
        return items_list
    
    def __str__(self):
        if self.is_empty():
            return "{}"
        
        items = []
        current = self.head
        while current:
            items.append(f"{current.key}: {current.value}")
            current = current.next
        
        return "{" + ", ".join(items) + "}"


if __name__ == "__main__":
    st = LinkedListSymbolTable()
    
    print("Testing Symbol Table Operations:")
    print(f"Is empty: {st.is_empty()}")
    
    st.put("apple", 5)
    st.put("banana", 3)
    st.put("cherry", 8)
    st.put("date", 2)
    
    print(f"After inserting 4 items: {st}")
    print(f"Size: {st.size_of()}")
    
    print(f"Get 'apple': {st.get('apple')}")
    print(f"Get 'banana': {st.get('banana')}")
    print(f"Get 'nonexistent': {st.get('nonexistent')}")
    
    print(f"Contains 'cherry': {st.contains('cherry')}")
    print(f"Contains 'grape': {st.contains('grape')}")
    
    st.put("apple", 10)  
    print(f"After updating 'apple': {st}")
    st.delete("banana")
    print(f"After deleting 'banana': {st}")
    print(f"Size after deletion: {st.size_of()}")
    
    print(f"Keys: {st.keys()}")
    print(f"Values: {st.values()}")
    print(f"Items: {st.items()}")