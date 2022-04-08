from edge_exception import EdgeException
from graph import Graph
from graph_exception import GraphException
from os import system, name
from application_headers import main_header, subheader


class Menu:

	def __init__(self):
		self.graph = None


	def show_main_menu(self):
		menu_options = {
			'1': self._add_vertices, 
			'2': self._add_edges
		}

		run = True
		while run:
			self._clear_and_apply_headers()
			print("Entre com a opção desejada [digite 'sair' p/ ir à adição de arestas]:")
			print("1) Adicionar vértices")
			print("2) Adicionar vértices")
			print("3) Carregar grafo a partir das informações do arquivo 'grafo.txt'")
			print("4) Ir para o menu de informações do grafo.")
			option = input(">>> ")

			if option == "sair":
				break

			if option not in menu_options.keys(): 
				print("⚠️ OPÇÃO NÃO VÁLIDA. TENTE NOVAMENTE.️ ⚠")
				input("Entre com qualquer tecla para continuar... ")
				continue

			menu_options[option]()
	
	
	def _clear(self):
		if name == 'nt':
			system('cls')
		else:
			system('clear')

	def _clear_and_apply_headers(self):
		self._clear()
		print(main_header)
		print(subheader)

	def _create_graph_instance(self):
		self._clear_and_apply_headers()
		print("** Menu de Criação da Instância do Grafo **")

		run = True
		while run:
			print("Entre com o número da opção p/ dizer se o grafo é direcionado ou não-direcionado:")
			print("1) Grafo direcionado")
			print("2) Grafo não-direcionado")

			option = input(">>> ")
			if option != '1' and option != '2':
				print('⚠️ Opção não válida. Tente novamente. ⚠')
				input("Entre com qualquer tecla para continuar... ")
				continue
			
			is_directed = False
			if option == '1':
				is_directed = True

			self.graph = Graph(is_directed)
			print("Grafo criado com sucesso! \U0001F60A")
			input("Entre com qualquer tecla para voltar ao menu inicial... ")

			run = False


	def _add_vertices(self):
		self._clear_and_apply_headers()
		print("** Menu de Adição de Vértices **")

		if self.graph is None:
			print("⚠ O grafo precisa ser criado antes da adição dos vértices. ⚠")
			input("Entre com qualquer tecla para ir ao Menu de Criação da Instância do Grafo... ")
			self._create_graph_instance()
		else:
			run = True
			while run:
				label = input("Entre c/ a label do vértice [digite 'sair' p/ ir à adição de arestas] >>> ")

				if label.lower().strip() == 'sair':
					break

				try:
					self.graph.add_vortex(label)
				except GraphException as e:
					print("⚠ Erro ao adicionar vértice " + str(e))
					input("Entre com qualquer tecla para continuar...")
					continue
				print(f"Vértice de label '{label}' adicionado com sucesso!")
				

	def _add_edges(self):
		self._clear_and_apply_headers()

		# TODO: concluir esse check da adição de arestas
		if self.graph is None or len(self.graph.vertices) < 2:
			print("⚠ O grafo precisa ter pelo menos dois vértices para que uma aresta possa ser inserida. ⚠")
			input("Entre com qualquer tecla para voltar ao Menu Principal... ")
		else:
			run = True
			while run:
				print("** Menu de Adição de Arestas **")
				label = input("Entre c/ a label da aresta [digite 'sair' p/ concluir] >>> ")

				if label.lower().strip() == 'sair':
					break

				connected_vertices = None
				if self.graph.is_directed:
					starting_vortex = input(f"Entre c/ a label do vértice de onde a aresta '{label}' sai >>> ")
					arrival_vortex = input(f"Entre c/ a label do vértice de onde a aresta '{label}' chega  >>> ")
					connected_vertices = starting_vortex, arrival_vortex
				else:
					vortex_1 = input(f"Entre c/ a label do primeiro vértice que está conectado a essa aresta >>> ")
					vortex_2 = input(f"Entre c/ a label do segundo vértice que está conectado a essa aresta >>> ")
					connected_vertices = {vortex_1, vortex_2} 

				weight = input("Entre com o peso da aresta. [Caso não tenha peso, inserir 0] >>> ")

				try:
					self.graph.add_edge(label, connected_vertices, weight)
				except GraphException as e:
					print("⚠ Erro ao adicionar arestas: " + str(e) + " Tente novamente. ⚠")
					input("Entre com qualquer tecla para continuar...")
					continue

				print(f"Vértice '{label}' inserido com sucesso! \U0001F60A")

				




# Testing
menu = Menu()
menu.show_main_menu()
		
