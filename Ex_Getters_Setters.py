class Animal:

    def __init__(self):

        self.__especie = ""
        self.__genero = ""
        self.__subEspecie = ""

# Encapsulamento com getter e setter

    # SETTERS -> Definir os valor dos atributos encapsulados

    def setEspecie(self, especie):
        # .strip remove espaçoes antes e depois do texto da string
        self.__especie = especie.strip()

    def setGenero(self, genero):
        self.__genero = genero.strip()

    def setSubEspecie(self, subEspecie):
        self.__subEspecie = subEspecie.strip()

    # GETTERS -> Ler os valores dos atributos encapsulados

    def getEspecie(self):
        if self.__especie != "":
            return self.__especie
        else:
            return "Erro ao mostrar espécie"

    def getGenero(self):
        if self.__genero != "":
            return self.__genero
        else:
            return "Erro ao mostrar genêro"

    def getSubEspecie(self):
        if self.__subEspecie != "":
            return self.__subEspecie
        else:
            return "Erro ao mostrar subespécie"


cachorro = Animal()
cachorro.setEspecie("     doginho     ")
#print(cachorro.__especie) # Erro: Atributo privado não acessível
print(cachorro.getEspecie())
