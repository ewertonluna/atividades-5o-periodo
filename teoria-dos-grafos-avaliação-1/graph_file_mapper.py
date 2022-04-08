from graph_file_mapper_exception import GraphFileMapperException


class GraphFileMapper:

	def __init__(self, file_path: str):
		self.file_path = file_path
	

	def set_file_path(self, file_path: str):
		if (file_path is None) or (not isinstance(file_path, str)):
			raise GraphFileMapperException("'file_path' must be a string")
		self.file_path = file_path
	

	def _get_validation_message(self):
		# check if file exists
		# check if file is empty
		# check if file is correctly formatted
		# check if file is missing some field
		pass


	def is_file_path_valid(self):
		pass
