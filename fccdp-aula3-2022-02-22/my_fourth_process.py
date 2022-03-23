import time

from multiprocessing import Process
from unicodedata import name

class MyFourthProcess(Process):
	def __init__(self, values, id):
		Process.__init__(self)
		self.id = id
		self.values = values
	
	def compute_prime_factors(self, values):
		factors = []
		for value in values:
			factors.append(self.num_prime_factors(value))
		return factors
	
	def num_prime_factors(self, number):
		prime_factors = 0
		n = number

		for i in range(2, number+1):
			while n % i == 0:
				prime_factors += 1
				n /= i
		return prime_factors

	def run(self):
		start = time.time()
		self.compute_prime_factors(self.values)
		end = time.time()
		print(f"Letra e) - Runtime de compute_prime_factores no processo {self.id} foi de {(end - start)}s")
	
