# Introdução de POO em Python

class Carro:

    # Método Construtor
    def __init__(self, cor, marca, modelo):

        # Atributo
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    # Métodos
    def ligar(self):
        print("Vrum Vrum")

    def desligar(self):
        print("Cof Cof")


# Criar um objeto "fusca"
# ou criando uma instância do tipo Carro
fusca = Carro("azul", "BMW", "mini cooper")
# parametros devem passados na ordem dos atributos do construtor

# Definindo cor do Carro
# fusca.cor = "azul"
# por segurança não se deve definir um atributo do objeto diretamente, e sim no momento da criação do objeto..

# Ligar carro
fusca.ligar()

# Desligar carro
fusca.desligar()

# Ler cor do carro
print(fusca.cor)
