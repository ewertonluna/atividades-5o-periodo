# Exercício 4
## Grupo: Carolina Vasconcelos, Ewerton Luna, Marcela Cavalcante, Mariana Coutinho
### Letra a
Solução: Olhar a implementação da classe SequentialCounter
### Letra b
O valor final de getValue() é 1000, pois estamos imprimindo o valor de getValue() depois que o método Thread.join(), isso garante que a execução da Thread termina antes que o valor de getValue seja impresso no standardout. 
Caso Thread.join() não fosse chamada antes da impressão do valor, o valor final (impresso) poderia ter um valor aleatório entre 0 e 1000.
Isso acontece por que não há garantias de quantas vezes o método increment() seria chamado até que o valor fosse printado.

### Letra c
O valor final de getValue() vai depender de em que momento o valor getValue() é chamado. Como não fizemos a chamada do método Thread.join(), o valor de getValue() está sendo um valor entre 0 e 10000. No caso da última execução, esse valor foi 8666. <br>
Olhar o código para conferir que isso acontece por falta de garantia de sincronia das threads.<br>
A segunda versão de Counter está implementada através na classe SafeSequentialCounter.

### Letra d
Como o pedido da questão em determinar os tempos de execução não estão muito claros se quer-se o tempo de execução dentro da thread ou fora dela, decidimos usar um timer dentro do método run() das Threads.
Os valores dos tempos são obtidos a partir daí. <br>
Optamos por fazer a medição dentro do run() pois, como não estamos usando join() após chamar o start(), o valor do tempo medido fora do run() não iria corresponder necessariamente ao tempo de execução da Thread que chama o Counter.
Qualquer dúvida, olhar a resolução através da classe MainLetraD pois cada uma das combinações que foram pedidas estão separadas, como indica os breves comentários. <br>
Favor, olhar o código de MainLetraD, MySecondCounter e SafeSequentialCounter.
### Letra e
Não há padrão. Apesar de o synchronized usado dentro da classe SafeSequentialCounter, a keyword garante apenas que duas threads não irão chamar o método ao mesmo tempo. Porém, não há garantias sobre a ordem que elas executam.
### Letra f
Olhar a implementação em MainLetraF.java, FairSynchronizedCounter.java e MyFourthThread.java.
PS: Na nossa implementação, fizemos o round robin executar indefinidamente 3 rounds. É possível modificar a quantidade de rounds que o round robin irá ter, apenas alterando a variável i que fica dentro do loop while
contido no método run() da classe MyFourthThread.java