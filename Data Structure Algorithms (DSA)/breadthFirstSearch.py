# Breadth First Search - Credit: https://www.youtube.com/watch?v=-uR7BSfNJko&t=42s

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.distance = 9999
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
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
			print "Vertex '" + key + "' with neighbors " + str(self.vertices[key].neighbors) + "  at distance (" + str(self.vertices[key].distance) + ") to vertex A"
		
	def bfs(self, vert):
		res = list() # empty queue to 
		vert.distance = 0 # set to 0 as distance of a vertex to itself is 0
		vert.color = 'red'
		for v in vert.neighbors:
			self.vertices[v].distance = vert.distance + 1 # iterating through vertices moving a distance of 1
			res.append(v)
		
		while len(res) > 0: # as long as there are still items on the queue
			u = res.pop(0) # u is vertex name
			node_u = self.vertices[u] # vertex object of the vertex name
			node_u.color = 'red'
			
			for v in node_u.neighbors:
				node_v = self.vertices[v] # save vertex object of each neighbor
				if node_v.color == 'black':
					res.append(v) # vertex yet to be visited is appended
					if node_v.distance > node_u.distance + 1:
						node_v.distance = node_u.distance + 1
					
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = [ 'AC', 'AG', 'BE', 'CG', 'CF', 'DH', 'EJ', 'FJ', 'GC', 'HF', 'ID', 'JC' ]
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	
g.bfs(a) # call BFS function

g.print_graph()