"""
Encapsulamento é um dos princípios fundamentais da programação orientada a objetos (POO) e se refere à prática de restringir o acesso direto aos atributos e métodos de um objeto, para proteger seu estado interno e garantir que ele seja modificado apenas por meio de métodos específicos. Em Python, o encapsulamento é geralmente implementado usando convenções de nomenclatura.

O encapsulamento em Python é uma questão de boas práticas e convenções mais do que de controle estrito de acesso. As convenções de nomenclatura (_ e __) ajudam a comunicar a intenção de acesso e a proteger o estado interno dos objetos, mas não oferecem uma proteção rigorosa como em algumas outras linguagens.
"""
#Atributos e Métodos Públicos
#Por padrão, todos os atributos e métodos em Python são públicos. Isso significa que eles podem ser acessados de fora da classe.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dizer_ola(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

#Atributos e Métodos Protegidos
#Você pode sinalizar que um atributo ou método é protegido (ou seja, deve ser acessado apenas dentro da classe e suas subclasses) usando um único sublinhado (_) antes do nome.
class Pessoa1:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def _dizer_ola_protegido(self):
        print(f"Olá, meu nome é {self._nome} e tenho {self._idade} anos")

#Atributos e Métodos Privados
#Para tornar um atributo ou método verdadeiramente privado e acessível apenas dentro da própria classe, use dois sublinhados (__) antes do nome. Isso causa uma transformação de nome (name mangling) para dificultar o acesso direto.
class Pessoa2:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def __dizer_ola_privado(self):
        print(f"Olá, meu nome é {self.__nome} e tenho {self.__idade} anos")

    def dizer_ola(self):
        return self.__dizer_ola_privado()
    

pessoa = Pessoa("Ana", 30)
print(pessoa.dizer_ola())  # Acesso permitido

pessoa1 = Pessoa1("João", 23)
print(pessoa1._dizer_ola_protegido())  # Acesso permitido, mas não recomendado

pessoa2 = Pessoa2("Caroline", 18)
print(pessoa2.dizer_ola())  # Acesso permitido
# print(pessoa.__dizer_ola_privado())  # Isso causará um erro, pois é privado
# print(pessoa.__nome)  # Isso também causará um erro

#Observação: é possível acessar atributos privados de fora da classe usando o nome transformado (não recomendado)
print(pessoa2._Pessoa2__nome)  # Acesso não recomendado