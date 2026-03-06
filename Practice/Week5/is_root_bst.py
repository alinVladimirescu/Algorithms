class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTSymbolTable:
    def __init__(self):
        self.root = None
        self.size = 0
        
    
    def get(self, key):
        current = self.root
        while current:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None
    def put(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            self.size += 1
            return
        current = self.root
        while current:
            if key == current.key:
                current.value = value
                return
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key, value)
                    self.size += 1
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(key, value)
                    self.size += 1
                    return
                else:
                    current = current.right
    def __str__(self):
        string = ""
        def inorder_traversal(node):
            nonlocal string
            if node:
                inorder_traversal(node.left)
                string += f"{node.key} : {node.value}\n"
                inorder_traversal(node.right)
        inorder_traversal(self.root)
        return string

def is_root(node, min_key, max_key):
    if node is None:
       return True
    if node.key < min_key or node.key > max_key:
        return False
    return is_root(node.left, min_key, node.key) and is_root(node.right, node.key, max_key)

def search_bst(node, x, y, result = []):
    if node is None:
        return result
    if node.key > x:
        search_bst(node.left, x, y, result)
    
    if x < node.key < y:
        result.append(node.key)
    
    if node.key < y:
        search_bst(node.right, x, y, result)
    return result
if __name__ == "__main__":
    symbol_table = BSTSymbolTable()
    symbol_table.put(1, 1)
    symbol_table.put(2, 1)
    symbol_table.put(3, 1)
    symbol_table.put(1, 1)
    print(symbol_table)
    print(symbol_table.get(1))
    print(is_root(symbol_table.root, float('-inf'), float('inf')))
    print(is_root(symbol_table.root.left, float('-inf'), float('inf')))
    print(is_root(symbol_table.root.right, float('-inf'), symbol_table.root.key))
    print(search_bst(symbol_table.root, 0, 4))