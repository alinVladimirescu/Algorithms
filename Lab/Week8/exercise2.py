import collections
class Graph:
    def __init__(self):
        self.adj = collections.defaultdict(list)
        self.nodes = set()
        self.directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) 
    def add_node(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.nodes.add(v)
        self.nodes.add(u)
    
    def check_euler_cycle(self):
        if not self.nodes:
            return -1
        
        for node in self.nodes:
            if len(self.adj[node]) % 2 != 0:
                return False
        start = next(iter(self.nodes))
        visited = set()
        q = collections.deque([start])
        while q:
            current_node = q.popleft()
            if current_node not in visited:
                visited.add(current_node)
            for nei_node in self.adj[current_node]:
                if nei_node not in visited:
                    visited.add(nei_node)
                    q.append(nei_node)
        return visited == self.nodes
    
    # Test 1: Empty graph → -1
g = Graph()
print(g.check_euler_cycle() == -1)

# Test 2: Simple triangle (0-1-2-0) — all degrees 2, connected → True
g = Graph()
g.add_node(0, 1); g.add_node(1, 2); g.add_node(2, 0)
print(g.check_euler_cycle() == True)

# Test 3: Square cycle (0-1-2-3-0) — all degrees 2, connected → True
g = Graph()
g.add_node(0, 1); g.add_node(1, 2); g.add_node(2, 3); g.add_node(3, 0)
print(g.check_euler_cycle() == True)

# Test 4: Path 0-1-2 — nodes 0 and 2 have odd degree (1) → False
g = Graph()
g.add_node(0, 1); g.add_node(1, 2)
print(g.check_euler_cycle() == False)

# Test 5: Single edge 0-1 — both nodes degree 1 (odd) → False
g = Graph()
g.add_node(0, 1)
print(g.check_euler_cycle() == False)

# Test 6: Two disconnected triangles — all even degrees but not connected → False
g = Graph()
g.add_node(0, 1); g.add_node(1, 2); g.add_node(2, 0)  # triangle 1
g.add_node(3, 4); g.add_node(4, 5); g.add_node(5, 3)  # triangle 2
print(g.check_euler_cycle() == False)

# Test 7: Complete graph K4 — all nodes degree 3 (odd) → False
g = Graph()
for i in range(4):
    for j in range(i+1, 4):
        g.add_node(i, j)
print(g.check_euler_cycle() == False)

# Test 8: "Bowtie" (two triangles sharing a vertex) — shared vertex has degree 4,
#          others degree 2 — all even, connected → True
g = Graph()
g.add_node(0, 1); g.add_node(1, 2); g.add_node(2, 0)  # triangle around 0
g.add_node(0, 3); g.add_node(3, 4); g.add_node(4, 0)  # triangle around 0
print(g.check_euler_cycle() == True)

# Test 9: Star graph (center node connects to 3 leaves) — center degree 3 (odd) → False
g = Graph()
g.add_node(0, 1); g.add_node(0, 2); g.add_node(0, 3)
print(g.check_euler_cycle() == False)
