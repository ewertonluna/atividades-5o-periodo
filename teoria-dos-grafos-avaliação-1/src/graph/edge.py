
class Edge:

	def __init__(self, label, is_directed=False, connected_vertices = dict()):
		self.label = label
		self.is_directed = is_directed
		self.connected_vertices = connected_vertices
