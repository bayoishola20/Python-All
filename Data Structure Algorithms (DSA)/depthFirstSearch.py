# Depth First Search - Credit: https://www.youtube.com/watch?v=QVcsSaGeSH0

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.discovery = 0
        self.end = 0

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {} # dictionary to store vertices in the graph

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted( list( self.vertices.keys() ) ):
            print "node '" + key + "' has neighbors " + str(self.vertices[key].neighbors)

g = Graph()
# print str( len(g.vertices) )

a = Vertex('A')
g.add_vertex(a)
g.add_vertex( Vertex('B') )

for i in range( ord('A'), ord('K') ):
    g.add_vertex( Vertex( chr(i) ) )

edges = [ 'AC', 'AG', 'BE', 'CG', 'CF', 'DH', 'EJ', 'FJ', 'GC', 'HF', 'ID', 'JC' ]

for edge in edges:
    g.add_edge( edge[:1], edge[1:] )


g.print_graph()