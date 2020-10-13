from models.cliente import Cliente
from models.conta import Conta
from time import sleep

contas = []


def main():
    menu()


def menu():
    print(''.center(40, '-'))
    print(' Caixa Eletrônico '.center(40, '-'))
    print(' Rot Bank'.center(40, '-'))
    print(''.center(40, '-'))

    print('Selecione uma das opções disponíveis:')
    print('1- Criar Conta')
    print('2- Efetuar Saque')
    print('3- Efetuar Depósito')
    print('4- Efetuar Transferência')
    print('5- Listar Contas')
    print('6- Sair do sistema')
    opcao = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida, tente novamente.')
        menu()


def criar_conta():
    print('Informe os dados do cliente:')

    nome = input('Nome: ')
    email = input('E-Mail: ')
    cpf = input('CPF: ')
    data_nasc = input('Data de Nascimento dd/mm/AA: ')

    cliente = Cliente(nome, email, cpf, data_nasc)
    conta = Conta(cliente)
    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados da conta:')
    print(''.center(20, '-'))
    print(conta)

    sleep(1)
    menu()


def efetuar_saque():
    if len(contas) > 0:
        cc = int(input('Informe o número de sua Conta Corrente: '))
        conta = buscar_cc(cc)

        if conta:
            valor = float(input('Digite o valor a ser sacado: '))
            conta.sacar(valor)
        else:
            print(f'Não encontramos nenhuma conta de número {cc}!')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(1)
    menu()


def efetuar_deposito():
    if len(contas) > 0:
        cc = int(input('Digite o número de sua Conta Corrente: '))
        conta = buscar_cc(cc)

        if conta:
            valor = float(input('Digite o valor a ser depositado: '))
            conta.depositar(valor)
        else:
            print(f'Não encontramos nenhuma conta de número {cc}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(1)
    menu()


def efetuar_transferencia():
    if len(contas) > 0:
        cc = int(input('Informe o número de sua Conta Corrente: '))
        conta = buscar_cc(cc)

        if conta:
            ccd = int(input('Informe o número da Conta Corrente destino: '))
            contad = buscar_cc(ccd)
            if contad:
                valor = float(input(f'Informe o valor a ser transferido para a conta {ccd}: '))
                conta.transferir(contad, valor)
            else:
                print(f'Não encontramos nenhuma conta destino de número {ccd}')

        else:
            print(f'Não encontramos nenhuma conta de número {cc}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(1)
    menu()


def listar_contas():
    if len(contas) > 0:
        print('Listagem de Contas')
        for conta in contas:
            print(conta)
            print(''.center(20, '-'))
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(1)
    menu()


def buscar_cc(cc):
    c = None

    if len(contas) > 0:
        for conta in contas:
            if conta.cc == cc:
                c = conta
    return c


if __name__ == '__main__':
    main()
