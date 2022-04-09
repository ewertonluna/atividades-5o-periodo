from graph_file_mapper_exception import GraphFileMapperException
import os


class GraphFileMapper:

	def __init__(self, file_path: str):
		self.file_path = file_path
	

	def set_file_path(self, file_path: str):
		if (file_path is None) or (not isinstance(file_path, str)):
			raise GraphFileMapperException("'file_path' must be a string")
		self.file_path = file_path
	

	def _get_validation_message(self, file_path: str):
		# check if file exists
		# check if file is empty
		# check if file is correctly formatted
		# check if file is missing some field
		validation_message = ""
		try:
			file = open(self.file_path, 'r')
		except FileNotFoundError as fnfe:
			validation_message += "The file was not found. "
		except PermissionError as pe:
			validation_message += "The current user doesn't have permission to read the file. "
		if self._is_file_emtpy(file_path):
			validation_message += "The file is empty. "


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
		return True if len(lines) >= 4 else False

	def _is_first_line_valid(self, file_path: str):
		file = open(file_path, 'r')
		lines = file.readlines()
		first_line = lines[0].strip()
		return True if (first_line == 'direcionado' or first_line == 'não direcionado') else False

	# TODO: Terminar de fazer essa verificação. Valores não podem ser vazios
	def _is_second_line_valid(self, file_path: str):
		is_valid = True
		file = open(file_path, 'r')
		lines = file.readlines()
		second_line = lines[1].strip()
		vertices_values = second_line.split(',')
		for i in range(0, len(vertices_values)):
			vertices_values[i] = vertices_values[i].strip()
		print(vertices_values)
		return True if (second_line == 'direcionado' or second_line == 'não direcionado') else False




mapper = GraphFileMapper("/Users/ewertonluna/tmp/graph.txt")
print(mapper._is_second_line_valid(mapper.file_path))
# print(mapper._is_file_emtpy("/Users/ewertonluna/temp/graph.txt"))
