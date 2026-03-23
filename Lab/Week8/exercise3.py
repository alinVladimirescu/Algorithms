import collections

class Graph:
    def __init__(self):
        self.adj = collections.defaultdict(list)
        self.nodes = set()

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def check_hamiltonian_path(self):
        stack = []
        visited = set()

        def dfs(node):
            visited.add(node)
            for nei_node in self.adj[node]:
                if nei_node not in visited:
                    dfs(nei_node)
            stack.append(node)

        for node in self.nodes:
            if node not in visited:
                dfs(node)

        stack = stack[::-1]
        for i  in range(len(stack) - 1):
            if stack[i + 1] not in self.adj[stack[i]]:
                return False
        return True
def main():
    tests = [
        {
            "name": "Simple chain A → B → C",
            "edges": [("A", "B"), ("B", "C")],
            "extra_nodes": [],
            "expected": True,
        },
        {
            "name": "Fork with no connecting edge",
            "edges": [("A", "B"), ("A", "C")],
            "extra_nodes": [],
            "expected": False,
        },
        {
            "name": "Diamond (no Hamiltonian path)",
            "edges": [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")],
            "extra_nodes": [],
            "expected": False,
        },
        {
            "name": "Diamond with shortcut A → B → C → D",
            "edges": [("A", "B"), ("B", "C"), ("C", "D"), ("A", "C"), ("B", "D")],
            "extra_nodes": [],
            "expected": True,
        },
        {
            "name": "Single node",
            "edges": [],
            "extra_nodes": ["A"],
            "expected": True,
        },
        {
            "name": "Disconnected node (no Hamiltonian path)",
            "edges": [("A", "B")],
            "extra_nodes": ["C"],
            "expected": False,
        },
        {
            "name": "Longer chain A → B → C → D → E",
            "edges": [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")],
            "extra_nodes": [],
            "expected": True,
        },
        {
            "name": "Multiple paths converging (A → B → C → D)",
            "edges": [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")],
            "extra_nodes": [],
            "expected": True,
        },
    ]

    passed = 0
    failed = 0

    for test in tests:
        g = Graph()
        for u, v in test["edges"]:
            g.add_edge(u, v)
        for node in test["extra_nodes"]:
            g.nodes.add(node)

        result = g.check_hamiltonian_path()
        status = "PASS" if result == test["expected"] else "FAIL"

        if status == "PASS":
            passed += 1
        else:
            failed += 1

        print(f"  [{status}] {test['name']}")
        if status == "FAIL":
            print(f"         Expected {test['expected']}, got {result}")

    print(f"\n{passed}/{passed + failed} tests passed")


if __name__ == "__main__":
    main()            