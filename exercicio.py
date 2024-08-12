import re  # biblioteca importada para validação de email usando RegEx
import random
import string

# Criando a classe User
class User:

    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__email = ""
        self.__password = ""

    # Método para validação de email usando RegEx
    # https://catabits.com.br/view/regex_para_validar_emails
    def validate_email(email):

        # Regex para validar endereços de e-mail, usada pelo HTML5
        # OBS: deve estar em uma única linha
        pattern = r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*$'

        # Verifica se o e-mail corresponde ao padrão regex
        if re.match(pattern, email):
            return True
        else:
            return False

    def gerar_senha(self):
        # Caracteres permitidos
        minusculas = string.ascii_lowercase
        maiusculas = string.ascii_uppercase
        digitos = string.digits
        especiais = "_-.+"

        # Garantir que a senha tenha pelo menos um de cada requisito
        senha = [
            random.choice(minusculas),
            random.choice(maiusculas),
            random.choice(digitos),
            random.choice(especiais)
        ]

        # Completar a senha até ter pelo menos 7 caracteres
        todos_caracteres = minusculas + maiusculas + digitos + especiais
        while len(senha) < 7:
            senha.append(random.choice(todos_caracteres))

        # Embaralhar os caracteres para garantir aleatoriedade
        random.shuffle(senha)

        return ''.join(senha)

    # Setter
    def setId(self, id):
        self.__id = int(id)  # tratamento, flitro, sanatização e validação

    def setName(self, name):
        self.__name = name.strip()  # tratamento, flitro, sanatização e validação
        # .strip() excluiu os espaços em branco antes e depois da string, mas não no meio da string.

    def setEmail(self, email):
        # tratamento, flitro, sanatização e validação.
        if self.validate_email(email):
            self.__email = email.strip()
        else:
            print("Erro!! \n Endereço de email inválido")
            exit()

    def setPassword(self, password):
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_\-.+])[A-Za-z\d_\-.+]{7,}$'
        if re.match(regex, password) is not None:
            self.__password = password.strip()
        else:
            print("Erro!", "Senha inválida!")
            exit()
        """
        Exemplo de setter para senha, regras para validar a senha:
            - Pelo menos 7 caracteres
            - Pelo menos 1 letra minúscula
            - Pelo menos 1 letra maiúscula
            - Pelo menos 1 dígito numérico
            - Pelo menos 1 dos caractetes `_`, `-`, `.` ou `+` 
        """

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
        self.setName(name)
        self.setEmail(email)
        self.setPassword(self.gerar_senha())
        # grava novo usuário no banco de dados
        """
        Exemplo no SQL
        INSERT INTO User(name, email, password) VALEUS (self.getName(), self.getEmail(), self.getPassword())
        """

    def view(id):
        # Recebe os dados do banco de dados relativos ao Id
        # SQL → SELECT * FROM User WHERE id = id
        # Insere os dados em um dicionário
        # Retorna o dicionário
        pass

    def delete(id):
        # Busca e apaga o registro do banco de dados relativo ao Id
        # SQL → DELETE * FROM User WHERE id = id
        # Se achou e apagou, retorna "True"
        pass


# Crianado a classe `Student` que herda atributos e métodos a classe `User`.
class Student(User):

    def __init__(self):
        super().__init__()
        self.__notas = {}
        self.__presenca = {}
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
