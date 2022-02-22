import time
from multiprocessing import Process
from unicodedata import name

class MySecondProcess(Process):
	def __init__(self, id, values):
		Process.__init__(self)
		self.id = id
		self.values = values

	def run(self):
		start = time.time()
		self.compute_prime_factors(self.values)
		end = time.time()
		print(f"Letra b) Tempo de execução dentro do processo #{self.id}: {end - start}s")

	def compute_prime_factors(self, values): 
		factors = []
		for value in values: 
			factors.append(self.num_prime_factors(value))
		return factors
	
	def num_prime_factors(self, number): 
		prime_factors = 0
		n = number

		for i in range(2,number+1):
			while n % i == 0: 
				prime_factors+=1 
				n /= i
		return prime_factors
