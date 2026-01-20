# Exercise 3 – Extended Union-Find 
# Extend Union-Find with a method find so that find(i) returns the largest element in the connected component containing i. For example, if one of the connected components is {1,2,6,9}, then the find method should return 9 for each of the four elements in the connected components.  The operations union(),  connected(), and find() should all take logarithmic time or better.

class Exercise3:
    parents = []
    size = []
    greatest = []
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.greatest = [i for i in range(n)]

    def root(self, node):
        while self.parents[node] != node:
            node = self.parents[node]
        return node
    def connected(self, u):
       return self.greatest[self.root(u)]
    def union(self, u, v):
        rootU = self.root(u)
        rootV = self.root(v)
        if rootU != rootV:
            if self.size[rootU] < self.size[rootV]:
                self.parents[rootU] = rootV
                self.size[rootV] += self.size[rootU]
                self.greatest[rootV] = max(self.greatest[rootV], self.greatest[rootU])
            else:
                self.parents[rootV] = rootU
                self.size[rootU] += self.size[rootV]
                self.greatest[rootU] = max(self.greatest[rootU], self.greatest[rootV])
if __name__ == "__main__":
    uf = Exercise3(10)
    uf.union(1, 2)
    uf.union(2, 6)
    uf.union(9, 1)
    uf.union(2, 9)
    
    print(uf.connected(1))  
    print(uf.connected(4))  
    print(uf.connected(2))  
    