# Function to perform topological sort using Kahn's algorithm with a min-heap
def topological_sort(graph, vertices):
    # Initialize in-degrees of all vertices to 0
    in_degree = {}
    for v in vertices:
        in_degree[v] = 0

    # Calculate in-degrees of all vertices
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Create a min-heap and add all vertices with in-degree 0
    min_heap = MinHeap()
    for v in vertices:
        if in_degree[v] == 0:
            min_heap.insert(v)

    store = []
    while not min_heap.is_empty():
        v = min_heap.extract_min()
        store.append(v)

        # Decrease in-degree of all neighbors of v
        for neighbor in graph[v]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                min_heap.insert(neighbor)

    # Check if there was a cycle (i.e., topological sorting is not possible)
    if len(store) != len(vertices):
        raise ValueError("Graph has at least one cycle, topological sort not possible")

    return store


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Extract from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


# Function to take graph input from user
def input_graph():
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    graph = {}
    vertices = set()

    print("Enter the edges in the format 'u v' where u -> v:")
    for _ in range(num_edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        vertices.add(u)
        vertices.add(v)

    # Ensure all vertices are in the graph, even if they have no outgoing edges
    for vertex in vertices:
        if vertex not in graph:
            graph[vertex] = []

    return graph, vertices


# Example usage
if __name__ == "__main__":
    graph, vertices = input_graph()

    try:
        result = topological_sort(graph, vertices)
        print("Topological Sort of the given graph:")
        print(result)
    except ValueError as e:
        print(e)
