from models.cliente import Cliente
from utils.helper import formata_valor


class Conta:

    codigo = 1000000

    def __init__(self, cliente):
        self.__cc = Conta.codigo + 1
        self.__cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100.0
        self.__saldo_total = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self):
        return f'Conta Corrente: {self.cc}\nCliente: {self.cliente.nome}\n' \
               f'Saldo Total: {formata_valor(self.saldo_total)}'

    @property
    def cc(self):
        return self.__cc

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def saldo_total(self):
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor):
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self):
        return self.saldo + self.limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com Sucesso!')

        else:
            print('Valor inválido, tente novamente.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                print('Saque efetuado com Sucesso!')
            else:
                restante = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                print(f'Você sacou utilizando seu limite, você ainda tem R$ {formata_valor(self.limite)} em seu limite.')
        else:
            print('Saque não realizado, tente novamente.')

    def transferir(self, destino, valor):
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total

            else:
                restante = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                destino.salor = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            print('Transferência realizada com sucesso!')
        else:
            print('Transferência não realizada. Tente novamente!')
