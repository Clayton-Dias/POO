#Heranaça de classe -> Permite criar uma nova classe baseada em uma classe existente, reutilizando seus atributos e métodos. 
# A herança nos permite definir uma classe (filho) que herda todos os métodos e propriedades de outra classe (pai).

#Criando a classe "pai" Pessoa com os atributos pnome (primeiro nome), unome (último nome) e o método printnome, que mostar o pnome e unome quando chamado.
#Classe "pai" é a classe que está sendo herdada, também chamada de classe base.
class Pessoa:

    def __init__(self, pnome, unome):   #A função __init__() é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.
        self.pnome = pnome
        self.unome = unome

    def printNome(self):
        print(self.pnome, self.unome)


#Classe "filho" é a classe que herda de outra classe ("pai"), também chamada de classe derivada.
#Para criar uma classe que herda a funcionalidade de outra classe, envie a classe pai como um parâmetro ao criar o filho classe.
#
class Estudante(Pessoa):    #Agora, a classe Estudante tem as mesmas propriedades e métodos que a classe Pessoa.

    #Quando você adiciona a função __init__(), a classe filha não herda mais a função __init__() do pai.
    # A função __init__() do filho substitui a herança da função __init__() do pai.
    def __init__(self, pnome, unome, ano = 0):
        #Para manter a herança da função __init__() pai, adicione uma chamada a função __init__() do pai.
        #Pessoa.__init__(self,pnome, unome)
        #Python tem a função super() que fará com que a classe filha herde todos os métodos e propriedades de seu pai.
        super().__init__(pnome, unome)
        self.ano = ano


#
x = Estudante("Enzo","Gian", 2020)

#print(x.pnome, x.unome, x.ano)
print(x.printNome(), x.ano)
