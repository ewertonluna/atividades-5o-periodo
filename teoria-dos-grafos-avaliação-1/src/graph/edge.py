class Edge:

	def __init__(self, label, is_directed=False) :
		self.label = label
		self.is_directed = is_directed
		self.connected_vertices = tuple() if is_directed else set()

	def add_pair_of_vertices(self, vertices):
		if len(vertices) != 2:
			raise ValueError('There must be exactly 2 vertices being connected by this edge')
		if self.is_directed:
			vertices = tuple(vertices)
		else:
			vertices = set(vertices)

		self.connected_vertices.add(vertices)
	
	def are_vertices_valid(self, vertices):
		if len(vertices) != 2:
			raise ValueError('There must be exactly 2 vertices being connected by this edge')
		# TODO: Realizar check para ver se o par de vértice possui a mesma label	

