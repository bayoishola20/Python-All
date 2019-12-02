# Depth First Search - Credit: https://www.youtube.com/watch?v=QVcsSaGeSH0

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.discovery = 0
		self.end = 0
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	time = 0
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex # letter name of vertex as key and vertex itself as value
			return True
		else:
			return False
	
	def add_edge(self, x, y):
		if x in self.vertices and y in self.vertices:
			for key, value in self.vertices.items():
				if key == x:
					value.add_neighbor(y)
				if key == y:
					value.add_neighbor(x)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print "Vertex '" + key + "' with neighbors " + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].end)

	def _dfs(self, vertex):
		global time
		vertex.color = 'red'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs( self.vertices[v] )
		vertex.color = 'blue'
		vertex.end = time
		time += 1
		
	def dfs(self, vertex):
		global time
		time = 1
		self._dfs(vertex)
			
g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')

g.add_vertex(a)
g.add_vertex( Vertex('B') )

for i in range( ord('A'), ord('K') ):
	g.add_vertex( Vertex( chr(i) ) )

edges = [ 'AC', 'AG', 'BE', 'CG', 'CF', 'DH', 'EJ', 'FJ', 'GC', 'HF', 'ID', 'JC' ]

for edge in edges:
	g.add_edge( edge[:1], edge[1:] )
	
g.dfs(a)
g.print_graph()