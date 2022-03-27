from typing import Dict, Set, Tuple, Union
from edge_exception import EdgeException
from vortex import Vortex
from edge import Edge
from graph_exception import GraphException

class Graph:
	def __init__(self, is_directed=False):
		self.is_directed = is_directed
		self.vertices: Dict[str, Vortex] = dict()
		self.edges: Dict[str, Edge] = dict()
	
	def add_vortex(self, vortex_label: str):
		"""
		Adds vortex to the Graph

		Parameters:
		vortex_label (str): Label of the vortex
	
		Returns:
		None
	
		"""

		vortex = Vortex(vortex_label)
		self.vertices[vortex.label] = vortex
	
	def add_edge(self, edge_label: str, connected_vertices: Union[Tuple[str, str], Set[str]]):
		"""
		Adds edge to the Graph

		Parameters:
		edge_label (str): Label of the edge
		connected_verties (tuple[str, str] | set(str)): A tuple (for directed graphs) or a set (for non-directed graphs)
			that represents the pair of vertices the edge connects.
	
		Returns:
		None
	
		"""

		for vertice_label in connected_vertices:
			if not self.has_vertice(vertice_label):
				raise GraphException(f"The edge is connected to a vertice that doesn't exist: (vertice label: '{vertice_label}')")

		edge = Edge(edge_label, self.is_directed)
		try:
			edge.add_connected_vertices_pair(connected_vertices)
		except EdgeException as e:
			raise GraphException('Error adding edge: ' + str(e))

		for vertice_label in connected_vertices:
			vortex = self.vertices[vertice_label]	
			vortex.add_adjacent_edge(edge)

		self.edges[edge.label] = edge
	
	def has_vertice(self, vortex_label: str) -> bool:
		"""
		Checks if the graph has a certain vertice

		Parameters:
		vortex_label (str): Label of the vortex
	
		Returns:
		bool: True if the vortex exists in the graph, False otherwise.
	
		"""
		return vortex_label in self.vertices.keys()
	
	def __repr__(self) -> str:
		repr = "Graph[\n" \
			f"\tvertices: \n"

		for vortex in self.vertices.values():
			repr += f"\t\t{vortex}\n"

		repr += "\tedges:\n"

		for edge in self.edges.values():
			repr += f"\t\t{edge}\n"

		repr += "]"
		return repr



# Testing
graph = Graph()
graph.add_vortex('a')
graph.add_vortex('b')
graph.add_edge('1', ('a', 'b'))
graph.add_vortex('c')
graph.add_edge('2', ('b', 'c'))
print(graph)