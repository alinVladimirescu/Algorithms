import collections

class Graph:
    def __init__(self, n):
        self.adj = collections.defaultdict(list)
        self.size = n
    def add_node(self, u, v):
        self.adj[u].append(v)

    def dfs(self, root, node, visited, M):
        for neighbor in self.adj[node]:
            if neighbor not in visited:
                M[root][neighbor] = 1
                visited.add(neighbor)
                self.dfs(root, neighbor, visited, M)
        

    def connectivity(self):
        M = [[0 for _ in range(self.size)] for _ in range(self.size)] 
        for node in range(self.size):
            visited = set()
            self.dfs(node, node, visited, M)
        return M
    
# --- Test 1: Simple chain (transitive reach) ---
# 0 → 1 → 2
# Expect: 0 can reach 1 AND 2
g1 = Graph(3)
g1.add_node(0, 1)
g1.add_node(1, 2)
print(g1.connectivity())
# Expected:
# [[0, 1, 1],
#  [0, 0, 1],
#  [0, 0, 0]]

# --- Test 2: Cycle ---
# 0 → 1 → 2 → 0
# Everyone can reach everyone
g2 = Graph(3)
g2.add_node(0, 1)
g2.add_node(1, 2)
g2.add_node(2, 0)
print(g2.connectivity())
# Expected:
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]

# --- Test 3: No edges ---
g3 = Graph(3)
print(g3.connectivity())
# Expected:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]