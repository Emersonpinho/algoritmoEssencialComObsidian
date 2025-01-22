você deve ter pensado "De maneira alguma vou executar um algoritmo que tem o tempo de execução O(n!)" Bem, deixe-me tentar provar ao contrário! Aqui está um exemplo de um algoritmo famoso  da ciência da computação, pois seu crescimento é apavorante e algumas pessoas muito inteligentes acreditam que ele possa ser melhorado. esse algoritmo é chamado de "o problema do caixeiro-vianjante"

você tem um caixeiro-viajante. 
o caixeiro precisa ir a cinco cidades.
O caixeiro, o qual chamarei de Opus, quer passar por todas as cidades
percorrendo uma distância mínima. Podemos enxergar o problema da
seguinte forma: analisar cada ordem possível de cidades para visitar.

**veja as imagens em recurso relacionada a esse tema**

Ele soma a distância total e escolhe o caminho de menor distância. Existem
120 permutações para cinco cidades, logo, precisa-se de 120 operações para
resolver o problema de cinco cidades. Para seis cidades, precisa-se de 720
operações (ou 720 permutações). Para sete cidades são necessárias 5.050
operações!

Esse algoritmo consome muitas operações, exceto para casos envolvendo números pequenos.

### recapitulando 
- A pesquisa binária é muito mais rápida do que a pesquisa simples.
- O(log n) é mais rápido do que O(n), e O(log n) ca ainda mais rápido conforme os elementos da lista aumentam.
- A rapidez de um algoritmo não é medida em segundos.
- O tempo de execução de um algoritmo é medido por meio de seu crescimento.
- O tempo de execução dos algoritmos é expresso na notação Big O.