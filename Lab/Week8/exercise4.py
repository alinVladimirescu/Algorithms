import collections
class Graph:

    def __init__(self):
        self.adj = collections.defaultdict(list)
        self.nodes = set()

    def add_edge(self, u , v):
        self.adj[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def find_shortest_cycle(self):
        min_cycle_length = float("inf")
        def bfs(start, min_cycle_length):
            q = collections.deque()
            q.append((start, 0))
            visited = set()
            level = 0

            while q:
                for i in range(len(q)):
                    current_node, l = q.popleft()
                    if current_node in visited:
                        min_cycle_length = min(min_cycle_length, l + 1)
                        continue
                    else:
                        visited.add(current_node)

                    for nei_node in self.adj[current_node]:
                        q.append((nei_node, level))
                level += 1
            return min_cycle_length
        for node in self.nodes:
            min_cycle_length = min(min_cycle_length, bfs(node, min_cycle_length))
        return min_cycle_length if min_cycle_length != float("inf") else -1
# Test 1: Empty graph → -1
g = Graph()
assert g.find_shortest_cycle() == -1

# Test 2: Simple triangle 0→1→2→0 — cycle length 3
g = Graph()
g.add_edge(0, 1); g.add_edge(1, 2); g.add_edge(2, 0)
assert g.find_shortest_cycle() == 3

# Test 3: Path 0→1→2 — no cycle → -1
g = Graph()
g.add_edge(0, 1); g.add_edge(1, 2)
assert g.find_shortest_cycle() == -1

# Test 4: Two-node cycle 0→1→0 — cycle length 2
g = Graph()
g.add_edge(0, 1); g.add_edge(1, 0)
assert g.find_shortest_cycle() == 2

# Test 5: Two cycles, should return shortest
# 0→1→0 (length 2) and 0→2→3→0 (length 3) → 2
g = Graph()
g.add_edge(0, 1); g.add_edge(1, 0)
g.add_edge(0, 2); g.add_edge(2, 3); g.add_edge(3, 0)
assert g.find_shortest_cycle() == 2

# Test 6: Square cycle 0→1→2→3→0 — cycle length 4
g = Graph()
g.add_edge(0, 1); g.add_edge(1, 2); g.add_edge(2, 3); g.add_edge(3, 0)
assert g.find_shortest_cycle() == 4

# Test 7: Single node, no edges → -1
g = Graph()
g.nodes.add(0)
assert g.find_shortest_cycle() == -1

print("All tests passed")