import time
from my_first_thread import MyFirstThread
from my_second_process import MySecondProcess

def get_int_array(size):
	int_aray = []
	for i in range(size):
		int_aray.append(i)
	return int_aray

def compute_prime_factors(values): 
	factors = []
	for value in values: 
		factors.append(num_prime_factors(value))
	return factors

def num_prime_factors(number): 
	prime_factors = 0
	n = number

	for i in range(2,number+1):
		while n % i == 0: 
			prime_factors+=1 
			n /= i
	return prime_factors

if __name__ == '__main__':
	# ** Início da letra a **
	for i in range(10):
		my_first_thread = MyFirstThread(i)
		my_first_thread.start() 
	# ** Fim da letra a **

	# ** Início da letra b **
	array_letra_a = get_int_array(10)
	start = time.time()
	my_second_process = MySecondProcess(1, array_letra_a)
	my_second_process.start()
	end = time.time()
	print(f"Letra b) Tempo de execução no processo principal: {end - start}s")
	# ** Fim da letra b **	

	# ** Início da letra c **
	# ** Fim da letra c **	

	# ** Início da letra d **
	# ** Fim da letra d **	

	# ** Início da letra e **
	# ** Fim da letra e **	