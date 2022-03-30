from typing import Set, Tuple
from typing import Union
from edge_exception import EdgeException

class Edge:

	def __init__(self, label, is_directed=False) :
		self.label = label
		self.weight = 0
		self.is_directed = is_directed
		self.connected_vertices = tuple() if is_directed else set() 

	def set_connected_vertices(self, vertices: Union[Tuple[str, str], Set[str]]):
		"""
		Adds pair of vertices to the edge instance.

		Parameters:
		vertices (str, str) | {str, str}: Pair of labels for each vortex connected to the edge instance.
	
		Returns:
		None
	
		"""

		vertices_validation_message = self.get_vertices_validation_message(vertices)
		if vertices_validation_message:
			raise EdgeException(vertices_validation_message)

		if self.is_directed:
			vertices = tuple(vertices)
		else:
			vertices = set(vertices)
		self.connected_vertices = vertices	

	
	def get_vertices_validation_message(self, vertices: Union[Tuple[str, str], Set[str]]):
		"""
		Checks if pair of vertices is a valid input and returns a message from it.

		The input is valid if it is a tuple or a set of 2 string and 
		if their label is different from one another.
	
		Parameters:
		vertices (str, str) | {str, str}: Pair of labels for each vortex connected to the edge instance.
	
		Returns:
		str: An empty string if input is valid. Otherwise, a message containing information about the validation.
	
		"""

		result = ""
		
		if len(vertices) != 2:
			result = "Length of 'vertices' has to be exactly 2."
		elif isinstance(vertices, set):
			# TODO: Continuar escrevendo o método
			pass
		else:
			label_1, label_2 = vertices
			
			if label_1 == label_2:
				result = "The vertices' labels cannot be the same"

		return result
	
	def set_weight(self, weight: float):
		if weight is None:
			raise EdgeException("Must provide a value for 'weight'.")
		if weight < 0:
			raise EdgeException("'weight' value has to be bigger than or equals to zero")
		self.weight = float(weight)

	def __repr__(self):
		return f'Edge[label: "{self.label}", weight: "{self.weight}", is_directed: "{self.is_directed}", connected_vertices: "{self.connected_vertices}]"'




# Testing
# edge = Edge('a', True)
# edge.add_connected_vertices_pair(('a', 'a'))
# print(edge.connected_vertices)