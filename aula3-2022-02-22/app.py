import time
from my_first_process import MyFirstProcess
from my_second_process import MySecondProcess
from my_third_process import MyThirdProcess
from my_fourth_process import MyFourthProcess

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
		my_first_process = MyFirstProcess(i)
		my_first_process.start() 
	# ** Fim da letra a **

	# ** Início da letra b **
	array_letra_a = get_int_array(10)
	start = time.time()
	my_second_process = MySecondProcess(1, array_letra_a)
	my_second_process.start()
	my_second_process.join()
	end = time.time()
	print(f"Letra b) Tempo de execução no processo principal: {end - start}s")
	# ** Fim da letra b **	

	# ** Início da letra c **
	start = time.time()
	my_third_process = MyThirdProcess(1)
	my_third_process.start()
	my_third_process.join()
	end = time.time()
	print(f"Letra c) Overhead de criar e executar um processo: {end - start}s")
	# ** Fim da letra c **	

	# ** Início da letra d **
	print("Letra d) - Por favor, olhar o código para ver implmentação de partition_data.")
	# ** Fim da letra d **	

	# ** Início da letra e **
	# ** Fim da letra e **	


	# ** Implementação da letra d **
	def partition_data(values, start_index, end_index):
		return values[start_index:end_index]
	# ** Fim da implementação da letra d **

	# ** Início da letra e **
	number_of_processes = 4
	work_load = 3
	values = list(range(number_of_processes * work_load))
	print(f"Letra e) - O número de processos que serão usados é {number_of_processes}. Cada processo terá um workload de {work_load}. Para alterar esses valores, bassta modificar o valor das variáveis number_of_processes e work_load.")
	for i in range(number_of_processes):
		local_values = partition_data(values, i * work_load, work_load * (i + 1) - 1)
		my_fourth_process = MyFourthProcess(local_values, i)
		my_fourth_process.start()
	# ** Fim da letra e **
