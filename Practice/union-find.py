
class Exercise1:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def root(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]  # Path compression
            node = self.parents[node]
        return node

    def find(self, u, v):
        return self.root(u) == self.root(v)

    def union(self, u, v):
        u_root = self.root(u)
        v_root = self.root(v)
        if u_root == v_root:
            return
        if self.size[u_root] < self.size[v_root]:
            self.parents[u_root] = v_root
            self.size[v_root] += self.size[u_root]
        else:
            self.parents[v_root] = u_root
            self.size[u_root] += self.size[v_root]


if __name__ == "__main__":
    uf = Exercise1(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print("Find(0, 2):", uf.find(0, 2))  
    print("Find(0, 3):", uf.find(0, 3))  
        
