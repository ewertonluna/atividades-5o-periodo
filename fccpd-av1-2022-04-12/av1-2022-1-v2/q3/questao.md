# Questão 3 - 1,5 pts

Vimos na disciplina que temos duas alternativas para tratarmos uma carga maior em nossa aplicação: a escalabilidade vertical (também conhecida como Scale Up) e a escalabilidade horizontal (também conhecida como Scale Out). Explique, com suas palavras, cada um dos conceitos, suas vantagens, desvantagens e limitações.

# Escalabilidade vertical
R: Escalabilidade vertical está relacionada com aumentar a capacidade de um sistema melhorando o hardware ou software melhorando os recursos, por
exemplo: aumentando a frequencia do CPU, usando uma CPU com mais núcleos, aumentando a memória RAM, usando um disco rígido com tecnologia mais
rápida. Escalabilidade vertical, basicamente, está relacionada com a melhora de uma máquina específica.
Uma vantagem é que pode ser mais barato melhorar uma única máquina do que diversas máquinas. 
No entanto, como desvantagem há o fato de que essa melhora é limitada pelo "tamanho" da sua máquina hospedeira. 
Nessa forma de escalabilidade, não há compartilhamento de memória: tudo está alocado num único nó da infraestrutura da rede.
Outras vantagens é que essa escalabilidade é de fácil implementação, consome menos energia, a compatibilidade da aplicação é mantida, entre outros.
Outras desvantagens estão o fato de que cria-se um SPOF (single point of failure) gerando probabilidade de downtimes maiores, 

# Escalabilidade Horizontal
R: Escalabilidade horizontal está relacionada com melhorar a performance adicionando mais máquinas/servidores para darem conta de uma determinada
carga. Dessa forma, consegue-se distribuir melhor a carga entre diferentes sistemas. Nessa forma de escalabilidade, a gente não melhora
a perfomance de um único nó, mas sim a gente diminui a carga individual do nó.
Entre as vantagens da escalabilidade horizontal está o fato de que ela é mais a prova de falha, não há limites para crescimento horizontal, pois
pode-se colocar quantas máquinas quanto se queira (se houver recursos financeiros para isso).
Entre as desvantagens estão o fato de o design da arquitetura ser mais complicado, o custo de energia e manutenção pode ser maior, necessita de
equipamentos de infraestutura de rede como roteadores e comutadores de pacote da camada de enlace.
