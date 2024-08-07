class MyClass:
    def __init__(self, value):
        self.__private_attr = value

    def __private_method(self):
        return self.__private_attr

    def public_method(self):
        return self.__private_method()

obj = MyClass(30)
print(obj.public_method())  # Acesso permitido através de método público
# print(obj.__private_attr)  # Erro: Atributo privado não acessível
# print(obj.__private_method())  # Erro: Método privado não acessível