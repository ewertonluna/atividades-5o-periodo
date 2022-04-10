from graph import Graph
from graph_file_mapper import GraphFileMapper
from graph_exception import GraphException
from os import system, name
from application_headers import main_header, subheader, group_name_header
from graph_file_mapper_exception import GraphFileMapperException
from text_file_import_requirements import requirements

class Menu:

	def __init__(self):
		self.graph = None
		self._graph_file_mapper = None


	def show_main_menu(self):
		menu_options = {
			'1': self._show_add_vertices_menu, 
			'2': self._show_add_edges_menu,
			'3': self._show_import_graph_menu
		}

		run = True
		while run:
			self._clear_and_apply_headers()
			print("** MENU PRINCIPAL **")
			print("Entre com a opção desejada [digite 'sair' terminar o programa]")
			print("1) Adicionar vértices")
			print("2) Adicionar arestas")
			print("3) Importar grafo a partir das informações de um arquivo")
			print("4) Ir para o Menu de Informações do Grafo.")
			option = input(">>> ")

			if option == "sair":
				break

			if option not in menu_options.keys(): 
				print("⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE.️ ⚠")
				input("Entre com qualquer tecla para continuar... ")
				continue

			menu_options[option]()
	
	
	def _show_create_graph_instance_menu(self):
		run = True
		while run:
			self._clear_and_apply_headers()
			print("** MENU DE CRIAÇÃO DA INSTÂNCIA DO GRAFO **")
			print("Entre com o número da opção p/ dizer se o grafo é direcionado ou não-direcionado:")
			print("1) Grafo direcionado")
			print("2) Grafo não-direcionado")

			option = input(">>> ")
			if option != '1' and option != '2':
				print('⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE ⚠')
				input("Entre com qualquer tecla para continuar... ")
				continue
			
			is_directed = False
			if option == '1':
				is_directed = True

			self.graph = Graph(is_directed)
			print("Grafo criado com sucesso! \U0001F60A")
			input("Entre com qualquer tecla para ser encaminhado(a) ao Menu de Adição de Vértices... ")
			run = False

		self._show_add_vertices_menu()


	def _show_add_vertices_menu(self):
		self._clear_and_apply_headers()

		if self.graph is None:
			print("⚠ O grafo precisa ser criado antes da adição dos vértices. ⚠")
			input("Entre com qualquer tecla para ser encaminhado(a) ao Menu de Criação da Instância do Grafo... ")
			self._show_create_graph_instance_menu()
		else:
			run = True
			while run:
				self._clear_and_apply_headers()
				print("** MENU DE ADIÇÃO DE VÉRTICES **")
				label = input("Entre c/ a label do vértice [digite 'sair' p/ voltar ao Menu Inicial] >>> ")

				if label.lower().strip() == 'sair':
					break

				try:
					self.graph.add_vortex(label)
				except GraphException as e:
					print("⚠ Erro ao adicionar vértice " + str(e))
					input("Entre com qualquer tecla para continuar...")
					continue
				print(f"Vértice de label '{label}' adicionado com sucesso! \U0001F60A")
				print(f"Vértices existentes: {list(self.graph.vertices.keys())}")
				input("Entre com qualquer tecla para continuar adicionando vértices... ")
				

	def _show_add_edges_menu(self):
		self._clear_and_apply_headers()
		num_of_vertices = 0 if self.graph is None else len(self.graph.vertices)
		existent_vertices = [] if self.graph is None else list(self.graph.vertices.keys())

		# TODO: concluir esse check da adição de arestas
		if self.graph is None or len(self.graph.vertices) < 2:
			print("⚠ O grafo precisa ter pelo menos dois vértices para que uma aresta possa ser inserida. ⚠")
			print(f"⚠ Quantidade de vértices atual: {num_of_vertices}. ⚠")
			input("Entre com qualquer tecla para voltar ao Menu Principal... ")
		else:
			run = True
			while run:
				self._clear_and_apply_headers()
				print("** MENU DE ADIÇÃO DE ARESTAS **")
				label = input("Entre c/ a label da aresta [digite 'sair' p/ concluir] >>> ")

				if label.lower().strip() == 'sair':
					break

				weight = input("Entre com o peso da aresta [Caso não tenha peso, inserir 0] >>> ")

				connected_vertices = None
				if self.graph.is_directed:
					starting_vortex = input(f"Entre c/ a label do vértice de onde a aresta '{label}' sai (vértices existentes: {existent_vertices}) >>> ")
					arrival_vortex = input(f"Entre c/ a label do vértice de onde a aresta '{label}' chega (vértices existentes: {existent_vertices})  >>> ")
					connected_vertices = starting_vortex, arrival_vortex
				else:
					vortex_1 = input(f"Entre c/ a label do primeiro vértice que está conectado a essa aresta (vértices existentes: {existent_vertices}) >>> ")
					vortex_2 = input(f"Entre c/ a label do segundo vértice que está conectado a essa aresta (vértices existentes: {existent_vertices}) >>> ")
					connected_vertices = {vortex_1, vortex_2} 

				try:
					self.graph.add_edge(label, connected_vertices, weight)
				except GraphException as e:
					print("⚠ Erro ao adicionar aresta: " + str(e) + " Tente novamente. ⚠")
					input("Entre com qualquer tecla para continuar...")
					continue

				print(f"Vértice '{label}' inserido com sucesso! \U0001F60A")
				input("Entre com qualquer tecla para continuar adicionando arestas... ")
	

	def _show_import_graph_menu(self):
		run = True
		while run:
			self._clear_and_apply_headers()
			print("** MENU DE IMPORTAÇÃO DO GRAFO **")
			print("Entre com a opção desejada [digite 'sair' para voltar ao Menu Principal]")
			print("1) Importar grafo a partir de arquivo de texto")
			print("2) Ver informações sobre requisitos os para o arquivo de texto")
			option = input(">>> ")

			if option.lower() == "sair":
				break
			if option != '1' and option != '2':
				print('⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE ⚠')
				input("Entre com qualquer tecla para continuar... ")
				continue

			if option == "1": 
				self._clear_and_apply_headers()
				file_path = input("Entre com o path absoluto do arquivo de texto a ser importado: ")
				file_path = file_path.strip()
				self._graph_file_mapper = GraphFileMapper(file_path)
				try:
					graph_values = self._graph_file_mapper.get_graph_values()
					print("Informações importadas com sucesso! \U0001F60A")
					graph = self._convert_file_info_into_graph(graph_values)
					if graph:
						self.graph = graph
						print("Grafo gerado a partir do arquivo importado! \U0001F60A")
					else:
						print("Não foi possível gerar o grafo a partir do arquivo. Certifique-se que as informações do arquivo estão corretas e tente novamente.")
					input("Entre com qualquer tecla para continuar... ")
				except GraphFileMapperException as gfme:
					print("⚠ Erro ao buscar informações do grafo pelo arquivo: " + str(gfme) + " ⚠")
					input("Entre com qualquer tecla para continuar... ")
					continue
				except Exception as e:
					print("⚠ General Error: " + str(e) + " ⚠")
					input("Entre com qualquer tecla para continuar... ")
					continue

			if option == "2":
				self._clear_and_apply_headers()
				print("Entre com qualquer concluir a visualização dos requisitos...\n\n")
				print(requirements)
				print("\n\n")
				input("Entre com qualquer concluir a visualização dos requisitos... ")
				continue
	
	
	def _convert_file_info_into_graph(self, graph_info: dict) -> Graph:
		is_directed = graph_info['is_directed']
		vertices_labels = graph_info['vertices_values']
		edge_labels = graph_info['edge_label_values']
		connected_vertices = graph_info['connected_vertices']
		weight_values = graph_info['weight_values']
		graph = Graph(is_directed)
		try:
			for label in vertices_labels:
				graph.add_vortex(label)
			print(f"Vértices adicionados com sucesso! \U0001F60A")
		except GraphException as e:
			print("⚠ Erro ao adicionar vértice " + str(e) + " ⚠")
			input("Entre com qualquer tecla para continuar... ")
			return None

		try:
			for i in range(0, len(edge_labels)):
				label = edge_labels[i]
				weight = weight_values[i]
				pair_of_vertices = connected_vertices[i]
				self.graph.add_edge(label, pair_of_vertices, weight)
			print(f"Arestas adicionadas com sucesso! \U0001F60A")
		except GraphException as e:
			print("⚠ Erro ao adicionar arestas " + str(e) + " ⚠")
			input("Entre com qualquer tecla para continuar... ")
			return None
		
		return graph


	def _clear(self):
		if name == 'nt':
			system('cls')
		else:
			system('clear')


	def _clear_and_apply_headers(self):
		self._clear()
		print(main_header)
		print(subheader)
		print(group_name_header)




# Testing
menu = Menu()
menu.show_main_menu()
		
