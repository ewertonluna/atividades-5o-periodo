# Questão 1 - 1,5 pts

Vimos em sala de aula o conceito das transparências que um sistema distribuído pode oferecer aos seus usuários:
- Transparência de Acesso
- Transparência de Localização
- Transparência de Migração
- Transparência de Relocação
- Transparência de Replicação
- Transparência de Concorrência
- Transparência de Falha

Explique, com suas palavras, três das transparências citadas acima.

# Resposta
R:
- TransparÊnca de Localização: clientes de um serviço não sabem a localização deste até que ele seja localizado no registro. O lookup e o
binding dinâmico a um serviço em tempo de execução permite à implementação desse serviço a se mover de locais sem que o cliente saiba. A capacidade
de mover o serviço melhora a disponibilidade e a performance dele.

- TransparÊncia de Falha: se refere até que ponto os erros e as recuperações dos sitemas onde esses erros acontecem, são invisíveis aos usuários e 
aplicações. Quando usuários são automaticamente redirecionados a outro servidor quando um determinado servidor cai, de modo que os usuários nem
notem a falha, significa dizer que o sistema tem alta transparência a falha.

- Transparência de Migração: é o que permite o movimento de recursos dentro de um sistema sem que o usuário do recurso note. Essa transparênca é
o que garante o fato de um recurso poder mover para um local diferente dentro do sistema e ainda ser acessível da mesma forma pelo usuário.
Também significa dizer que um sistema não precisa mudar seu nome se ele migra.