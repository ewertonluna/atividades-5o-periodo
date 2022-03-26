from vortex import Vortex
from edge import Edge
class Graph:
	def __init__(self, is_directed=False):
		self.is_directed = is_directed
		self.vertices = set()
		self.edges = set()
	
	def add_vortex(self, vortex):
		if not isinstance(vortex, Vortex):
			raise ValueError("'vortex' value must be an instance of Vortex")
		self.vertices.add(vortex)
	
	def add_edge(self, edge):
		if not isinstance(edge, Edge):
			raise ValueError("'edge' value must be an instance of Edge")
		self.edges.add(edge)
	
	def get_vortex_by_label(self, label):
		for vortex in self.vertices:
			if vortex.label == label:
				return vortex
		return None
	
	# Checa se a aresta conecta dois vértices existentes do grafo
	def is_edge_valid(self, edge):
		vortex_1_found = False
		vortex_2_found = False
		vortex_1, vortex_2 = edge.connected_vertices
		
		for vortex in self.vertices:
			if vortex_1_found and vortex_2_found:
				break
			if vortex.label == vortex_1.label:
				vortex_1_found = True
			elif vortex.label == vortex_2.label:
				vortex_2_found = True

		return vortex_1_found and vortex_2_found