from graph import Graph
from vortex import Vortex
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
		# self.add_edges()


	def _add_vertices(self):
		print("** Adição de Vértices **")

		if self.graph is None:
			print("Primeiro é preciso criar o grafo. Tente novamente.")
		else:
			run = True
			while run:
				label = input("Entre c/ a label do vértice [digite 'sair' p/ concluir] >>> ")

				if label.lower().strip() == 'sair':
					break

				vortex = Vortex(label)
				try:
					self.graph.add_vortex(vortex)
				except GraphException as e:
					print("Erro ao adicionar vértice " + str(e))
					continue
				print(f"Vértice de label '{label}' adicionado com sucesso!")
				

# Testing
# menu = Menu()
# menu.create_graph()
		
