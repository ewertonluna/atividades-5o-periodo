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
	
	def add_vortex(self, label: str):
		"""
		Adds vortex to the Graph

		Parameters:
		vortex_label (str): Label of the vortex
	
		Returns:
		None
	
		"""

		vortex = Vortex(label)
		self.vertices[vortex.label] = vortex
	
	def add_edge(self, label: str, connected_vertices: Union[Tuple[str, str], Set[str]], weight: float=0):
		"""
		Adds edge to the Graph

		Parameters:
		edge_label (str): Label of the edge
		connected_verties (tuple[str, str] | set(str)): A tuple (for directed graphs) or a set (for non-directed graphs)
			that represents the pair of vertices the edge connects.
	
		Returns:
		None
	
		"""

		non_existent_vertices = list()
		for vertice_label in connected_vertices:
			if not self.has_vertice(vertice_label):
				non_existent_vertices.append(vertice_label)

		if non_existent_vertices:
			raise GraphException(f"The edge is connected to one or more vertices that don't exist: (label(s): {non_existent_vertices})")

		edge = Edge(label, self.is_directed)
		try:
			edge.set_connected_vertices(connected_vertices)
			edge.set_weight(float(weight))
		except (EdgeException, ValueError) as e:
			raise GraphException('Error adding edge: ' + str(e))
		except Exception as e:
			raise GraphException('General exception:' + str(e))

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
			f"\tis_directed: {self.is_directed}\n" \
			f"\tvertices: \n"

		for vortex in self.vertices.values():
			repr += f"\t\t{vortex}\n"

		repr += "\tedges:\n"

		for edge in self.edges.values():
			repr += f"\t\t{edge}\n"

		repr += "]"
		return repr
	
	def dijkstra(self, starting_label, destination_label):
		# (label_vertice, distancia, de_onde_veio, se_ta_aberto)
		# Obs: ver se tem como ordenar vertices_list pelo valor do custo da tuple
		vertices_list = list()
		for label in self.vertices.keys():
			if label == starting_label:
				vertices_list.append([label, 0, label, True])  # [('a', 0, 'a', True), ('b', -1, None, True)]
			else:
				vertices_list.append([label, -1, None, True])

		# Escolher o vértice de menor custo	
		min_distance = 0
		chosen_label = None
		for vertice_tuple in vertices_list:
			if (vertice_tuple[1] != -1) and (vertice_tuple[1] <= min_distance):
				chosen_label = vertice_tuple[0]
				vertice_tuple[3] = False

		# **  Relaxar as arestas **
		# Percorrer todas as arestas adjcentes ao vértice escolhido
		for adjacent_edge in self.vertices[chosen_label].adjacent_edges:
			connected_vortex_1, connected_vortex_2 = adjacent_edge.connected_vertices # ('a', 'b') 
			label = connected_vortex_1 if (connected_vortex_1 != chosen_label) else connected_vortex_2
			edge_weight = adjacent_edge.weight
			current_tuple = None

			for vertice_tuple in vertices_list:
				if vertice_tuple[1] == label:
					current_tuple = vertice_tuple

			if current_tuple[2] == -1:
				current_tuple[2] = edge_weight


# Testing
graph = Graph()
graph.add_vortex('a')
graph.add_vortex('b')
graph.add_edge('1', {'a', 'b'}, 10)
graph.dijkstra('a', 'b')
# graph.add_vortex('c')
# graph.add_edge('2', ('b', 'c'))
# print(graph)