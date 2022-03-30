import tkinter as tk
from functools import partial

class Calculadora:
    def __init__(self):
        simbolos = ['0','1','2','3','4','5','6','7','8','9','.','=','C','<']
        self.window = tk.Tk()
        tamanho = int(self.window.winfo_screenheight()/2)
        self.window.title('Calculadora decimal para binário')
        self.window.config(bg='black')
        posX = int((self.window.winfo_screenwidth() / 2) - (tamanho / 2))
        posY = int((self.window.winfo_screenheight() / 2) - (tamanho / 2))
        self.window.geometry('{}x{}+{}+{}'.format(int(tamanho/2),tamanho,posX,posY))
        
        self.resultado = tk.Label(text='RESULTADO\n\n',bg='white',fg='black')
        self.resultado.pack(expand=True,fill='both')
        
        self.entradaNumero = tk.Entry(master=self.window)
        self.entradaNumero.pack(expand=True)
        
        self.entradaBits = tk.Entry(master=self.window)
        self.entradaBits.pack(expand=True)
        self.numeroBinario = 10
        
        self.numerosFrame = tk.Frame(master=self.window)
        self.numerosFrame.config(bg='black')
        linha = 0
        posicao = 0
        frame = tk.Frame(master=self.numerosFrame)
        frame.config(bg='black')
        frame.pack(expand=True,fill='both')
        for i in simbolos:
            botao = tk.Button(text=i,master=frame,command=partial(self.adicionarNumero,i))
            posicao += 1
            if posicao >= 3:
                frame = tk.Frame(master=self.numerosFrame)
                frame.config(bg='black')
                frame.pack(expand=True,fill='both')
                posicao = 0
                linha += 1
            botao.pack(side='left',expand=True)
        self.numerosFrame.pack(expand=True,fill='both')
        self.window.mainloop()

    def contadorDecimais(self,numero):
        numeroString = str(numero)
        lista = numeroString.split(".")
        inteiro = int(lista[0])
        decimalStr = str(round(numero - inteiro, 9))
        decimalFloat = float(round(numero - inteiro, 9))
        x = (len(decimalStr) - 2)
        y = 10 ** x
        decimalInt = int(decimalFloat * y)
        return (y, decimalStr, decimalInt)

    def fracaoBinario(self,objetivo):
        divisor, decimalStr, decimalInt = self.contadorDecimais(objetivo)
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
                self.numeroBinario = modoBinario[:self.bits]
                numeroDecimalSaida = "".join([str(numeral) for numeral in self.numeroBinario])
                return (numeroDecimalSaida)
            if len(modoBinario) == self.bits:
                numeroBinario = modoBinario[:self.bits]
                numeroDecimalSaida = "".join([str(numeral) for numeral in numeroBinario])
                return (numeroDecimalSaida)

    def inteiroBinario(self,numeroInteiro):
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

    def calcular(self):
        numero = float(self.entradaNumero.get())
        self.bits = int(self.entradaBits.get())
        parteFracao = self.fracaoBinario(numero)
        resultadoBinario = self.inteiroBinario(numero)
        print(f'{numero} transformado para binario fica {resultadoBinario}')
        resposta = 'RESULTADO\ndecimal: {}\nbinario:{}'.format(numero,resultadoBinario)
        self.resultado['text'] = resposta

    def adicionarNumero(self,numero):
        focus = str(self.entradaNumero.focus_get())
        entrada = ''
        if focus == '.!entry':
            entrada = self.entradaNumero.get()
        if focus == '.!entry2':
            entrada = self.entradaBits.get()
        entradaNova = ''
        if numero not in ['<','C','=']:
            entradaNova = entrada + numero
        else:
            if(numero=='<'):
                entradaNova = entrada[:-1]
                return 
            if(numero=='='):
                self.calcular()
                return 
            if(numero=='C'):
                self.entradaNumero.delete(0,tk.END)
                self.entradaBits.delete(0,tk.END)
                self.resultado['text'] = 'RESULTADO\n\n'

        if focus =='.!entry':
            self.entradaNumero.delete(0,tk.END)
            self.entradaNumero.insert(0,str(entradaNova))
        if focus == '.!entry2':
            self.entradaBits.delete(0,tk.END)
            self.entradaBits.insert(0,str(entradaNova))

Calculadora()   