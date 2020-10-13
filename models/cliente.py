from datetime import date
from utils.helper import date_str, str_date


class Cliente:

    contador = 0

    def __init__(self, nome, email, cpf, data_nasc):
        self.__codigo = Cliente.contador + 1
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_nasc = str_date(data_nasc)
        self.__data_cad = date.today()
        Cliente.contador += 1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nasc(self):
        return date_str(self.__data_nasc)

    @property
    def data_cad(self):
        return date_str(self.__data_cad)

    def __str__(self):
        return f'Código: {self.codigo}\nNome: {self.nome}\nData de Nascimento: {self.data_nasc}\n' \
               f'Cadastro: {self.data_cad}'
