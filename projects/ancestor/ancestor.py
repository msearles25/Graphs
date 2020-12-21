from util import Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices= {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for vertex in ancestors:
        if vertex[0] not in g.vertices:
            g.add_vertex(vertex[0])
        if vertex[1] not in g.vertices:
            g.add_vertex(vertex[1])
    
    for vertex in ancestors:
        g.add_edge(vertex[1], vertex[0])

    if g.get_neighbors(starting_node) == set():
        return -1

    q = Queue()
    q.enqueue([starting_node])
    oldest = []
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if len(path) > len(oldest):
            oldest = path
        if len(path) == len(oldest) and path[-1] < oldest[-1]:
            oldest = path
        for neighbor in g.get_neighbors(v):
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)
    return oldest[-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 2)    