import collections
class Graph:
    def __init__(self):
        self.adj = collections.defaultdict(list)
        self.nodes = set()
    def add_node(self, u, v):
        self.nodes.add(u)
        self.nodes.add(v)
        self.adj[u].append(v)
        self.adj[v].append(u)
       
    def find_distance(self, node_a, node_b):
        if node_a is None or node_b is None:
            return -1
        q = collections.deque()
        q.append(node_a)
        visited = set()
        visited.add(node_a)
        distance = 0
        while q:
            for i in range(len(q)):
                current_node = q.popleft()
                if current_node == node_b:
                    return distance
                for node in self.adj[current_node]:
                    if node not in visited:
                        visited.add(node)
                        q.append(node)
            distance += 1
        return -1
    def find_eccentricity(self, node):
        max_distance = 0
        for current_node in self.nodes:
            if current_node != node:
                max_distance = max(max_distance, self.find_distance(node, current_node))
        return max_distance
    def find_radius(self):
        radius = len(self.nodes)
        for node in self.nodes:
            radius = min(radius, self.find_eccentricity(node))
        return radius
    def find_diameter(self):
        diameter = 0
        for node in self.nodes:
            diameter = max(diameter, self.find_eccentricity(node))
        return diameter
    def find_center(self):
        center = []
        radius = self.find_radius()
        for node in self.nodes:
            ecc = self.find_eccentricity(node)
            if ecc == radius:
                center.append(node)
        return node
g = Graph()
g.add_node(0, 1)
g.add_node(0, 2)
g.add_node(2, 3)
g.add_node(3, 4)
print(g.find_eccentricity(2))
print(g.find_center())
print(g.find_radius())
print(g.find_diameter())
