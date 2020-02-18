
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex_id in self.vertices:
            print('WARNING: That vertex already exists')
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    '''
    Finds the earliest ancestor to the starting_node
    '''
    # instantiate the graph
    g = Graph()
    for num in ancestors:
        g.add_vertex(num[0])
        g.add_vertex(num[1])
        g.add_edge(num[1], num[0])
    # set a variable to record the longest length (earliest ancestor)
    longest = []
    # because we should use depth first search, create an empty stack
    s = Stack()
    # Add A PATH TO the starting node_id to the stack
    s.push([starting_node])
    # while the stack is not empty
    while s.size() > 0:
        # pop the first path
        path = s.pop()
        # grab the last node from the path
        last = path[-1]
        # check to see if path is the longest
        if len(path) > len(longest):
            longest = path
        # check if the lengths of the paths are equal
        if len(path) == len(longest):
            # check if the last index is smaller
            if last < longest[-1]:
                longest = path
        # Then add A PATH TO all parents to the top of the stack
        for neighbor in g.vertices[last]:
            # (Make a copy of the path before adding)
            last_copy = path.copy()
            last_copy.append(neighbor)
            s.push(last_copy)
    # establish base case, if not base case, return earliest ancestor
    if longest[-1] == starting_node:
        return -1
    else:
        return longest[-1]
