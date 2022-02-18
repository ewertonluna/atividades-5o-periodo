# Exercício 2
## Grupo: Carolina Vasconcelos, Cao Guim, Ewerton Luna e Mariana Coutinho.

a) A maneira que usamos para identificar qual das Threads está imprimindo no console foi concatenando o valor do ID da thread a mensagem "Hello Thread!".
A garantia que o programa só irá encerrar após a segunda Thread terminar de executar é dada pelo método da
classe java.lang.Thread chamado join(), que espera a thread atual encerrar antes de prosseguir.
