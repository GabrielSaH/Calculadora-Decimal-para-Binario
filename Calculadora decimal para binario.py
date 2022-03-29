# contador de casas decimais
def contadorDecimais(numero):
    numeroString = str(numero)
    lista = numeroString.split(".")
    inteiro = int(lista[0])
    decimalStr = str(round(numero - inteiro, 9))
    decimalFloat = float(round(numero - inteiro, 9))
    x = (len(decimalStr) - 2)
    y = 10 ** x
    decimalInt = int(decimalFloat * y)
    return (y, decimalStr, decimalInt)

# parte fracionaria
def fracaoBinario(objetivo):
    divisor, decimalStr, decimalInt = contadorDecimais(objetivo)
    objetivo = decimalInt / divisor
    resultado = 0
    numeroTeste = 1
    resultadoTeste = 0 
    listaDecimal = []  
    listaFracao = []  
    modoBinario = []  
    while not resultado == objetivo:
        denominadorTeste = 2**numeroTeste
        decimalTeste = {denominadorTeste}
        fracaoTeste = 1/denominadorTeste
        resultadoTeste = resultado + fracaoTeste
        if objetivo > resultado:
            if objetivo > resultadoTeste:
                resultado += fracaoTeste
                listaDecimal.append(fracaoTeste)
                listaFracao.append(decimalTeste)
                numeroTeste += 1
                modoBinario.append("1")
            if objetivo < resultadoTeste:
                numeroTeste += 1
                modoBinario.append("0")
            if objetivo == resultadoTeste:
                resultado += fracaoTeste
                listaDecimal.append(fracaoTeste)
                listaFracao.append(decimalTeste)
                modoBinario.append("1")
        if objetivo == resultado:
           numeroBinario = modoBinario[:bits]
           numeroDecimalSaida = "".join([str(numeral) for numeral in numeroBinario])
           return (numeroDecimalSaida)
        if len(modoBinario) == bits:
            numeroBinario = modoBinario[:bits]
            numeroDecimalSaida = "".join([str(numeral) for numeral in numeroBinario])
            return (numeroDecimalSaida)

# progama que transforma inteiros em binarios
def inteiroBinario(numeroInteiro):
    numeroString = str(numeroInteiro)
    if numeroInteiro < 1:
        return ("0")
    lista = numeroString.split(".")
    numeroInteiro = int(lista[0])
    numeroTemporario = numeroInteiro
    numeroBinario = []
    while numeroTemporario != 1:
        sobra = numeroTemporario % 2
        numeroTemporario = int(numeroTemporario / 2)
        numeroBinario.append(sobra)
    if numeroTemporario == 1:
        numeroBinario.append(1)
    numeroBinario.reverse()
    numeroBinarioSaida = "".join([str(numeral) for numeral in numeroBinario])
    return(numeroBinarioSaida)

numero = float(input("numero real na base 10 que quer converter: [ex: 6.12]"))
bits = int(input("quantos bits para a parte decimal do binario?"))
parteFracao = fracaoBinario(numero)
parteInteiro = inteiroBinario(numero)
print(f'{numero} transformado para binario fica {parteInteiro}.{parteFracao}')
