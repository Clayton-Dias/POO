#Introdução de POO em Python

class Carro:

    # Método Construtor
    def __init__(self):

        # Atributo
        self.cor = None
        self.marca = None
        self.modelo = None
        pass

    # Métodos
    def ligar(self):
        print("Vrum Vrum")

    def desligar(self):
        print("Cof Cof")


# Criar um objeto "fusca"
fusca = Carro()  # criando uma instância do tipo Carro

#Cor do Carro
fusca.cor = "azul"

#Ligar carro
fusca.ligar()

#Desligar carro
fusca.desligar()

#Ler cor do carro
print(fusca.cor)


#Criando outro objeto
veloz = Carro()
veloz.cor = "prata"
veloz.ligar()
print(veloz.cor)
veloz.desligar()

