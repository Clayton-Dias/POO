class User:

    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__email = ""
        self.__password = ""

    # Setter
    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setEmail(self, email):
        self.__email = email

    def setPassword(self, password):
        self.__password = password

    # Getter
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    # Métodos
    def new(self, name, email):
        pass

    def view(id):
        pass

    def delete(id):
        pass


class Student(User):

    def __init__(self):
     
        self.__notas = 0
        self.__presenca = ""
        self.__curso = ""


    # Setter
    def setNotas(self, notas):
        self.__notas = notas

    def setPresenca(self, presenca):
        self.__presenca = presenca

    def setCurso(self, curso):
        self.__curso = curso

    # Getter
    def getNotas(self):
        return self.__notas

    def getPresenca(self):
        return self.__presenca

    def getCurso(self):
        return self.__curso


    
