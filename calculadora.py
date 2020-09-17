from tkinter import *
import time

class Calculadora():
    def __init__(self, master):
        pass

        '''Container PAI'''
        self.Container = Frame(master)
        self.Container.pack()

        '''CAMPO DE SUBTITULO (RÓTULO)'''
        self.titulo = Label(self.Container, text="Calculadora")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.configure(relief="ridge", border= 5, background="blue")#CONFIGURA TODA A PARTE DE DESIGNE
        self.titulo.pack(side=TOP)

        self.hora = Label(self.Container, text=time.asctime(time.localtime((time.time()))))
        self.hora["font"] = ("Arial", "10","bold")
        self.hora.configure(relief="ridge", border=5)
        self.hora.pack()#GERENCIADOR DE GEOMETRIA
 
        #-------------------------------------------------#
        self.contResultado = Frame(master)
        self.contResultado.pack()

        self.msg = Label(self.contResultado, text="")
        self.msg["font"] = ("Arial","20","bold")
        self.msg.pack()
        #-------------------------------------------------#
        '''CONTAINER PAI PARA CAMPO DE TEXTO'''
        self.campoContainer = Frame(master)
        self.campoContainer.pack()
        
        self.campo = Entry(self.campoContainer)
        self.campo["font"] = ("Arial", "20", "bold")
        self.campo["width"] = 18
        self.campo.configure(relief="ridge", border=5)
        self.campo.pack(expand=TRUE)

        self.campo2 = Entry(self.campoContainer)
        self.campo2["font"] = ("Arial", "20", "bold")
        self.campo2["width"] = 18
        self.campo2.configure(relief="ridge", border=5)
        self.campo2.pack(expand=TRUE)

        #-------------------SAIR-------------------------#
        self.containerSair = Frame(master)
        self.containerSair.pack(side=BOTTOM, expand=TRUE, fill="both")

        self.botaoo = Button(self.containerSair)
        self.botaoo["text"] = "Sair"
        self.botaoo["font"] = "Arial"
        self.botaoo["width"] = 5
        self.botaoo["command"] = self.campoContainer.quit
        self.botaoo.pack()       

        #------------------SOMA------------------------------#
        self.contSoma = Frame(master)
        self.contSoma.pack(side=LEFT, expand=TRUE, fill='y') #EXPAND PARA DEIXAR O CAMPO REDIMENCIONAVEL

        self.somador = Button(self.contSoma)
        self.somador["text"] = "+"
        self.somador["font"] = "Arial"
        self.somador["width"] = 5
        self.somador["command"] = self.soma
        self.somador.pack()

        #------------------SUBTRAÇÃO----------------------#
        self.contSubtracao = Frame(master)
        self.contSubtracao.pack(side=RIGHT, expand=TRUE, fill="y")

        self.subtrador = Button(self.contSubtracao)
        self.subtrador["text"] = "-"
        self.subtrador["font"] = "Arial"
        self.subtrador["width"] = 5
        self.subtrador["command"] = self.subtracao
        self.subtrador.pack()
        
        #------------Mutplicacao--------------------------#
        self.contMutplicacao = Frame(master)
        self.contMutplicacao.pack(side=RIGHT, expand=TRUE, fill="y")

        self.Bmultiplica = Button(self.contMutplicacao)
        self.Bmultiplica["text"] = "*"
        self.Bmultiplica["font"] = "Arial"
        self.Bmultiplica["width"] = 5
        self.Bmultiplica["command"] = self.multiplicacao
        self.Bmultiplica.pack()

        #--------------------Divisao----------------------#
        self.contDivisao = Frame(master)
        self.contDivisao.pack()

        self.divisao = Button(self.contDivisao)
        self.divisao["text"] = "%"
        self.divisao["font"] = "Arial"
        self.divisao["width"] = 5
        self.divisao["command"] = self.div
        self.divisao.pack()

    def soma(self):
        resul = int(self.campo.get())
        result = int(self.campo2.get())
        self.msg["text"] = resul + result
        
    def subtracao(self):        
        resul = int(self.campo.get())
        result = int(self.campo2.get())
        if resul > result:
            self.msg["text"] = resul - result
        else:
            self.msg["text"] = result - resul    

    def multiplicacao(self):
        resul = int(self.campo.get())
        result = int(self.campo2.get())
        self.msg["text"] = resul * result

    def div(self):
        resul = int(self.campo.get())
        result = int(self.campo2.get())
        if resul < result:
            self.msg["text"] = float(result / resul)
        elif result == resul:
            self.msg["text"] = float(resul / result)
        else:
            self.msg["text"] = float(resul / result)        
        
root = Tk()
root.title("Calculadora")
root.geometry("300x300+100+100")
Calculadora(root)
root.mainloop()
