# Calculadora-Decimal-para-Binario
eu fiz esse progama para me ajudar nas aulas de conversao numerica na faculdade, essa é uma explicaçao resumida dos processos passo a passo que foram usados no progama

o progama é divido em 3 funçoes que tem que se interconectar algumas vezes e sao utilizadas para calcular a parte inteira do numero e a decimal separadamente.

  a primeira funçao -> (contadorDecimais) recebe um numero real com virgula, que eu vou atribuir nessa expliçao 12,016 e separa a sua parte inteira da sua parte 
decimal, porem, convertidos para string, em seguida é usado a parte inteira para separar a parte decimal do numero original, usando a operaçao 
{numero original - parte inteira = parte decimal  ou  12,016 - 12 = 0,016} desse modo temos um numero iniciado em 0 com uma virgula e suas casas decimais.
esse numero é salvo em duas variaveis, decimalStr para uma versao string do numero, e decimalFloat para uma versao float do numero. logo apos isso a funçao checa
o numero de casas do decimalStr e usa em uma operaçao, onde x = {numero de casas do decimalStr - 2}, o -2 é adicionado para compensar o "0" e o ".", desse modo
temos o resultado como a quantidade de casas decimais do numero original (essa informaçao é util mais para frente). a funçao entao retorna 3 atributos
y = o expoente que na base 10 converte o 0,016 para inteiro ou vice versa sendo nesse caso 1000 (0,016 * 1000 = 16  ou  16 : 1000 = 0,016)
decimalStr = a forma string da decimal
decimalInt = a forma inteira da decimal (0,016 -> 16)

  a segunda funçao -> (fracaoBinario) recebe o mesmo numero real e faz o uso da primeira funcao para receber o seus dados separadamente. apos isso ela converte o numero
para decimal usando o metodo de multiplicaçao de valor decimal da base 10, onde multiplicamos um valor pela base desejada, no caso 2, adicionamos oque passar para 
a parte decimal no numero e seguimos o processo no numero decimal caso nao passe nada adicionamos o zero e seguimos o processo:
0.016 * 2 = 0.032 -> 0

0.032 * 2 = 0.064 -> 00

0.064 * 2 = 0.128 -> 000

0.128 * 2 = 0.256 -> 0000

0.256 * 2 = 0.512 -> 00000

0.512 * 2 = 1.24 -> 000001

e assim por diante, a funçao adiciona os resultados de 0 e 1 numa lista, quando a conta terminar ela separa a lista pelo numero de bits que o usuario pediu e readiciona
os numero em uma string
  
 a terceira funça -> recebe o mesmo numero real, apartir do processo que usamos na primeira funçao conseguimos separar o numero inteiro dessa vez, a funçao entao converte
o numero inteiro para binario usando o metodo de divisao, onde dividimos o numero inteiro pela base desejada e entao colocamos a sobra na parte inteira do resultado
caso nao tenha sobra é colocado o 0 e seguimos o processo
12 / 2 = 6 -> 0
6 / 2 = 3 -> 00
3 / 2 = 1 -> 001
1/2 = nulo -> 0011
e assim por diante, a funçao adiciona os resultados de 0 e 1 numa lista, quando a conta terminar ela readiciona os numero em uma string, porem, por causa da natureza do 
metodo é necessario inverter a lista antes de dar o resultado, assim 0011 = 1100, 12 para decimal = 1100

e finalmente nas linhas individuais do progama ele reuni a parte decimal com a parte inteira e imprimi o resultado
  
