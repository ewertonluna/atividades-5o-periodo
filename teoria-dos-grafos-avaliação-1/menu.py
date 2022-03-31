from edge_exception import EdgeException
from graph import Graph
from vortex import Vortex
from edge import Edge
from graph_exception import GraphException


class Menu:

	def __init__(self):
		self.graph = None


	def create_graph(self):
		run = True

		while run:
			print("Entre com o número da opção p/ dizer se o grafo é direcionado ou não-direcionado:")
			print("1) Grafo direcionado")
			print("2) Grafo não-direcionado")

			option = input(">>> ")
			if option != '1' and option != '2':
				print('Opção não válida. Tente novamente.')
				continue
			
			is_directed = False
			if option == '1':
				is_directed = True
			
			self.graph = Graph(is_directed)
			run = False
		self._add_vertices()
		self._add_edges()


	def _add_vertices(self):
		print("** Adição de Vértices **")

		if self.graph is None:
			print("Primeiro é preciso criar o grafo. Tente novamente.")
		else:
			run = True
			while run:
				label = input("Entre c/ a label do vértice [digite 'sair' p/ ir à adição de arestas] >>> ")

				if label.lower().strip() == 'sair':
					break

				try:
					self.graph.add_vortex(label)
				except GraphException as e:
					print("Erro ao adicionar vértice " + str(e))
					continue
				print(f"Vértice de label '{label}' adicionado com sucesso!")
				

	# TODO: 
	# Existe bug nesse ou em outros métodos. Mesmo inserido os vértices e colocando as arestas conectando vértices válidos
	# está acontecendo mensagem de erro imprópria.
	def _add_edges(self):
		print("** Adição de Arestas **")
		if self.graph is None:
			print("Primeiro é preciso criar o grafo. Tente novamente.")
		else:
			run = True
			while run:
				label = input("Entre c/ a label da aresta [digite 'sair' p/ concluir] >>> ")

				if label.lower().strip() == 'sair':
					break

				connected_vertices = None
				if self.graph.is_directed:
					starting_vortex = input(f"Entre c/ a label do vértice de onde a aresta '{label}' sai >>> ")
					arrival_vortex = input(f"Entre c/ a label do vértice de onde a aresta '{label}' sai >>> ")
					connected_vertices = starting_vortex, arrival_vortex
				else:
					vortex_1 = input(f"Entre c/ a label do primeiro vértice que está conectado a essa aresta >>> ")
					vortex_2 = input(f"Entre c/ a label do segundo vértice que está conectado a essa aresta >>> ")
					connected_vertices = {vortex_1, vortex_2} 

				weight = input("Entre com o peso da aresta. [Caso não tenha peso, inserir 0] >>> ")

				try:
					self.graph.add_edge(label, connected_vertices, weight)
				except GraphException as e:
					print("Erro ao adicionar arestas" + str(e) + ". Tente novamente.")
					continue

				print(f"Vértice '{label}' inserido com sucesso!")

				




# Testing
menu = Menu()
menu.create_graph()
		
