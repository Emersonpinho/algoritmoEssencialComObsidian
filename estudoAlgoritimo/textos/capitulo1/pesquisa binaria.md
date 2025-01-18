vamos supor que você está buscando o nome de uma pessoa em sua agenda telefônica. o nome dessa pessoa começa com K, provavelmente você não olhara a pagina do começo até chegar ao K porque você sabe que o K está mais pelo meio.

Outro exemplo: suponha que você precisa achar uma palavra que começa com O em um dicionário. novamente você começa a busca pelo meio.

Agora, imagine que você entre no Facebook. quando faz isso, o Facebook precisa verificar que você tem uma conta no site. Logo, ele procura seu nome de usuário em um banco de dados. Digamos que seu usuário seja Karlmageddon. o Facebook poderia começar pelos As e procura seu nome - mas faz mais sentido que ele comece a busca pelo meio.

**Isto é um problema de busca. e todos estes casos usam um algoritmo para resolvê-lo:** _Pesquisa binária._ 

A pesquisa binária é um algoritmo. sua entrada é uma lista ordenada de elementos (explicarei mais tarde por que motivo a lista precisa ser ordenada).
Se o elemento que você está buscando está na lista, a pesquisa binária retorna ```none``` 

**acesse a pagina de recurso e olhe figura 1.1

1      |      2       |      3      |     4       .... 100

Você deve procurar adivinhar o meu número com menor número de tentativas possível. a cada tentativa, digo se você chutou muito para cima, muito para baixo ou corretamente

digamos que começou tentando assim: 1, 2, 3, 4....

**Uma tentativa muito ruim de acertar o número**
isso se chama pesquisa simples (talvez pesquisa estúpida seja um termo melhor) a cada tentativa, você está eliminando apenas um número. se o meu número fosse o 99, Você precisaria de 99 chances para acertá-lo!

#### Uma maneira melhor de busca
comece com 50. muito baixo mas você eliminou metade dos números! agora, você sabe que os números de 1 a 50 são muito baixos. próximo chute: 75.

**observe a figura 1.2 para entender o próximo passo**

