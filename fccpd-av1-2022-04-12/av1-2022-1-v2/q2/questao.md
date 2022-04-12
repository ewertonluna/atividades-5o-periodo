# Questão 2 - 2 pts

O Java oferece o conceito de monitores que foi proposto por Dijkstra e posteriormente desenvolvido por Hoare e Hansen. Explique, em separado, com suas palavras, o papel de cada um dos itens a seguir que fazem parte da implementação dos monitores no Java:

## Palavra reservada synchronized
R: A palavra reservada synchronized em Java está relacionada com Thread safety. Ela garante que um determinado bloco de código,
ou até mesmo a classe inteira (para o caso onde synchronized é usado num método estático),
não seja acessada simultaneamente por mais de uma Thread ao mesmo tempo. 
Ela permite que o código seja acessado um código seja acessado por diferentes Threads, mas de maneira segura, sem que haja race condition.
Sem synchronized, não tem como garantir a ordem que um recurso é acessado/escrito.

## Método Object.wait() e Object.wait(timeout)
R: O método wait, que permite a entrada de um parâmetro 'timeout' é um método que faz com que a Thread que está executando um determinado bloco
de código entre em estado de espera indefinidamente, caso não seja passado o timeout, ou pelo tempo de timeout. Quando a Thread então entra,
nesse estado de espera, ela libera o lock sobre o objeto ou classe que ela havia prendido.

## Método Object.notify() e Object.notifyAll()
R: O método notify e notifyAll servem para que a Thread que está em execução "avise" as outras threads que estão em estado de espera para que
saiam do estado de espera e voltem a executar. 
No caso do nofifyAll, esse aviso chega para todas as Threads que estão em espera, já 
o notify visa acordar alguma thread que está esperando pelo monitor do objeto que não está liberado. 
Esse aviso pelo notify é dado para uma Thread aleatória que está em espera do monitor do objeto.
