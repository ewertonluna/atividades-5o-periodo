from edge import Edge
class Vortex:
	def __init__(self, label):
		self.label = label
		self.adjacent_edges = set() # Esse atributo recebe um conjunto de arestas
	
	def add_adjacent_edge(self, edge):
		if isinstance(edge, Edge):
			raise ValueError("'edge' must be an instance of Edge")
		self.adjacent_edges.add(edge)
