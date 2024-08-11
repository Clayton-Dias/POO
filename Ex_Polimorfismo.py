#A palavra "polimorfismo" significa "muitas formas" e, na programação, refere-se a métodos/funções/operadores com o mesmo nome que podem ser executados em muitos objetos ou classes.
#O polimorfismo é frequentemente usado em métodos de classe, onde podemos ter vários classes com o mesmo nome de método.

#Classe Pai
class Veiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("Ligando...")
    
    def desligar(self):
        print("Desligando...")

class Carro(Veiculo):

    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self.ano = ano

    def ligar(self):
        print(f"{super().ligar()}  o carro" ) 

    def desligar(self):
        print(f"{super().ligar()} o carro")   

class Barco(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def ligar(self):
        print(f"{super().ligar()} o barco")

    def desligar(self):
        print(f"{super().desligar()} o barco")

class Aviao(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def ligar(self):
        print("Decolando")

    def desligar(self):
        print("Pousando")


#Criando objetos: 
carro = Carro("Lamborghini", "Aventador", 2016) #Obejto Carro

barco = Barco("Fibrafort","Focker 272 GTO") #Obejto Barco

aviao = Aviao("Boeing","747-400") #Obejto Aviao

for x in (carro, barco, aviao):
    print(x.marca, x.modelo)
    #print(x.modelo)
    x.ligar()
    x.desligar()

