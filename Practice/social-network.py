class Exercise2:
    parents = []
    size = []
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    def root(self, node):
        while self.parents[node] != node:
            node = self.parents[node]
        return node
    def find(self, u, v):
        return self.root(u) == self.root(v)
    def union(self, u, v):
        u_r = self.root(u)
        u_v = self.root(v)
        if u_r == u_v:
            return
        if self.size[u_r] < self.size[u_v]:
            self.parents[u_r] = u_v
            self.size[u_v] += self.size[u_r]
        else:
            self.parents[u_v] = u_r
            self.size[u_r] += self.size[u_v]
    
    def check_all(self, n):
        if n < 0:
            return False
        first = self.root(0)
        for i in range(1, n):
            if self.root(i) != first:
                return False
        return True
    
if __name__ == "__main__":
    uf = Exercise2(5)
    uf.union(0, 1)
    uf.union(0, 2)
    uf.union(0 , 3)
    uf.union(1, 4)
    print(uf.check_all(5))

        