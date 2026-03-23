import collections
class Graph:
    def __init__(self):
        self.adj = collections.defaultdict(list)

    def add_node(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
       

    def bfs(self, root, color):
        q = collections.deque()
        q.append(root)
        color[root] = 0

        while q:
            node = q.popleft()
            for i in self.adj[node]:
                if i not in color:
                    color[i] = 1 - color[node]
                    q.append(i)
                elif color[node] == color[i]:
                    return False
        return True
    
    def check_bipartite(self):
        color = {}
        for i in self.adj:
            if i not in color:
                if not self.bfs(i, color):
                    return False
        return True
# --- Test 1: Simple bipartite graph (single edge) ---
g1 = Graph()
g1.add_node(0, 1)
print(g1.check_bipartite())  # Expected: True

# --- Test 2: Even cycle (bipartite) ---
# 0-1-2-3-0 (square)
g2 = Graph()
g2.add_node(0, 1)
g2.add_node(1, 2)
g2.add_node(2, 3)
g2.add_node(3, 0)
print(g2.check_bipartite())  # Expected: True

# --- Test 3: Odd cycle (NOT bipartite) ---
# 0-1-2-0 (triangle)
g3 = Graph()
g3.add_node(0, 1)
g3.add_node(1, 2)
g3.add_node(2, 0)
print(g3.check_bipartite())  # Expected: False

# --- Test 4: Disconnected, both components bipartite ---
# Component 1: 0-1, Component 2: 2-3
g4 = Graph()
g4.add_node(0, 1)
g4.add_node(2, 3)
print(g4.check_bipartite())  # Expected: True

# --- Test 5: Single node (trivially bipartite) ---
g5 = Graph()
g5.add_node(0, 0)  # self-loop — debatable, usually NOT bipartite
print(g5.check_bipartite())  # Expected: False

# --- Test 6: Complete bipartite K(2,2) ---
g6 = Graph()
g6.add_node(0, 2)
g6.add_node(0, 3)
g6.add_node(1, 2)
g6.add_node(1, 3)
print(g6.check_bipartite())  # Expected: True

# --- Test 7: K4 complete graph (NOT bipartite) ---
g7 = Graph()
for u in range(4):
    for v in range(u + 1, 4):
        g7.add_node(u, v)
print(g7.check_bipartite())  # Expected: False
    



