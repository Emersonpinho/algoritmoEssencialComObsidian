A notação Big 0 é uma notação especial que diz o quão rápido é um algoritmo. Mas quem liga para isso? bem, acontece que você frequentemente utilizará o algoritmo  que outra pessoas fez - e quando faz isso, é bom entender o quão rápido ou lento o algoritmo é. nesta seção, explicarei como a notação Big O funciona e fornecerei uma lista com os tempos de execução mais comuns para os algoritmos.

### tempo de execução dos algoritmos cresce a taxas diferentes 
Bob está escrevendo um algoritmo para a NASA. O algoritmo dele entrará em ação quando o foguete estiver prestes a pousar na lua, e ele o ajudará a calcular o local de pouso.
Este é um exemplo de como o tempo de execução de dois algoritmos pode
crescer a taxas diferentes. Bob está tentando decidir entre a pesquisa simples
e a pesquisa binária. O algoritmo precisa ser tão rápido quanto correto. Por
um lado, a pesquisa binária é mais rápida, o que é bom, pois Bob tem apenas
10 segundos para descobrir onde pousar, ou o foguete sairá de seu curso. Por
outro lado, é mais fácil escrever a pesquisa simples, o que gera um risco
menor de erros. Bob não quer mesmo erros no seu código! Para ser ainda
mais cuidadoso, Bob decide cronometrar ambos os algoritmos com uma
lista de 100 elementos.
Vamos presumir que leva-se 1 milissegundo para veri car um elemento.Com a pesquisa simples, Bob precisa veri car 100 elementos, então a busca
leva 10 ms para rodar. Em contrapartida, ele precisa veri car apenas sete
elementos na pesquisa binária (log2 100 é aproximadamente 7), logo, a
pesquisa binária leva 7 ms para ser executada. Porém, realisticamente
falando, a lista provavelmente terá em torno de 1 bilhão de elementos. Se a
lista tiver esse número, quanto tempo a pesquisa simples levará para ser
executada? E a pesquisa binária? Tenha certeza de que sabe a resposta para
essa pergunta antes de continuar lendo.

a notação Big informa o quão rápido é um algoritmo. por exemplo, imagine que você tem uma lista de tamanho _n_. o tempo de execução na notação Big O é O(_n_). onde estão os segundos? eles não existem - **a notação Big O não fornece o tempo em segundos. A notação Big O permite que você compare número de operações. Ela informa o quão rapidamente um algoritmo cresce** 
