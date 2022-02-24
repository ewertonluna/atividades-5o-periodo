from multiprocessing import Process
from unicodedata import name

class MyFirstProcess(Process):
	def __init__(self, id):
		Process.__init__(self)
		self.id = id

	def run(self):
		print(f"Hello process {self.id}")
