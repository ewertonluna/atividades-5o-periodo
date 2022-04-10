requirements = """\
REQUISITOS DE VALIDADE PARA O ARQUIVO

Para que o grafo possa ser criado corretamente a partir do arquivo de texto
o arquivo precisa cumprir alguns requisitos:

i)		Ter pelo menos 4 linhas

ii) 	Na 1a linha, informar se é direcionado ou não. Valores aceitos: "direcionado" ou "não direcionado"

iii) 	Na 2a linha, informar as labels dos vértices colocando valores separados por vírgula. Ex.: a,b,c,d,e

iv) 	Na 3a linha, informar através de tuplas (se o grafo for direcionado) ou sets (se for não direcionado) onde cada tupla seja separada por vírgula
		Ex.: Para grafo direcionado: (a, b),(c, d), (e, a)
		Ex.: Para grafo direcionado: {a, b},{c, d}, {e, a}
		Obs: É permitido que a linha não contenha valores.

v) 		Na 4a linha, também contendo separação por vírgula, informar os pesos das respectivas arestas descritas pela linha anterior. 
		A quantidade de pesos precisa corresponder à quantidade de arestas informadas.
		Os valores precisam ser numéricos (int ou float)
		Ex.: 10,3.5,4.3
		Obs: É permitido que a linha não contenha valores se, e somente se, a 3a linha não contiver valores.

vi)		Caso o arquivo não seja válido, o programa imprimirá uma mensagem explicando o porquê.


EXEMPLO DE ARQUIVO ACEITO (Caso Direcionado)

direcionado
a,b,c,d,e,f,g
(b,d),(c,e),(f,g),(g,a)
13.2,5,4.8,50
<tudo da quinta linha em diante é ignorado>

EXEMPLO DE ARQUIVO ACEITO (Caso Não-Direcionado)

não direcionado
a,b,c,d,e,f,g
{b,d),{c,e},{f,g},{g,a}
13.2,5,4.8,50
<tudo da quinta linha em diante é ignorado>

"""