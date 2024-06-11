class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

def kruskal(graph, num_vertices):
    mst = []
    total_cost = 0
    ds = DisjointSet(num_vertices)
    min_heap = MinHeap()

    for u, v, weight in graph:
        min_heap.insert((weight, u, v))

    while len(mst) < num_vertices - 1 and len(min_heap.heap) > 0:
        weight, u, v = min_heap.extract_min()
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# Taking input manually
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))
edges = []

print("Enter the edges in the format 'u v weight':")
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))

mst, total_cost = kruskal(edges, num_vertices)


print(f"Minimum cost of the Minimum Spanning Tree: {total_cost}")
