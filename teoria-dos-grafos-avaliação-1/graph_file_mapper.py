from ctypes import Union
import os
import re
from typing import Any
from xmlrpc.client import boolean
from graph_file_mapper_exception import GraphFileMapperException


# TODO: Refatorar código para aceitar 5 linhas. A 4a linha é a de labels das arestas
class GraphFileMapper:

	def __init__(self, file_path: str):
		self.file_path = file_path
	

	def set_file_path(self, file_path: str):
		if (file_path is None) or (not isinstance(file_path, str)):
			raise GraphFileMapperException("'file_path' must be a string")
		self.file_path = file_path


	# Could use some refactoring :)
	def get_graph_values(self):
		validation_message = self._get_validation_message(self.file_path)
		if validation_message:
			raise GraphFileMapperException("Error getting graph values from file: " + validation_message)

		directed_edge_pattern = "\(\s*\w\s*,\s*\w\s*\)"
		undirected_edge_pattern = "\{\s*\w\s*,\s*\w\s*\}"
		file = open(self.file_path, 'r')
		lines = file.readlines()
		file.close()
		first_line = lines[0].strip()
		second_line = lines[1].strip()
		third_line = lines[2].strip()	
		fourth_line = lines[3].strip()
		is_directed = True if (first_line.lower() == 'direcionado') else False
		vertices_values = second_line.split(',')
		vertices_values = set(map(lambda vertice: vertice.strip(), vertices_values))
		vertices_values = set(filter(lambda vertice: vertice != '', vertices_values))
		pattern = directed_edge_pattern if first_line == 'direcionado' else undirected_edge_pattern
		edges = re.findall(pattern, third_line)
		edges = self._clean_edges_values(edges)
		weight_values = fourth_line.split(',')
		weight_values = list(map(lambda weight: weight.strip(), weight_values))
		weight_values = list(filter(lambda weight: weight != '', weight_values))
		weight_values = self._clean_weights_values(weight_values)
		return {'is_directed': is_directed, 'vertices_values': vertices_values, 'edges': edges, 'weight_values': weight_values}


	def _get_validation_message(self, file_path: str):
		try:
			file = open(self.file_path, 'r')
		except FileNotFoundError as fnfe:
			return "The file was not found. "
		except PermissionError as pe:
			return "The current user doesn't have permission to read the file. "
		if self._is_file_emtpy(file_path):
			return "The file is empty. "
		file.close()

		validation_message = ""
		if not self._has_minimum_number_of_lines(file_path):
			validation_message += "The file must have at least 4 lines to be valid."
		else:
			if not self._is_first_line_valid(file_path):
				validation_message += "First line of the file is not valid. "
			if not self._is_second_line_valid(file_path):
				validation_message += "Second line of the file is not valid. "
			if not self._is_third_line_valid(file_path):
				validation_message += "Third line of the file is not valid. "
			if not self._is_fourth_line_valid(file_path):
				validation_message += "Fourth line of the file is not valid. "
		validation_message = validation_message +  "Check the information about the file format requirements. " if validation_message else validation_message

		return validation_message


	def _is_file_emtpy(self, file_path: str):
		return True if not os.path.getsize(file_path) else False

	
	def _has_right_format(self, file_path: str):
		has_right_format = True
		file = open(file_path, 'r')
		if not self._has_minimum_number_of_lines(file_path):
			has_right_format = False
		
		file.close()

	
	def _has_minimum_number_of_lines(self, file_path: str):
		file = open(file_path, 'r')
		lines = file.readlines()
		file.close()
		return True if len(lines) >= 5 else False
		

	def _is_first_line_valid(self, file_path: str):
		file = open(file_path, 'r')
		lines = file.readlines()
		first_line = lines[0].strip()
		file.close()
		return True if (first_line == 'direcionado' or first_line == 'não direcionado') else False

	
	def _is_second_line_valid(self, file_path: str):
		file = open(file_path, 'r')
		lines = file.readlines()
		second_line = lines[1].strip()
		vertices_values = second_line.split(',')
		vertices_values = set(map(lambda vertice: vertice.strip(), vertices_values))
		vertices_values = set(filter(lambda vertice: vertice != '', vertices_values))
		file.close()
		return True if len(vertices_values) >= 1 else False
	

	# TODO: refatorar para ser fourth_line
	def _is_third_line_valid(self, file_path: str):
		file = open(file_path, 'r')
		lines = file.readlines()
		file.close()
		third_line = lines[2].strip()
		first_line = self._get_first_line_value(file_path)
		
		# If third line is empty (i.e. no edges were passed)
		if not third_line:
			return True

		directed_edge_pattern = "^(\(\s*(\w+)\s*,\s*(\w+)\s*\)\s*,?\s*)*$"
		undirected_edge_pattern = "^(\{\s*(\w+)\s*,\s*(\w+)\s*\}\s*,?\s*)*$"
		tuple_pattern = "\(\s*\w\s*,\s*\w\s*\)"
		set_pattern = "\{\s*\w\s*,\s*\w\s*\}"
		directed_edges = re.findall(tuple_pattern, third_line)
		undirected_edges = re.findall(set_pattern, third_line)

		# If first line is valid, the pattern will depend on its value
		if self._is_first_line_valid(file_path):
			if first_line == 'direcionado':
				pattern = directed_edge_pattern
			else: 
				pattern = undirected_edge_pattern
			return bool(re.match(pattern, third_line)) and len(self._get_edge_label_values()) == self._get_number_of_connected_vertices_pairs()
		# If first line is invalid, the pattern accepts either directed
		else:
			return (bool(re.match(directed_edge_pattern, third_line)) or bool(re.match(undirected_edge_pattern, third_line))) and (len(self._get_edge_label_values()) == self._get_number_of_connected_vertices_pairs())


	# TODO: refatorar para ser fifth_line
	def _is_fourth_line_valid(self, file_path: str):
		is_valid = True
		file = open(file_path, 'r')
		lines = file.readlines()
		fourth_line = lines[3].strip()
		weight_values = fourth_line.split(',')
		weight_values = list(map(lambda weight: weight.strip(), weight_values))
		weight_values = list(filter(lambda weight: weight != '', weight_values))

		if len(weight_values) != self._get_number_of_connected_vertices_pairs(file_path):
			is_valid = False
		for value in weight_values:
			if not self._can_be_converted_to_float(value):
				is_valid = False
				break
		return is_valid
	

	# TODO: refatorar parar ser third_line
	def _is_fifth_line_valid(self, file_path: str) -> bool:
		file = open(file_path, 'r')
		lines = file.readlines()
		file.close()
		fifth_line = lines[4].strip()
		return True if len(vertices_values) >= 1 else False

				

	def _get_first_line_value(self, file_path: str):
		file = open(file_path, 'r')
		lines = file.readlines()
		first_line = lines[0].strip()
		file.close()
		return first_line

	# TODO: refatorar para ser _get_fourth_line_value	
	def _get_third_line_value(self, file_path: str):
		file = open(file_path, 'r')
		lines = file.readlines()
		third_line = lines[2].strip()
		file.close()
		return third_line
	
	# Returns 0 if the third line is the not valid for the given graph or if the graph doesn't have edges.
	def _get_number_of_connected_vertices_pairs(self, file_path: str):
		third_line = self._get_third_line_value(file_path)  # TODO: refatorar referências de thid_line para fourth_line
		if not self._is_third_line_valid(file_path) or not third_line:
			num_of_edges = 0
		else:
			directed_edge_pattern = "\(\s*\w\s*,\s*\w\s*\)"
			undirected_edge_pattern = "\{\s*\w\s*,\s*\w\s*\}"
			directed_edges = re.findall(directed_edge_pattern, third_line)
			undirected_edges = re.findall(undirected_edge_pattern, third_line)
			num_of_edges = len(directed_edges) if len(directed_edges) > len(undirected_edges) else len(undirected_edges)
		return num_of_edges


	def _can_be_converted_to_float(self, value: Any):
		try:
			float(value)	
			return True
		except ValueError:
			return False 


	def _clean_edges_values(self, edges: list):
		"""This method is supposed to run ONLY if all the data in the file is valid"""

		directed_edge_pattern = "^\(\s*(\w)\s*,\s*(\w)\s*\)$"
		undirected_edge_pattern = "^\{\s*(\w)\s*,\s*(\w)\s*\}$"
		cleaned_edges_values = list()
		for tuple_or_set in edges:
			if self.is_it_tuple_or_set(edges) == 'tuple':
				match = re.match(directed_edge_pattern, tuple_or_set)
				first_value = match.group(1)
				second_value = match.group(2)
				cleaned_edges_values.append((first_value, second_value))
			else:
				match = re.match(undirected_edge_pattern, tuple_or_set)
				first_value = match.group(1)
				second_value = match.group(2)
				cleaned_edges_values.append({first_value, second_value})

		return cleaned_edges_values
	
	# TODO: refatorar par buscar na linha de index 2
	def _get_edge_label_values(self, file_path: str) -> list:
		file = open(file_path, 'r')
		lines = file.readlines()
		file.close()
		fifth_line = lines[4].strip()
		edge_labels = fifth_line.split(',')
		edge_labels = set(map(lambda edge_label: edge_label.strip(), edge_labels))
		edge_labels = set(filter(lambda edge_label: edge_label != '', edge_labels))
		return edge__labels

	def is_it_tuple_or_set(self, values: list) -> bool:
		if values[0][0] == '(':
			return "tuple"
		elif values[0][0] == '{':
			return "set"
		return ""


	def _clean_weights_values(self, weights: list):
		cleaned_weights_values = list()
		for weight in weights:
			cleaned_weights_values.append(float(weight))
		return cleaned_weights_values





# mapper = GraphFileMapper("/Users/ewertonluna/tmp/graph.txt")
# print(mapper.get_graph_values(mapper.file_path))
