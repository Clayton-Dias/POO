#Introdução de POO em Python

class Carro:

    # Método Construtor
    def __init__(self):

        # Atributo
        self.cor = None
        self.marca = None
        self.modelo = None
        #pass

    # Métodos
    def ligar(self):
        print("Vrum Vrum")

    def desligar(self):
        print("Cof Cof")


# Criar um objeto "fusca"
fusca = Carro()  # criando uma instância do tipo Carro

#Definindo cor do Carro
fusca.cor = "azul" 

#Ligar carro
fusca.ligar()

#Desligar carro
fusca.desligar()

#Ler cor do carro
print(fusca.cor)


#Criando outro objeto
veloz = Carro()     #Instância da Classe Carro
veloz.cor = "prata" #Define valor do atributo
veloz.ligar()       #Executa método
print(veloz.cor)    #Mostrar valor do atributo do objeto veloz
veloz.desligar()    #Executa método
