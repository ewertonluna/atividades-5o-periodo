from multiprocessing import Process
from unicodedata import name

class MyThirdProcess(Process):
	def __init__(self, id):
		Process.__init__(self)
		self.id = id

	def run(self):
		pass
