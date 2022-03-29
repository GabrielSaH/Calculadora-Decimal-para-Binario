bits = int(input("quantos bits?")) # quantidade de casas da resposta em binario
objetivo = 56 / 1000  #fraçao a ser representada (0,056 = 56/1000)
denominador = 0  # setado para 0 pq é so para definir uma variavel antes do while
resultado = 0   # setado para 0 pq é so para definir uma variavel antes do while
numeroTeste = 1  # setado para 1 pq se for 0 o primeiro denominador deve ser 2**1
resultadoTeste = 0  # setado para 0 pq é so para definir uma variavel antes do while
listaDecimal = []  
listaFracao = []  
modoBinario = []  
while not resultado == objetivo: # enquanto o resultado nao for igual ao objetivo repita o codigo abaixo:
    denominadorTeste = 2**numeroTeste # o denominador da funçao
    decimalTeste = f"1/{denominadorTeste}"  # tranformando a fraçao em string para o python nao resolver a divisao
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
        print(f"essa é a lista de decimais: {listaDecimal} \r \r")
        print(f"essa é a lista de fraçao:{listaFracao} \r \r")
        print(f"esse é o resultado no numero de bits pedidos: {modoBinario[:bits]}")

