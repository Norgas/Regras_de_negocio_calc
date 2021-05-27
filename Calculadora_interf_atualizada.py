import tkinter as tk
import math ,os
from operacoes.cosseno import cos
from operacoes_arquivo import *

class Calculadora():
    def __init__(self):
        self.base = tk.Tk() #abre a janela Tkinter
        self.base.geometry("305x210") #define as dimensoes da janela
        self.base.title("Calculadora")
        self.expressao = ''
        self.primeira_instancia = True #Boolean para distinguir primeiro numero do segundo inserido
        self.angulo = True
        self.run()

    def igual(self):
        self.primeira_frase = float(self.primeira_frase)
        try:
            self.segunda_frase = float(self.segunda_frase)
        except:
            pass
        self.visor_operacao = tk.Label(self.base, text = '          ')
        self.visor_operacao.grid(column = 4, row = 0)

        if self.algarismo == '+':
            self.resul = soma(self.primeira_frase, self.segunda_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == '-':
            self.resul = subtracao(self.primeira_frase, self.segunda_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == '*':
            self.resul = multiplicacao(self.primeira_frase, self.segunda_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == '/':
            self.resul = divisao(self.primeira_frase, self.segunda_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == '^':
            self.resul = exponenciacao(self.primeira_frase, self.segunda_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == '√':
            self.resul = raiz(self.primeira_frase, self.segunda_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == '!':
            self.resul = fatorial(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == 'cos':
            if self.angulo == True:
                self.resul = cos(self.primeira_frase)
            else:
                self.resul = cos_radiano(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == 'ln':
            self.resul = ln(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == 'tg':
            if self.angulo == True:
                self.resul = tan(self.primeira_frase)
            else:
                self.resul = tan_radiano(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == 'sin':
            if self.angulo == True:
                self.resul = sen(self.primeira_frase)
            else:
                self.resul = sen_radiano(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == 'log':
            self.resul = log(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == 'sec':
            self.resul = sec(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == 'cossec':
            self.resul = cossec(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.algarismo == 'cotg':
            self.resul = cotg(self.primeira_frase)
            self.visor_numero = tk.Label(self.frame_visor, text = self.resul)
            self.visor_numero.grid(column=5,row=0, columnspan=4)
        
        self.primeira_frase = self.resul

    def angulo_rad(self, opcao):
        if opcao == 'rad':
            self.angulo = False
        if opcao == 'ang':
            self.angulo = True

    def digito(self, x):
        self.expressao = self.expressao + str(x)
        self.visor_numero = tk.Label(self.frame_visor, text = self.expressao)
        self.visor_numero.grid(column=5,row=0, columnspan=4)
        if self.primeira_instancia: 
            self.primeira_frase = self.expressao
            #print(self.primeira_frase + "PRIMEIRA")
        else:
            self.segunda_frase = self.expressao
            #print(self.segunda_frase + "SEGUNDA")

    def negativo(self):
        self.primeira_frase = 0 - int(self.primeira_frase)
        self.visor_operacao = tk.Label(self.base, text = '-')
        self.visor_operacao.grid(column = 4, row = 0)

    def operacao(self, algarismo):
        self.expressao = ''
        self.frame_visor.destroy()
        self.visores()
        self.visor_operacao = tk.Label(self.base, text = algarismo)
        self.visor_operacao.grid(column = 4, row = 0)

        if algarismo == '+':
            self.algarismo = '+'
            self.primeira_instancia = False
        if algarismo == '-':
            self.algarismo = '-'
            self.primeira_instancia = False
        if algarismo == '*':
            self.algarismo = '*'
            self.primeira_instancia = False
        if algarismo == '/':
            self.algarismo = '/'
            self.primeira_instancia = False
        if algarismo == '^':
            self.algarismo = '^'
            self.primeira_instancia = False
        if algarismo == '√':
            self.algarismo = '√'
            self.primeira_instancia = False
        if algarismo == '!':
            self.algarismo = '!' 
        if algarismo == 'cos':
            self.algarismo = 'cos' 
        if algarismo == 'ln':
            self.algarismo = 'ln' 
        if algarismo == 'tg':
            self.algarismo = 'tg' 
        if algarismo == 'sin':
            self.algarismo = 'sin'
        if algarismo == 'log':
            self.algarismo = 'log'
        if algarismo == 'sec':
            self.algarismo = 'sec'
        if algarismo == 'cossec':
            self.algarismo = 'cossec'
        if algarismo == 'cotg':
            self.algarismo = 'cotg'

    def clear(self):
        self.frame_visor.destroy()
        self.expressao = ''
        self.primeira_instancia = True
        self.visores()

    def delete(self):
        expressao = []
        string = ''
        for digito in self.expressao:
            expressao.append(digito)
        expressao.pop()
        for elemento in expressao:
            string += str(elemento)

    def visores(self):
        self.frame_visor = tk.Frame()
        self.frame_visor.grid(column=5 , row=0, columnspan=4)
    
        self.visor_numero = tk.Label(self.frame_visor, text = '')
        self.visor_numero.grid(column=5,row=0, columnspan=4)

        self.visor_operacao = tk.Label(self.base, text = '          ')
        self.visor_operacao.grid(column = 4, row = 0)

    def botoes(self):

        botao7 = tk.Button(text="7", width=4, height=2, command = lambda :self.digito(7))
        botao7.grid(column=4,row=1)

        botao8 = tk.Button(text="8", width=4, height=2,command = lambda :self.digito(8))
        botao8.grid(column=5,row=1 )

        botao9 = tk.Button(text="9", width=4, height=2,command = lambda :self.digito(9))
        botao9.grid(column=6 ,row=1 )

        botao4 = tk.Button(text="4", width=4, height=2,command = lambda :self.digito(4))
        botao4.grid(column=4 ,row=2 )

        botao5 = tk.Button(text="5", width=4, height=2,command = lambda :self.digito(5))
        botao5.grid(column=5 ,row=2 )

        botao6 = tk.Button(text="6", width=4, height=2,command = lambda :self.digito(6))
        botao6.grid(column=6 ,row=2 )

        botao1 = tk.Button(text="1", width=4, height=2,command = lambda :self.digito(1))
        botao1.grid(column=4 ,row=3)

        botao2 = tk.Button(text="2", width=4, height=2,command = lambda :self.digito(2))
        botao2.grid(column=5 ,row=3 )

        botao3 = tk.Button(text="3", width=4, height=2,command = lambda :self.digito(3))
        botao3.grid(column=6 ,row=3)

        soma_botao = tk.Button(text = "+", width=4, height=2, command=lambda :self.operacao('+'))
        soma_botao.grid(column=7 ,row=3 )

        subtracao_botao = tk.Button(text = "-", width=4, height=2, command=lambda :self.operacao('-'))
        subtracao_botao.grid(column=8 ,row=2 )

        multiplicacao_botao = tk.Button(text = "*", width=4, height=2 , command=lambda :self.operacao('*'))
        multiplicacao_botao.grid(column=8 ,row=3 )

        divisao_botao = tk.Button(text = "/", width=4, height=2, command=lambda :self.operacao('/'))
        divisao_botao.grid(column=8 ,row=4 )

        exponencial_botao = tk.Button(text= "x^y", width=4, height=2, command=lambda :self.operacao('^'))
        exponencial_botao.grid(column= 3,row=1 )

        raiz_botao = tk.Button(text = "y√x", width=4, height=2, command=lambda :self.operacao('√'))
        raiz_botao.grid(column=3 ,row=2 )

        ac_botao = tk.Button(text = "AC", width = 4,height = 5, command = self.clear)
        ac_botao.grid(column=7,row=1, rowspan=2)

        del_botao = tk.Button(text = "DEL", width = 4,height = 2, command = self.delete)
        del_botao.grid(column= 8, row = 1)

        rad_botao = tk.Button(text = "rad", width=4, height=2, command= lambda : self.angulo_rad('rad'))
        rad_botao.grid(column=0,row=0)

        ang_botao = tk.Button(text = "ang", width=4, height=2, command = lambda : self.angulo_rad('ang'))
        ang_botao.grid(column= 2, row= 0)

        fat_botao = tk.Button(text = "x!", width=4, height=2,command=lambda :self.operacao('!'))
        fat_botao.grid(column= 3, row= 0)

        cos_botao = tk.Button(text = "cos", width=4, height=2,command=lambda :self.operacao('cos'))
        cos_botao.grid(column= 0, row= 2)

        ln_botao = tk.Button(text = "ln", width=4, height=2,command=lambda :self.operacao('ln'))
        ln_botao.grid(column= 2, row= 2)

        tg_botao = tk.Button(text = "tg", width=4, height=2,command=lambda :self.operacao('tg'))
        tg_botao.grid(column= 0, row= 3)

        e_botao = tk.Button(text = "e", width=4, height=2,command = lambda :self.digito(math.e))
        e_botao.grid(column= 2, row= 3)

        pi_botao = tk.Button(text = "π", width=4, height=2,command = lambda :self.digito(math.pi))
        pi_botao.grid(column= 3, row= 3)

        sin_botao = tk.Button(text = "sin", width=4, height=2,command=lambda :self.operacao('sin'))
        sin_botao.grid(column= 0, row= 1)
        
        sec_botao = tk.Button(text= "sec", width=4, height=2,command=lambda :self.operacao('sec'))
        sec_botao.grid(column=3, row=4)

        cossec_botao = tk.Button(text= "cossec", width=4, height=2,command=lambda :self.operacao('cossec'))
        cossec_botao.grid(column=2, row=4)

        cotg_botao = tk.Button(text= "cotg", width=4, height=2,command=lambda :self.operacao('cotg'))
        cotg_botao.grid(column=0, row=4)

        log_botao = tk.Button(text = "log", width=4, height=2,command=lambda :self.operacao('log'))
        log_botao.grid(column= 2, row= 1)

        botao0 = tk.Button(text="0", width=4, height=2, command = lambda :self.digito(0))
        botao0.grid(column=6 ,row=4 )

        igual_botao = tk.Button(text="=", width=4, height=2, command = self.igual)
        igual_botao.grid(column=7 ,row=4 )

        ponto_botao = tk.Button(text = ".", width=4, height=2,command = lambda :self.digito('.'))
        ponto_botao.grid(column=5,row=4)

        negativo_botao = tk.Button(text = "(-)", width=4, height=2,command = self.negativo)
        negativo_botao.grid(column=4,row=4)

    def run(self):
        self.running = True
        while self.running:
            self.visores()
            self.botoes()
            self.base.mainloop()

calc = Calculadora()

