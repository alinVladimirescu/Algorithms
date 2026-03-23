class Graph:
    def __init__(self, n):
        self.neighbors = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        
    def root(self, node):
        while self.neighbors[node] != node:
            self.neighbors[node] = self.neighbors[self.neighbors[node]]
            node = self.neighbors[node]
        return node 

    def find(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            self.neighbors[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.neighbors[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True
    def check_cycle(self, edges):
        for u, v in edges:
            if not self.union(u, v):
                return False
        return True
# --- Test 1: No cycle (simple tree) ---
# 0-1, 1-2, 2-3 (a line)
g1 = Graph(4)
print(g1.check_cycle([(0,1), (1,2), (2,3)]))  # Expected: True (no cycle)

# --- Test 2: Has a cycle (triangle) ---
# 0-1, 1-2, 2-0
g2 = Graph(3)
print(g2.check_cycle([(0,1), (1,2), (2,0)]))  # Expected: False (cycle found)

# --- Test 3: Single edge ---
g3 = Graph(2)
print(g3.check_cycle([(0,1)]))  # Expected: True

# --- Test 4: No edges at all ---
g4 = Graph(5)
print(g4.check_cycle([]))  # Expected: True

# --- Test 5: Cycle appears late ---
# 0-1, 2-3, 1-2, 3-0
g5 = Graph(4)
print(g5.check_cycle([(0,1), (2,3), (1,2), (3,0)]))  # Expected: False

# --- Test 6: Duplicate edge (instant cycle) ---
g6 = Graph(3)
print(g6.check_cycle([(0,1), (0,1)]))  # Expected: False

# --- Test 7: Larger tree, no cycle ---
#     0
#    / \
#   1   2
#  / \
# 3   4
g7 = Graph(5)
print(g7.check_cycle([(0,1), (0,2), (1,3), (1,4)]))  # Expected: True

# --- Test 8: Two disconnected components, cycle in one ---
# Component 1: 0-1-2-0 (triangle)
# Component 2: 3-4 (edge)
g8 = Graph(5)
print(g8.check_cycle([(0,1), (1,2), (3,4), (2,0)]))  # Expected: False

# --- Test 9: Self-loop ---
g9 = Graph(3)
print(g9.check_cycle([(0,0)]))  # Expected: False (but will return True
                                 # because root(0)==root(0), union returns
                                 # False before size check — actually works!)

# --- Test 10: find() method directly (after fixing the bug) ---
g10 = Graph(4)
g10.union(0, 1)
g10.union(2, 3)
print(g10.find(0, 1))  # Expected: True  (same component)
print(g10.find(0, 2))  # Expected: False (different components)
g10.union(1, 2)
print(g10.find(0, 3))  # Expected: True  (now all connected)