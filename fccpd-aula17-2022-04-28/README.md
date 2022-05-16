# Grupo: Carolina Vasconcelos, Ewerton Luna e Mariana Coutinho

## Instrução para executar casos de uso
No arquivo `app.py` tem-se o código para diferentes casos de uso em cada linha, da linha 10 a linha 17.<br>
Da linha 7 a linha 9 instancia-se 3 instancias de User. Quando User é instanciado, é criada uma fila relacionada com o respectivo user e é feito o
bind da fila criada a Exchange. Caso deseje-se criar novos usuários, é só fazer o mesmo, especificando um id através do construtor de User. Quando
isso for feito, uma nova fila será criada e atrelada a Exchange. A partir disso, essas instâncias podem ler e receber mensagens diretas e em grupo.

## Overview
**Vídeo com a explicação do código e dos conceitos utilizados nesta implementação: [https://youtu.be/KB0GQgSlPn0](https://youtu.be/KB0GQgSlPn0)**<br><br>
A classe User representa um usuário do sistema "zapzap".<br> 
Uma instância desta classe pode enviar mensagens diretamente um usuário e também pode enviar mensagem
para todos os usuários que fazem parte do sistema.<br><br>
Assista o vídeo linkado acima para entender com mais detalhes como seria o uso do sistema.