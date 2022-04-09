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
	
	# TODO: Completar esse método
	def _has_right_format(self, file_path: str):
		pass


# mapper = GraphFileMapper("/Users/ewertonluna/temp/graph.txt")
# print(mapper._is_file_emtpy("/Users/ewertonluna/temp/graph.txt"))