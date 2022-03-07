# Exercício 3
## Grupo: Carolina Vasconcelos, Ewerton Luna, Marcela Cavalcante, Mariana Coutinho
### Letra a
Solução: Olhar a implementação da classe SequentialCounter
### Letra b
O valor final de getValue() é 1000, pois estamos imprimindo o valor de getValue() depois que o método Thread.join(), isso garante que a execução da Thread termina antes que o valor de getValue seja impresso no standardout. 
Caso Thread.joi() não fosse chamada antes da impressão do valor, o valor final (impresso) poderia ter um valor aleatório entre 0 e 1000.
Isso acontece por que não há garantias de quantas vezes o método increment() seria chamado até que o valor fosse printado.

### Letra c
O valor final de getValue() vai depender de em que momento o valor getValue() é chamado. Como não fizemos a chamada do método Thread.join(), o valor de getValue() está sendo um valor entre 0 e 10000. No caso da última execução, esse valor foi 8666.
Olhar o código para conferir que isso acontece por falta de garantia de sincronia das threads.</ br>
A segunda versão de Counter está implementada através na classe SafeSequentialCounter.

### Letra d
Os dois primeiros tópicos da letra d estão resolvidos no código da letra b e da letra c, respectivamente. </ br>
Para os dois tópicos seguintes, checar os valores que são logados ao executar o método main() da classe MainLetraD.
Como o tempo medido fora do método run() da Thread não necessariamente cronometra o tempo de execução, fizemos a medição do tempo dentro da Thread.
Favor, olhar o código de MainLetraD, MySecondCounter e SafeSequentialCounter.
### Letra e
Não há padrão. Apesar de o synchronized usado dentro da classe SafeSequentialCounter, a keyword garante apenas que duas threads não irão chamar o método ao mesmo tempo. Porém, não há garantias sobre a ordem que elas executam.
### Letra f
Olhar a implementação em MainLetraF.java, FairSynchronizedCounter.java e MyFourthThread.java.
PS: Na nossa implementação, fizemos o round robin executar indefinidamente 3 rounds. É possível modificar a quantidade de rounds que o round robin irá ter, apenas alterando a variável i que fica dentro do loop while
contido no método run() da classe MyFourthThread.java