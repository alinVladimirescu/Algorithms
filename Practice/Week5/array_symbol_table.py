def binary_search(arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return None
def binary_search2(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l
       
class ArraySymbolTable:
    def __init__(self):
        self.keys = []
        self.values = []
    
    def get(self, key):
        index = binary_search(self.keys, key)
        if index is not None:
            return self.values[index]
        else:
            return None
    def put(self, key, value):
        insert_index = binary_search2(self.keys, key)
        if self.get(key) is None:
            self.keys.insert(insert_index, key)
            self.values.insert(insert_index, value)
        else:
            self.values[insert_index] += value
    def __str__(self):
        string = ""
        for item in zip(self.keys, self.values):
            string += f"{item[0]} : {item[1]}\n"
        return string

    
symbol_table = ArraySymbolTable()
symbol_table.put(1, 1)
symbol_table.put(2, 1)
symbol_table.put(3, 1)
symbol_table.put(1, 1)
print(symbol_table)
print(symbol_table.get(1))
