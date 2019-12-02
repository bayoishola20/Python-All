# Depth First Search - Credit: https://www.youtube.com/watch?v=QVcsSaGeSH0

class Node:
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
    nodes = {} # dictionary to store nodes in the graph

    def add_node(self, node):
        if isinstance(node, Node) and node.name not in self.nodes:
            self.nodes[node.name] = node
            return True
        else:
            return False
    
    def add_edge(self, x, y):
        if x in self.nodes and y in self.nodes:
            for key, value in self.nodes.items():
                if key == x:
                    value.add_neighbor(y)
                if key == y:
                    value.add_neighbor(x)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted( list( self.nodes.keys() ) ):
            print "node '" + key + "' has neighbors " + str(self.nodes[key].neighbors)

g = Graph()
# print str( len(g.vertices) )

g.add_node( Node('A') )

g.add_node( Node('B') )

for i in range( ord('A'), ord('K') ):
    g.add_node( Node( chr(i) ) )

edges = [ 'AC', 'AG', 'BE', 'CG', 'CF', 'DH', 'EJ', 'FJ', 'GC', 'HF', 'ID', 'JC' ]

for edge in edges:
    g.add_edge( edge[:1], edge[1:] )


g.print_graph()